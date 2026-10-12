---
name: experience-validation
description: Validate a changed product experience by exercising realistic user journeys, checking relevant states, inspecting the rendered interface and verifying expected outcomes. Use after implementing user-facing functionality or changing an existing interaction.
---

# Experience Validation

## Purpose

Establish whether the implemented experience behaves as intended and provides adequate feedback and recovery.

Validate the actual product wherever possible. Code inspection and successful compilation are supporting evidence, not substitutes for exercising the experience.

## 1. Establish what success means

Use the best available evidence, in this order where applicable:

- Explicit decisions and requirements confirmed by the user.
- Established product rules and documented behaviour.
- The request's intended outcome.
- Relevant existing interaction patterns.
- Clearly labelled assumptions.

Do not invent requirements merely to make the task appear fully specified.

If the intended behaviour is materially ambiguous, invoke product discovery or ask the user before making a consequential assumption.

## 2. Build a small journey checklist

Identify the smallest set of scenarios that meaningfully tests the change.

Consider:

- The primary successful journey.
- Empty or first-use states.
- Invalid input.
- Loading and delayed responses.
- Network or server failure.
- Permission restrictions.
- Duplicate or conflicting actions.
- Cancellation and recovery.
- Relevant responsive layouts.
- Existing behaviour that might regress.

Only include scenarios relevant to the feature. Do not run every possible test for every change.

## 3. Exercise the actual interface

Where browser or application automation is available:

1. Launch the application.
2. Navigate to the feature as a user would.
3. Perform the intended interaction.
4. Observe the resulting interface and application state.
5. Exercise relevant failure and recovery paths.
6. Check that visible feedback matches the underlying result.
7. Inspect the changed layout at relevant viewport sizes.
8. Check keyboard behaviour and accessible feedback for relevant interactions.

Prefer interacting with the rendered application over calling internal functions that bypass the user experience.

## 4. Check the outcome, not just the action

For each scenario, verify:

- The intended action was possible.
- The expected result actually occurred.
- The interface communicated the result.
- The user can understand what to do next.
- Failures are handled without avoidable data loss.
- Repeated actions do not produce unintended results.
- The interface remains coherent after the state changes.

For example, a successful invitation test should verify more than the existence of a submit button. It should establish that the invitation was created and that the interface communicates the resulting state.

## 5. Evaluate quality alongside functionality

For the changed journey, ask:

- Is the next action apparent?
- Is the current state understandable?
- Is the feedback timely and useful?
- Are errors actionable?
- Can the user recover?
- Does the interface remain visually coherent?
- Can the journey be completed with the supported input methods?
- Are important accessibility checks verified?

Invoke the design-quality and accessibility skills for a more thorough review when appropriate.

## 6. Handle failures properly

If a check fails:

1. Capture the reproduction steps and evidence.
2. Determine whether the cause is product logic, UI behaviour, shared component behaviour, accessibility, styling or test setup.
3. Fix the underlying issue rather than hiding the symptom.
4. Repeat the failing scenario.
5. Run relevant regression checks.

If a check cannot be performed because of missing credentials, unavailable environments or unsupported automation, report the limitation explicitly.

## 7. Report the evidence

For each important scenario, record:

- **Scenario:** What was tested?
- **Expected:** What should have happened?
- **Observed:** What actually happened?
- **Evidence:** What supports the conclusion?
- **Status:** Pass, fail or not verified.

Separate implementation checks, automated journey checks, accessibility checks and subjective design judgements.

Do not claim usability has been proven without suitable user evidence.

## Principles

- Verify outcomes, not the presence of UI elements.
- Test the smallest meaningful set of user journeys.
- Include failure and recovery where relevant.
- Distinguish implementation confidence from experience confidence.
- Report limitations honestly.
- Make the next improvement actionable.
