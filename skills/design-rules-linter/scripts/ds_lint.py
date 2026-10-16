#!/usr/bin/env python3
"""Design-system linter. Stdlib only. Heuristic and line-based by design."""
import argparse, json, os, re, sys

DEFAULTS = {
    "extensions": [".tsx", ".jsx", ".ts", ".js", ".vue", ".svelte", ".html", ".css", ".scss"],
    "ignore_dirs": ["node_modules", "dist", "build", ".next", ".git", "coverage"],
    "token_files": ["tokens.css", "theme.css", "tokens.ts", "tailwind.config.js", "tailwind.config.ts"],
    "allowed_px": [0, 1, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64],
    "allowed_icon_sizes": [16, 20],
    "disabled_rules": [],
    "link_markers": ["<a ", "Link", "href"],
}

HEX = re.compile(r"#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b")
FUNC_COLOR = re.compile(r"\b(?:rgba?|hsla?|oklch|oklab)\s*\(")
ARBITRARY = re.compile(r"\b[a-z-]+-\[[^\]\s]+\]")
PX = re.compile(r"(?<![\w.#-])(-?\d+(?:\.\d+)?)px\b")
ICON_SIZE = re.compile(r"<\w*Icon\w*[^>]*\bsize=\{?(\d+)\}?|<[A-Z]\w*[^>]*\bicon\b[^>]*\bsize=\{?(\d+)\}?")
RAW_SHADOW_CSS = re.compile(r"box-shadow\s*:\s*(?!var\(|none|inherit|initial|unset)")
RAW_SHADOW_TW = re.compile(r"\bshadow-\[")
POINTER = re.compile(r"cursor-pointer|cursor\s*:\s*pointer")
HOVER_REVEAL = re.compile(
    r"(?:group-hover|peer-hover|hover):(?:opacity-(?:[1-9]\d*)|visible|block|flex|inline-flex|inline-block|translate-\S+)"
)
HOVER_CSS = re.compile(r":hover[^{]*\{[^}]*(?:display\s*:\s*(?!none)|visibility\s*:\s*visible|opacity\s*:\s*[1-9.])")
INLINE_STYLE = re.compile(
    r"style=\{\{[^}]*\b(?:color|background(?:Color)?|boxShadow|borderRadius|fontSize|fontWeight|padding|margin|border)\b"
)
ALLOW = re.compile(r"ds-allow:\s*([a-z-]+)\s*(.*)")

HINTS = {
    "raw-color": "Use a colour token/semantic class. Status colours only for status.",
    "arbitrary-value": "Arbitrary utility = override. Use a scale value, a component prop, or flag a ds-gap.",
    "off-scale-px": "Use a spacing/size token from the scale.",
    "icon-size": "Use one of the allowed icon sizes.",
    "raw-shadow": "Use an elevation level token (resting < raised < floating < overlay).",
    "pointer-cursor": "Pointer cursor is for links only. Use default cursor for buttons/rows.",
    "hover-reveal": "Nothing hides behind hover. Render it visibly; hover may only show interactivity.",
    "inline-style": "Inline visual styles bypass the system. Use tokens/components.",
}


def load_config(path):
    cfg = dict(DEFAULTS)
    path = path or ("design-system.rules.json" if os.path.exists("design-system.rules.json") else None)
    if path:
        with open(path) as f:
            cfg.update(json.load(f))
    return cfg


def iter_files(paths, cfg):
    for p in paths:
        if os.path.isfile(p):
            yield p
            continue
        for root, dirs, files in os.walk(p):
            dirs[:] = [d for d in dirs if d not in cfg["ignore_dirs"]]
            for fn in files:
                if os.path.splitext(fn)[1] in cfg["extensions"]:
                    yield os.path.join(root, fn)


def check_line(line, ctx_css, is_token_file, cfg):
    found = []
    code = line
    if not is_token_file and (HEX.search(code) or FUNC_COLOR.search(code)):
        # ignore var(--x, #fff) fallbacks? no: still a literal. Flag.
        found.append("raw-color")
    if ARBITRARY.search(code):
        found.append("arbitrary-value")
    if ctx_css and not is_token_file:
        for m in PX.finditer(code):
            if float(m.group(1)) not in [float(x) for x in cfg["allowed_px"]] and abs(float(m.group(1))) not in [float(x) for x in cfg["allowed_px"]]:
                found.append("off-scale-px")
                break
    m = ICON_SIZE.search(code)
    if m:
        size = int(m.group(1) or m.group(2))
        if size not in cfg["allowed_icon_sizes"]:
            found.append("icon-size")
    if RAW_SHADOW_CSS.search(code) or RAW_SHADOW_TW.search(code):
        found.append("raw-shadow")
    if POINTER.search(code) and not any(k in code for k in cfg["link_markers"]):
        found.append("pointer-cursor")
    if HOVER_REVEAL.search(code) or HOVER_CSS.search(code):
        found.append("hover-reveal")
    if INLINE_STYLE.search(code):
        found.append("inline-style")
    return [r for r in found if r not in cfg["disabled_rules"]]


def lint_file(path, cfg):
    violations, deviations = [], []
    is_css = path.endswith((".css", ".scss"))
    is_token = os.path.basename(path) in cfg["token_files"]
    try:
        lines = open(path, encoding="utf-8", errors="ignore").read().splitlines()
    except OSError:
        return violations, deviations
    for i, line in enumerate(lines, 1):
        rules = check_line(line, is_css or "style" in line or "px" in line, is_token, cfg)
        if not rules:
            continue
        window = line + " " + (lines[i - 2] if i > 1 else "")
        allows = {m.group(1): m.group(2).strip(" */->}") for m in ALLOW.finditer(window)}
        for r in rules:
            if r in allows:
                if allows[r]:
                    deviations.append({"file": path, "line": i, "rule": r, "reason": allows[r]})
                else:
                    violations.append({"file": path, "line": i, "rule": r,
                                       "text": line.strip()[:140],
                                       "hint": "ds-allow needs a reason. " + HINTS[r]})
            else:
                violations.append({"file": path, "line": i, "rule": r,
                                   "text": line.strip()[:140], "hint": HINTS[r]})
    return violations, deviations


def main():
    ap = argparse.ArgumentParser(description="Design-system linter")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--config")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    cfg = load_config(a.config)
    V, D = [], []
    for f in iter_files(a.paths, cfg):
        v, d = lint_file(f, cfg)
        V += v
        D += d
    if a.json:
        print(json.dumps({"violations": V, "deviations": D}, indent=2))
    else:
        for v in V:
            print(f"{v['file']}:{v['line']}  [{v['rule']}]  {v['text']}\n    -> {v['hint']}")
        if D:
            print("\nAllowed deviations (human should review):")
            for d in D:
                print(f"  {d['file']}:{d['line']} [{d['rule']}] {d['reason']}")
        print(f"\n{len(V)} violation(s), {len(D)} allowed deviation(s).")
    sys.exit(1 if V else 0)


if __name__ == "__main__":
    main()
