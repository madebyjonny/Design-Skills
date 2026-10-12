---
name: accessibility-validation
description: Evaluate implemented user interfaces for accessibility barriers using automated checks, semantic inspection, keyboard interaction, focus behaviour and assistive-technology testing where available. Use when building or changing user-facing interfaces.
---

# Accessibility Validation

## Purpose

Identify and help resolve barriers that could prevent people with disabilities from understanding, navigating or using the experience.

Accessibility is a requirement of product quality, not an optional visual polish step.

Use applicable WCAG 2.2 criteria as a reference, alongside platform-specific guidance and the product's actual interaction model.

Do not claim WCAG conformance or full accessibility based solely on an automated scan.

## 1. Inspect the rendered experience

When possible, run the actual application and inspect the changed journey.

Identify:

- Interactive controls and their accessible names.
- Headings, landmarks and content structure.
- Forms, instructions and validation messages.
- Dialogs, menus, popovers and custom controls.
- Dynamic updates and loading feedback.
- Keyboard focus and navigation order.
- Responsive layouts, zoom and text reflow.

Do not assume that semantic correctness in source code guarantees correct behaviour in the browser.

## 2. Evaluate the following dimensions

### A. Semantics and accessible names

- Do controls expose appropriate roles and names?
- Are buttons and links distinguishable by purpose?
- Are headings and landmarks meaningful?
- Are form controls associated with their labels and relevant instructions?
- Are custom widgets using appropriate platform semantics?
- Is important information available to assistive technology rather than only visually apparent?

Prefer native HTML controls over custom implementations when they meet the product's needs.

### B. Keyboard interaction

- Can all functionality be operated using a keyboard?
- Is the focus order logical?
- Is focus visible?
- Can users enter and leave dialogs, menus and other interactive regions?
- Are Escape, Enter, Space and arrow keys handled according to the control's interaction pattern?
- Are there keyboard traps?
- After an action, does focus remain in a sensible place?

Do not assume every control should support every key. Validate the expected interaction model for that control.

### C. Focus management

For dialogs, menus, route changes and other significant transitions, examine:

- Where focus begins.
- Whether focus remains within a modal interaction when appropriate.
- Where focus goes when the interaction closes.
- Whether navigation changes are communicated and focus remains useful.
- Whether newly displayed validation errors can be discovered and addressed.

Focus management should follow the user's task rather than a universal rule to move focus after every update.

### D. Forms and errors

- Are required fields identified clearly?
- Are constraints explained before or when they become relevant?
- Are errors specific and actionable?
- Can users identify which field has a problem?
- Are errors exposed programmatically as well as visually?
- Is valid input preserved when submission fails?
- Can users correct and resubmit without unnecessary repetition?

Do not communicate errors through colour alone.

### E. Contrast, typography and reflow

- Does text meet applicable contrast requirements?
- Are non-text controls and meaningful visual indicators sufficiently distinguishable?
- Does content remain usable when zoomed?
- Does text reflow appropriately at narrow viewport widths?
- Are text resizing and user spacing adjustments accommodated where applicable?
- Is meaning preserved when colour is unavailable?

Use actual rendered colours and applicable contrast calculations rather than visual guesses.

### F. Dynamic feedback

- Are important success and failure messages perceivable?
- Are asynchronous updates announced when appropriate?
- Do live regions avoid excessive or repetitive announcements?
- Is progress communicated for operations that take time?
- Are changes to status or availability conveyed without forcing users to discover them visually?

Do not make every UI update a live announcement. Announcements should help users understand meaningful changes without creating noise.

### G. Motion and sensory requirements

- Is essential information available without animation?
- Is unnecessary motion avoided?
- Are reduced-motion preferences respected where applicable?
- Do flashing or moving elements create avoidable barriers?
- Does meaning depend solely on sound, colour, spatial position or another single sensory channel?

### H. Touch and pointer interaction

- Are interactive targets sufficiently large or adequately spaced under the applicable requirements?
- Can controls be operated without unnecessarily precise movements?
- Are hover-only interactions available through other input methods?
- Are pointer cancellation and dragging interactions usable alternatives where required?

## 3. Validate with appropriate evidence

Use the strongest available method for each check:

1. Automated accessibility analysis for detectable semantic, naming, contrast and structural issues.
2. DOM and accessibility-tree inspection for roles, names, states and relationships.
3. Keyboard-only interaction for navigation, activation and focus behaviour.
4. Screen-reader testing where available, especially for complex widgets, forms and dynamic content.
5. Zoom, reflow and responsive inspection.
6. Manual review against applicable accessibility criteria.

When a method or environment is unavailable, record the check as not verified rather than assuming it passed.

## 4. Report findings

For each issue, record:

- The observed barrier.
- The affected component or journey.
- The applicable criterion or interaction principle, where known.
- The reproduction steps.
- The user impact.
- The recommended correction.
- Whether the issue was reproduced or inferred from inspection.

Use these statuses:

- **Pass:** The specific check was performed and passed.
- **Fail:** A barrier was observed.
- **Not verified:** The necessary check could not be performed.
- **Not applicable:** The criterion does not apply to this experience.

Do not report the entire experience as accessible merely because no issues were found by an automated tool.

## 5. Prevent recurring failures

When a barrier is repeated, correct it at the most appropriate layer:

- Fix shared component semantics or behaviour.
- Replace unnecessary custom controls with native elements.
- Improve component APIs so accessible usage is straightforward.
- Add automated checks or regression tests where feasible.
- Document complex interaction patterns with accessible examples.
- Update the relevant skill when the failure reveals a missing instruction.

Reproduce the original failure after making the correction.

## Principles

- Accessibility is part of the core experience.
- Test behaviour, not only markup.
- Do not overstate what automated tools establish.
- Prefer robust native semantics.
- Make unverified areas explicit.
- Fix recurring barriers at their source.
