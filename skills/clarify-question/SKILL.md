---
name: clarify-question
description: Clarify a user's intent when their request and the preceding conversation leave plausible interpretations that would lead to different answers or actions.
---

# Clarify the question

Read the user's words, the referenced material, and the preceding conversation. Identify what they want to understand, decide, or change. If the plausible interpretations lead to the same answer or next step, proceed. If they would lead to materially different answers or actions, ask one focused question in the user's terms and wait before doing the work that depends on it.

| Signal | Clarification strategy | Example |
| --- | --- | --- |
| A reference could point to two different things | Name the specific alternatives left open by the conversation | “By ‘the result’, do you mean this file's verdict or the final import decision?” |
| The desired outcome is unclear | Ask which deliverable would resolve the issue | “Do you want an explanation of why this happened, or a change to prevent it recurring?” Allow a different answer. |
| The goal is clear but the starting point would change the lesson | Use a prior-knowledge probe about a relevant prerequisite | “Which step already makes sense to you: saving an object as bytes, or rebuilding it from those bytes?” Start at the first missing link. Skip this if their example already shows what they know. |
| A prediction suggests two competing mental models | Use a low-stakes concept question that distinguishes the models | “If the file were renamed without changing its bytes, would you expect the result to change? What led you to expect that?” Use the reasoning to locate the confusion. Address an explicit factual error directly when no diagnosis is needed. |
| An educator requests material for unspecified readers | Work backward from the performance the document should enable | “After reading, should the team recognize a risky input, trace an inspection, or operate the tool?” Ask about audience or allowed evidence only if it changes that deliverable. |

Use what the user has already established. In teaching contexts, use a prior-knowledge or concept question only when it changes the explanation. Once the material ambiguity is resolved, answer or proceed within the clarified scope.

Method references: [CMU Eberly Center on prior knowledge](https://www.cmu.edu/teaching/assessment/priorknowledge/) and [concept tests](https://www.cmu.edu/teaching/assessment/assesslearning/concepTests.html).
