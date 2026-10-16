---
name: design-system-first
description: Makes an agent build UI strictly from the project's design system instead of inventing styles. Use whenever the task involves building, editing, or restyling any UI (components, pages, screens, dashboards, forms, emails, docs sites), even if the user never mentions a "design system". Trigger on words like component, page, layout, screen, button, modal, form, table, theme, style, CSS, Tailwind, or "make it look like". Also use when a repo contains DESIGN-SYSTEM.md, a tokens file, a components/ui folder, or a Storybook. Apply BEFORE writing any markup or styles.
---

# Design system first

Agents build fast and default to the most generic answer. A design system exists so that
decisions get made once, by people with taste, instead of re-made (slightly differently)
on every screen. Your job is to *spend the system's decisions*, not to make new ones.

Most inconsistency comes from many individually reasonable choices: a 16px icon here,
a 20px one there. Both look fine alone; side by side the product feels stitched together.
So the goal is fewer decisions, not better-looking ones.

## Step 1: Find the system (before writing anything)

Look, in this order, and read what you find:

1. Instruction files: `DESIGN-SYSTEM.md`, `AGENTS.md`, `CLAUDE.md`, `docs/design/*`
2. Tokens: CSS variables, `tailwind.config.*`, `theme.ts`, `tokens.json`
3. Components: `components/ui`, `packages/ui`, Storybook stories
4. `design-system.rules.json` (machine-readable rules, if present)
5. Two or three existing screens similar to the one you're building

If nothing exists, say so, and ask whether to proceed with the `design-system-author`
skill first (recommended) or to build with neutral, minimal defaults and flag everything
as provisional. Do not silently invent a visual language.

## Step 2: Climb the decision ladder

For every UI need, stop at the first rung that works:

1. **Existing pattern** (a documented solution to this recurring problem, e.g. "empty state",
   "confirm destructive action", "settings form"). Copy its structure whole.
2. **Existing component** with its existing props and variants.
3. **Composition** of existing components with no style overrides.
4. **Token-only styling** (spacing/colour/type/shadow tokens) for glue between components.
5. **Stop and escalate.** Anything below this line is a *new decision*, and new decisions
   belong to a human.

The test: if you need an override (`className` that changes colour/size, inline `style`,
a one-off hex, an arbitrary value like `p-[13px]`), then either the component is missing
or you're misusing it. An override is a symptom, not a solution.

## Step 3: When the ladder runs out

Never quietly improvise. Instead:

- Build the closest compliant version using rungs 1-4.
- Mark the gap in code with `// ds-gap: <what is missing and why>` (use the file's comment syntax).
- List every gap at the end of your reply under **"Design system gaps"** with a proposed
  addition (new variant? new pattern? genuinely new component?) and whether you saw the
  need more than once (repeating need = candidate for the system; one-off = rethink the design).

Do not add variants or sizes "just in case". Nothing enters the system before there is a
real, repeating use case.

## Step 4: Check yourself

Before finishing, run `design-rules-linter` if available, and skim `references/self-check.md`.
Report honestly: what you matched, what you couldn't, what needs a human's call.

## What you must not do

- Don't invent colours, sizes, radii, shadows, or font weights. Use tokens.
- Don't pick a size or variant from taste. Use the documented default; if there are no
  defaults documented, use the smallest/most neutral option and flag it.
- Don't restyle a component to "fix" it locally. Report it.
- Don't claim the result is production-ready. Even with constraints, agent output is a better
  *start*; a human still judges whether it solves the real problem with taste.

## Putting this in a repo permanently

`references/agents-md-snippet.md` has a short block to paste into `AGENTS.md`/`CLAUDE.md`
so every agent session starts constrained.
