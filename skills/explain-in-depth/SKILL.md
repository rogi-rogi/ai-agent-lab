---
name: explain-in-depth
description: Supply the missing background or mechanism when a user asks how or why, follows up on an earlier answer, or finds a passage unclear. Use direct examples from the subject itself.
---

# Explain in depth

Read the question alongside the earlier explanation. Identify what that explanation assumed the reader knew: an undefined term, a change of representation, a skipped operation, or a condition that connects the stated cause to its result. Use the user's wording as a clue. Supply the missing piece yourself when the context is sufficient. Ask a focused question only if plausible interpretations would require materially different explanations.

Answer the specific point, introducing any prerequisite at the step that needs it. Use the subject's own objects, values, and operations. Avoid analogies and cross-domain examples. When a transformation is unclear, show a small input, the operation, the resulting representation, and how to interpret it. If a condition matters, vary that condition and explain the change in outcome. Include only the steps needed to resolve the question.

Choose an example from the user's current topic. For a question about why two SQL counts differ, show the column values: with scores of 80, NULL, and 90, COUNT(*) counts all three rows. COUNT(score) counts only the two rows with a recorded score. Replacing NULL with 0 makes both counts three, because zero is a recorded value. This isolates the condition that changes the result.

Draw on reliable subject knowledge or primary sources within the user's evidence constraints. Distinguish a general mechanism from a particular product's implementation. If the permitted material omits a necessary step, say exactly what cannot be established. For a question about whether the product actually implements a documented claim, trace the implementation using the technical specification review workflow.

Teaching reference: the [IES practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/1) discusses worked examples, concrete representations, and explanatory questions.
