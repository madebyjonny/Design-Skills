---
name: design-rules-linter
description: Runs a deterministic linter that catches design-system violations in UI code (raw hex colours, arbitrary px/Tailwind values, off-scale icon sizes, hardcoded shadows, pointer cursors on non-links, actions hidden behind hover, inline styles). Use after writing or editing any front-end code (React, Vue, Svelte, HTML, CSS, Tailwind) and whenever the user asks to audit, check, enforce, or clean up styling consistency, even if they don't say "lint". Also use to set up or tune a design-system.rules.json for a repo.
---

# Design rules linter

Prompts persuade; scripts verify. Instructions like "use tokens only" drift over a long
session, so check them mechanically. `scripts/ds_lint.py` is a dependency-free Python
script (stdlib only) that scans UI files for the violations that most often creep in.

## Run it

```bash
python scripts/ds_lint.py src/            # scan a folder
python scripts/ds_lint.py src/Button.tsx  # or specific files
python scripts/ds_lint.py src/ --json     # machine-readable
python scripts/ds_lint.py src/ --config design-system.rules.json
```

It looks for `design-system.rules.json` in the current directory if `--config` is omitted;
otherwise it uses built-in defaults. Exit code is 1 if there are violations.

## Rules

| id | Catches | Why |
|---|---|---|
| `raw-color` | hex/rgb/hsl literals outside token files | colour drift; status-vs-brand confusion |
| `arbitrary-value` | Tailwind `p-[13px]`, `text-[#fff]` | an override pretending to be a utility |
| `off-scale-px` | CSS px values not on the spacing/size scale | the "16 vs 14 vs 20" problem |
| `icon-size` | icon `size={}` not in the allowed set | same |
| `raw-shadow` | literal `box-shadow` / `shadow-[...]` | elevation must come from levels |
| `pointer-cursor` | `cursor-pointer` / `cursor: pointer` not on a link | convention: pointer means link |
| `hover-reveal` | content/actions revealed only on hover | invisible to touch & keyboard users |
| `inline-style` | `style={{ ... }}` with visual properties | bypasses the system |

Defaults are strict-but-sane starting points; the real source of truth is the repo's own
config. Copy `assets/design-system.rules.example.json` to the repo root and edit it to
match the project's actual scale (allowed px values, icon sizes, token files, disabled rules).

## Working with the output

1. Fix real violations by moving *up the decision ladder* (see `design-system-first`):
   swap the literal for a token, swap the hack for a component, or restructure the UI.
   Do **not** fix a warning by making the linter quieter.
2. If a violation is genuinely unavoidable, annotate the line (or the line above) with
   `ds-allow: <rule-id> <reason>`, e.g. `/* ds-allow: raw-color brand asset, not product UI */`.
   The reason is required; the linter rejects empty ones. Allowed exceptions are listed
   in a "deviations" section of the output so a human can review them.
3. Never edit the rules file to silence findings unless the user asked you to change the system.
4. Re-run until clean, then report: violations fixed, deviations allowed (with reasons).

## Limits (say so when relevant)

It is a line-based heuristic, not a parser. It can't know whether an element is "really"
a link, so `pointer-cursor` skips lines that visibly contain `<a`, `Link`, or `href` and
flags the rest for you to confirm. It also can't judge taste or hierarchy. Pair it with
`design-system-review` for the judgment calls.
