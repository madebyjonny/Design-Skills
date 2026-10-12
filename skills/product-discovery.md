---
name: product-discovery
description: Interpret product requests, investigate missing behaviour and domain logic, ask targeted questions when decisions materially affect the outcome, and capture confirmed product knowledge for future work. Use before implementation when a request is ambiguous or introduces new behaviour.
---

# Product Discovery

## Purpose

Turn an incomplete product request into a sufficiently understood problem that can be implemented responsibly.

Do not assume the user has a user story, specification, wireframe, design file, or acceptance criteria. Create only the intermediate artefacts that help resolve real uncertainty.

The objective is not to eliminate all ambiguity. It is to identify which decisions matter, resolve what can be inferred safely, and ask the user about decisions that genuinely need their input.

## 1. Understand the request

Start by identifying:

- The outcome the user wants to achieve.
- Who or what is affected.
- The existing product area involved.
- The expected change in behaviour.
- What would make the result useful or successful.

Treat these as working hypotheses, not established facts.

## 2. Investigate before asking

Inspect the available evidence before asking the user questions.

Depending on the task, this may include:

- Existing application behaviour and journeys.
- Related pages, components and interaction patterns.
- Domain models, API contracts and business rules.
- Existing product documentation and recorded decisions.
- Existing empty, loading, success and failure states.
- Tests that reveal established behaviour.

Reuse confirmed knowledge. Do not ask questions that can be answered reliably by inspecting the product.

Do not treat existing implementation as proof that the existing behaviour is correct. Distinguish established behaviour from an established product decision.

## 3. Find missing logic

Consider whether the request leaves important questions unanswered.

Examples:

- What happens if the requested entity already exists?
- Can an action be undone?
- What happens if a request fails halfway through?
- Who is allowed to perform this action?
- What happens when two people change the same resource?
- Is the action immediate or does it require confirmation?
- What happens when there is no data, partial data or stale data?
- What feedback does the user receive after acting?
- Can the user recover without losing their work?

Only investigate questions relevant to the requested feature. Do not turn every task into an exhaustive checklist.

## 4. Decide whether to infer, ask or defer

For each important uncertainty, choose one approach.

### Infer

Infer when existing evidence, established product conventions or a strong domain constraint support one answer.

Record a significant inference as an assumption when it could affect future behaviour.

### Ask

Ask the user when plausible answers would materially change the product, and available evidence cannot resolve the choice.

Prefer a small number of specific questions over a long requirements questionnaire.

For each question, briefly explain why the answer matters and offer concrete alternatives when useful. Do not present invented alternatives as the only possible choices.

Prioritise questions that affect:

- User goals or product semantics.
- Permissions, privacy or destructive actions.
- Data integrity and irreversible behaviour.
- Important journey structure.
- Significant scope, cost or architectural commitments.

When several questions are related, group them into one concise interaction. Ask no more than three questions at a time unless the user requests a deeper discovery session.

### Defer

Defer decisions that are low-risk, reversible and do not block meaningful progress.

Choose a sensible default consistent with the product, state the assumption when appropriate, and make it easy to change later.

Do not interrupt the user to ask about trivial implementation details.

## 5. Establish a working product brief

Before substantial implementation, be able to explain:

- Intended outcome.
- Relevant existing behaviour.
- Important domain rules.
- Primary user journey.
- Significant alternative and failure paths.
- Confirmed decisions.
- Assumptions and unresolved questions.
- What evidence would demonstrate success.

This can be a short internal summary. Do not require a formal document if the task is already clear.

If an important unresolved question blocks safe or meaningful implementation, ask before proceeding. Otherwise, continue with explicit assumptions.

## 6. Validate the proposed behaviour

Before implementing, mentally or explicitly walk through the journey from the user's perspective.

Ask:

- Does this solve the requested problem?
- Does each action have a clear consequence?
- Does the user understand the current state?
- Are important failure cases recoverable?
- Are permissions and data changes coherent?
- Does this conflict with existing product behaviour?
- Are we solving the actual problem or merely implementing the first obvious UI?

Revise the approach if it fails these checks.

## 7. Capture reusable learning

When a decision reveals a durable product rule, propose adding it to the project's shared product knowledge.

Record:

- The rule or decision.
- Why it exists.
- Its source: user-confirmed, documented, observed or inferred.
- Where it applies.
- Any known exceptions.
- Whether it is still unresolved.

Do not silently convert an assumption into an authoritative product rule. Do not overwrite an existing decision simply because a new implementation suggests a different approach.

If the project has no suitable knowledge store, propose a lightweight one rather than inventing an elaborate documentation system.

## 8. Report the outcome

Summarise only what is useful:

- What you understood.
- Important decisions and assumptions.
- Questions requiring the user's input.
- Significant behaviour that will be covered in implementation and validation.

Do not claim the product problem is fully understood when important uncertainties remain.

## Principles

- Investigate before interrogating.
- Ask about consequential ambiguity, not every ambiguity.
- Prefer evidence over convention, and convention over unsupported invention.
- Make uncertainty visible.
- Preserve user intent over implementation convenience.
- Treat discovery as an ongoing process; revise the brief when new evidence emerges.
