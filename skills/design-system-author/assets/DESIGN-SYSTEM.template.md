# <Product> design system

> Read this before writing any UI. These are decisions, not suggestions. If something is
> missing, don't improvise: see "When the system doesn't cover it".

## How to work
1. Existing **pattern** → 2. existing **component** → 3. composition → 4. token-only glue → 5. stop and flag.
An override means a missing component or a misuse.

## Tokens
**Spacing:** 4, 8, 12, 16, 24, 32, 48, 64 (nothing else)
**Radius:** <sm / md / lg: when each is used>
**Type:** <3-5 text styles, one line each: where used>
**Icons:** <sizes allowed and where each applies>

### Colour
| Role | Token | Use |
|---|---|---|
| Text / surface / border | ... | ... |
| Brand (product) | ... (cool range only) | links, focus, selected |
| Brand (assets only) | full palette | marketing, illustration |
| Success / warning / danger / info | ... | **status only**, never decoration or hover |

Why: brand colour near a status colour gets misread as that status.

### Elevation
| Level | Token | Use |
|---|---|---|
| 0 resting | ... | cards on page |
| 1 raised | ... | sticky bars, popovers |
| 2 floating | ... | menus, dropdowns |
| 3 overlay | ... | modals, command palette |
Heavier = higher. Inner (inset) shadow allowed on: <components>.

## Components
For each: allowed sizes/variants **(and only these)**, when to use, when *not* to.
- Button: <variants>, <sizes>. One primary per view.
- ...

## Patterns
### <Pattern name>  (e.g. Destructive confirm)
- **Problem:** ...
- **Structure:** components in order
- **Rules:** copy tone, button order, default focus, etc.
- **Don't:** ...

## Interaction rules
- Hover shows *interactivity*, never *functionality*. Nothing hides behind hover or disappears with its button in it (hard to find on touch and keyboard).
- Pointer cursor on links only. Buttons and rows use the default cursor.
- Every interactive element has a visible focus state and a ≥ 40px target on touch.
- Icon-only buttons have an accessible label.
- <add your own, each with a one-line reason>

## When the system doesn't cover it
Build the closest compliant version. Mark `ds-gap: <what/why>` in code. List gaps in your reply.
Add to the system only after a need repeats; otherwise rethink the design.

## Human judgment
The system can't decide whether a screen solves the user's problem or has the product's
character. A designer or design engineer makes the final call.

## Gaps backlog
- (date) <gap> – seen N times

## Changelog
- (date) <change>
