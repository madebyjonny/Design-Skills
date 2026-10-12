# Design Skills

Four complementary skills for understanding product requests and evaluating user-facing work from discovery through validation.

## Skills

### [Product Discovery](skills/product-discovery/SKILL.md)

Use before implementation when a request is ambiguous or introduces new behaviour. This skill helps investigate existing product evidence, identify consequential gaps in domain logic, decide when to infer, ask or defer, and capture confirmed product knowledge without turning every request into a lengthy requirements exercise.

### [Experience Validation](skills/experience-validation/SKILL.md)

Use after implementing or changing a user-facing interaction. This skill validates the smallest meaningful set of realistic journeys, including relevant success, failure and recovery paths, by exercising the rendered product and verifying outcomes rather than merely checking that UI elements exist.

### [Design Quality Review](skills/design-quality-review/SKILL.md)

Use after building or changing a user-facing experience, whether or not a reference design exists. This skill evaluates purpose, visual hierarchy, consistency, interaction quality, information density, responsive behaviour and fit and finish using observable evidence and product context.

### [Accessibility Validation](skills/accessibility-validation/SKILL.md)

Use when building or changing user-facing interfaces. This skill checks rendered experiences for barriers across semantics, keyboard interaction, focus management, forms, contrast and reflow, dynamic feedback, motion, and touch or pointer use, applying WCAG 2.2 and platform guidance where relevant.

## Shared Approach

Across the skills:

- Inspect the actual product and rendered experience whenever possible.
- Prefer evidence and observed behavior over assumptions or source inspection alone.
- Test scenarios proportionately, focusing on the journeys and risks relevant to the change.
- Distinguish verified findings from hypotheses, assumptions and checks that could not be performed.
- Describe issues precisely, connect them to user impact and recommend actionable corrections.
- Fix recurring problems at the appropriate shared layer and verify the result.

These skills are complementary rather than sequential requirements for every task. Product discovery resolves meaningful uncertainty before implementation; experience validation verifies changed journeys; design quality review assesses usability and craft; and accessibility validation examines barriers for people with disabilities.
