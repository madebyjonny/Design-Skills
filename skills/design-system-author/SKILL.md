---
name: design-system-author
description: Creates or tightens the written design-system constraints an agent needs (DESIGN-SYSTEM.md, tokens, patterns, interaction rules, and a design-system.rules.json for the linter) by interviewing the user and auditing existing UI. Use when a project has no design system docs, when agents keep producing inconsistent UI, when the user wants to cut down component variants, define patterns, document interaction rules, set up elevation/colour semantics, or "make our design system agent-friendly". Also use when design-system-first reports repeated gaps.
---

# Design system author

A system an agent can obey is short, opinionated, and written as decisions, not options.
More baked-in constraints give an agent a more accurate first attempt; every option you
leave open is a guess it will make differently each time.

## Principles to design from

1. **Constraints are freedom.** Every extra size or variant is a decision someone makes differently. Cut options to what the product actually uses. No new component without a repeating use case; otherwise it's an override.
2. **Design the interface first, componentise second.** Look at real screens, find what recurs, then lift that into components. Constraints discovered this way are better than invented ones.
3. **Patterns beat components for agents.** A pattern ("destructive confirm", "settings form", "empty state") answers many questions at once, so there is less to guess and less to get wrong. Users also learn it once.
4. **Interaction rules are part of the system.** Write them as rules with reasons (see template).
5. **Colour has meaning.** Keep brand colours distinguishable from status colours (e.g. a link hover in a green-ish brand colour reads as "success"). In product UI, restrict brand use to a palette range that can't be mistaken for status.
6. **Elevation is a scale.** A small number of shadow levels (about four), stronger the higher an element floats; some depth belongs on inner components (inset) rather than outer boxes.
7. **Humans keep the judgment.** The system encodes decisions; it can't tell whether a solution is right for the problem. Say so in the doc.

## Workflow

1. **Audit** (read, don't ask yet): collect from the codebase every distinct colour, font size, spacing value, radius, shadow, icon size, and button/input variant. Count usages. The long tail is your inconsistency; the head is your de facto system.
2. **Propose cuts**: for each category, recommend the smallest set covering ~95% of use, mapping every outlier to its nearest survivor. Show counts so the user can decide quickly.
3. **Interview** for what code can't tell you. Ask in small batches (max 3 questions): taste calls the user cares about, hard rules ("hover never reveals actions"), brand colours that collide with status, who has final say.
4. **Extract patterns**: identify 3-8 recurring problems and write each as a pattern (see template). Start with what already works in the product.
5. **Write `DESIGN-SYSTEM.md`** from `assets/DESIGN-SYSTEM.template.md`. Keep it under ~300 lines. Decisions, not essays.
6. **Write `design-system.rules.json`** so `design-rules-linter` enforces the same numbers (allowed px, icon sizes, token files). The doc and the config must agree.
7. **Add the agent block**: paste `design-system-first/references/agents-md-snippet.md` into AGENTS.md / CLAUDE.md.
8. **Test it**: ask an agent to build one new screen with only the doc; run the linter; note every place it had to guess. Each guess is a missing rule. Add it, repeat.

## Style of the doc

- Imperative and specific: "Icons are 16px, or 20px in page headers. No other sizes."
- Give the *why* in one line so the agent generalises to cases you didn't list.
- Include a "When the system doesn't cover it" section: stop, build the closest compliant version, flag with `ds-gap`.
- Keep a **Changelog** and a **Gaps backlog** so the system visibly grows (it's never finished).
