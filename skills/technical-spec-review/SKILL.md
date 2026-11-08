---
name: technical-spec-review
description: Reverse-engineer current system behavior to answer the user's question and identify where the implementation matches or differs from the technical specification.
---

# Technical Specification Review

Identify the specific claim to check and the implementation path that would confirm or contradict it.

## Work within the evidence boundary

- If the user asks for a document-only explanation, use the supplied material. Cite the relevant section. When a step is unspecified, identify the missing detail and explain which conclusion it prevents.
- When implementation evidence is in scope, trace the claim through the actual entry point, caller, and relevant configuration. A helper shows a capability; its caller establishes when that capability is used. Attribute test results and runtime observations to the specific input and environment examined.
- Keep documented intent, observed behavior, inference, and unknowns distinguishable. A missing description leaves a question open. Report an omission or contradiction as a finding only when evidence supports it.

## Trace the mechanism that determines the answer

Follow the input from selection through processing and the decision that produces the result. Focus on branches that change the answer: what gets admitted, skipped, rejected, or returned as inconclusive? Cite the rule or code path for each consequential distinction. Explain unfamiliar terms at the step where they affect the outcome.

## Show what the evidence supports

When examples help, compare a normal input and a boundary or risky input that differ in one relevant condition. Walk each through the documented or observed decision. Label hypothetical examples and distinguish predicted outcomes from recorded results.

Prioritize gaps that affect correctness, security, or coverage. For each material gap, state what is known, why the missing step matters, and the specific evidence that would settle it, such as a caller, a configuration value, or a test with a particular input.
