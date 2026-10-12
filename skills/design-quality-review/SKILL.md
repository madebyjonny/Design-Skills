---
name: design-quality-review
description: Critically evaluate implemented interfaces for visual hierarchy, clarity, consistency, interaction design, responsive behaviour and overall design craft. Use after building or changing a user-facing experience, even when no reference design exists.
---

# Design Quality Review

## Purpose

Determine whether the implemented experience is coherent, understandable, appropriate to the product and well executed.

A passing build, working tests or absence of runtime errors does not establish design quality.

A reference design is useful when available, but is not required. Evaluate the interface against user intent, product context, established design language and the quality criteria below.

## 1. Establish the basis for evaluation

Before reviewing, inspect what is available:

- The user's request and intended outcome.
- Existing application pages and established visual patterns.
- Design tokens, components and documented design principles.
- The actual rendered interface.
- Relevant interaction states and responsive layouts.

If no design system exists, infer a provisional set of conventions from the product and assess whether those conventions form a coherent experience.

Do not invent a brand identity or impose personal aesthetic preferences without evidence.

## 2. Review core quality dimensions

### A. Purpose and clarity

- Is the purpose of the page or component apparent?
- Is the primary action easy to identify?
- Are labels and instructions understandable in context?
- Does the interface expose the information needed to make a decision?
- Is unnecessary complexity obscuring the user's goal?
- Does the interface use language that reflects the product's actual domain?

A user should not need to understand the implementation to understand the interface.

### B. Visual hierarchy

- Does visual emphasis reflect the relative importance of content and actions?
- Can users distinguish primary, secondary and destructive actions?
- Are spacing, grouping, alignment and typography helping people understand relationships?
- Is important information prominent enough for its context?
- Are there competing visual elements that make the next step unclear?

Do not equate visual hierarchy with making the primary button brighter or larger. Hierarchy should reflect meaning.

### C. Consistency and coherence

- Are related components and actions presented consistently?
- Does the experience fit the established product language?
- Are spacing, typography, colour, borders, icons and interaction states coherent?
- Are existing components reused appropriately?
- Does a deviation from an established pattern have a clear reason?

Consistency is not an absolute rule. A pattern should change when the context or user need justifies the change.

### D. Interaction quality

- Is it clear which elements are interactive?
- Do controls behave as users would reasonably expect?
- Is feedback provided after important actions?
- Are loading, empty, error, success and disabled states appropriate?
- Can users recover from mistakes?
- Are destructive or consequential actions handled proportionately?
- Does the interaction avoid unnecessary steps or surprising changes?

Review the actual interaction, not only its appearance in a screenshot.

### E. Information density and cognitive load

- Is the amount of information appropriate to the task?
- Are related details grouped logically?
- Are optional or advanced details obscuring the primary path?
- Does the interface make users remember information that could reasonably remain visible?
- Are repeated explanations, decorative elements or unnecessary controls adding noise?

Do not automatically minimise content. Dense interfaces can be appropriate for expert workflows when the information is organised well.

### F. Responsive behaviour

- Does the interface remain usable at relevant viewport sizes?
- Does content reflow without clipping or unintended horizontal scrolling?
- Do navigation, forms, dialogs and tables remain workable?
- Are touch targets and spacing appropriate for the interaction method?
- Does the information hierarchy survive the change in layout?

Do not assume that a desktop layout scaled down is a suitable mobile experience.

### G. Fit and finish

- Is spacing intentional rather than arbitrary?
- Are icons, typography and component proportions visually coherent?
- Are there awkward line breaks, misaligned elements, overflow or inconsistent states?
- Are transitions and animations useful, restrained and consistent?
- Are empty or incomplete regions intentional rather than evidence of unfinished work?

Avoid subjective findings that cannot be connected to a user impact or a meaningful product principle.

## 3. Examine the experience in context

Where tools are available:

1. Launch the actual application.
2. Navigate to the changed experience as a user would.
3. Inspect the initial state and important interactive states.
4. Exercise the primary action and at least one relevant alternative or failure path.
5. Inspect screenshots at relevant viewport sizes.
6. Compare with established product patterns and design references when available.
7. Verify that visual and interaction feedback matches the underlying application state.

If you cannot run the application, clearly distinguish code inspection from rendered-interface validation.

## 4. Identify problems precisely

For every finding, describe:

- **Observation:** What is actually wrong?
- **Evidence:** Where was it observed, and under what conditions?
- **Impact:** How could it affect comprehension, task completion, trust or accessibility?
- **Recommendation:** What change would address the problem?
- **Confidence:** Is this an observed defect or a design hypothesis?

Prefer:

"The destructive Remove action has the same visual prominence as Save, and the interface provides no indication of its consequences. Users may mistake the two actions as equivalent."

Avoid:

"The buttons look bad."

## 5. Prioritise findings

Use these categories as a practical guide:

- **Critical:** Prevents an important task or creates a serious risk.
- **High:** Materially impairs comprehension, task completion or recovery.
- **Medium:** Creates noticeable friction, inconsistency or avoidable confusion.
- **Low:** A minor craft issue with limited user impact.

Severity should reflect impact and likelihood, not how visually irritating the issue is to the reviewer.

Do not inflate severity to make the review appear thorough.

## 6. Make a judgement

Report findings as:

- **Pass:** The reviewed criterion was checked and adequate evidence supports the conclusion.
- **Fail:** A concrete problem was observed.
- **Needs evidence:** The available evidence cannot establish whether the experience meets the criterion.
- **Not applicable:** The criterion genuinely does not apply.

A review is not a declaration that a design is objectively good. It is an evidence-based assessment of defined quality dimensions.

## 7. Improve the system when patterns recur

When the same issue appears repeatedly, investigate its cause.

Possible corrections include:

- Improving an existing component.
- Adding a missing reusable interaction pattern.
- Clarifying design tokens or principles.
- Adding examples and counterexamples to design knowledge.
- Updating a generation instruction or skill.
- Adding an automated regression check when the problem is objectively testable.

Do not add a new rule for every isolated visual preference.

## Principles

- Evaluate the user experience, not just the code.
- Prefer observable problems over aesthetic assertions.
- Use product context to interpret quality.
- Do not require a reference design to perform a meaningful review.
- Distinguish defects from subjective preferences and unvalidated hypotheses.
- Treat quality criteria as guides for judgement, not a recipe that guarantees good design.
