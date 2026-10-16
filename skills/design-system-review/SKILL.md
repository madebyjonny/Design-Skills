---
name: design-system-review
description: Reviews UI code, screenshots, or a pull request against the design system and produces a short, prioritised deviation report that separates mechanical violations from judgment calls a human must make. Use when the user asks to review, audit, critique, QA, or sanity-check UI for consistency, when finishing a UI task (to self-review), or when comparing screens side by side. Trigger on "does this follow our design system", "review this component", "is this consistent", or any request to check agent-generated UI before merging.
---

# Design system review

Agents are good at checking rules and bad at knowing whether the result is *good*.
This skill splits review into those two halves so nobody mistakes a clean lint for
good design.

## Process

1. **Load the system** (see `design-system-first`, Step 1). Review against the project's rules, not generic taste.
2. **Run the mechanical pass** with `design-rules-linter` if there's code. Collect its output as-is.
3. **Run the structural pass** (below) by reading the code or looking at the screenshot.
4. **Run the consistency pass**: compare with 2-3 existing screens that solve a similar problem. Put them side by side mentally: do icon sizes, spacing rhythm, heading levels, button hierarchy, and empty/loading/error states match? Inconsistency hides here, not in any single file.
5. **Write the report** in the format below. Keep it short; reviewers skim.

## Structural pass: questions to ask

- **Decision ladder**: Was an existing pattern available and ignored? Is a component re-implemented by hand?
- **Overrides**: Any `className`/`style` that changes look? Each one means "missing component or misuse". Which?
- **Variants**: Does it use only documented sizes/variants? Any invented option?
- **Colour semantics**: Are status colours (success/warn/error) used only for status? Could any brand/link/hover colour be mistaken for a status? In product UI, brand colour should come from the cool, non-status end of the palette.
- **Elevation**: Does depth match position? Resting surfaces lighter than floating ones; overlays strongest. Is a shadow used where a border or spacing would do?
- **Interaction rules**: Anything hidden behind hover? Pointer cursor on non-links? Actions reachable by keyboard and touch? Visible focus ring? Disabled vs. loading states present?
- **States**: Empty, loading, error, long-text, and narrow-width behaviour all handled by the pattern, not ad hoc?
- **Accessibility basics**: contrast, labels on icon-only buttons, tap target size, heading order.

## Report format

```
# Design system review: <thing reviewed>

**Verdict:** Ship / Fix first / Rethink   (one line why)

## Mechanical violations (agent can fix)
- file:line [rule] what & fix

## Pattern & component issues (agent can fix, confirm approach)
- what's off, which pattern/component should be used

## Judgment calls (needs a human: designer / design engineer)
- Does this solve the actual problem? Is the hierarchy right? Does it feel like the product?
- Specific questions, not vague worries.

## Possible system gaps
- Needs I saw that the system doesn't cover; seen N times; suggest: variant / pattern / component / one-off
```

## Rules for the reviewer

- Be specific: file, line, rule, concrete fix. "Spacing feels off" is not a finding.
- Don't pad. If the screen is clean, say so in two lines.
- Never invent rules the system doesn't have. If you think a rule *should* exist, put it under "Possible system gaps".
- Keep "judgment calls" honest. If you can't verify taste, say that a human must.
