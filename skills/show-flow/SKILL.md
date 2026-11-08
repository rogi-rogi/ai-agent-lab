---
name: show-flow
description: Visualize flows and relationships in technical documentation. Choose the diagram and its visual encodings from the reader's question about interaction, hierarchy, quantities, decisions, or state.
---

# Show flow

Identify what the reader should be able to tell from the figure and what evidence establishes the relationship. Choose a representation from its semantics before choosing a layout.

## Choose the deliverable

Honor any requested format. By default, embed an editable Mermaid diagram in the document. For a dense topic, first consider an overview and a focused detail diagram. Choose an interactive, standalone HTML document when the reader needs to explore alternatives, change a condition, or inspect detail in context. For example, a sequence diagram can show one retry path; if the reader needs to switch between timeout and rejection and trace the affected steps, a scenario selector can make that comparison easier.

## Choose the visual form

| Reader's question | Starting point | Preserve |
| --- | --- | --- |
| Who sends what to whom, and when? | Sequence diagram | Participants, message order, replies, and alternative paths |
| What can this object become? | State diagram | States and transition conditions |
| What belongs inside what? | Mind map or nested groups | Parentage and containment. A treemap also encodes magnitude and needs values. |
| How much moves between categories? | Sankey | Sourced amounts in comparable units; if counts are unknown, use labeled relationships without weighted widths. |
| Where do cases branch, stop, or rejoin? | Flowchart | Decision conditions on edges, endpoints, and ownership boundaries |
| How do entities relate or activities overlap? | ER diagram for cardinality; Gantt for known durations | Verified multiplicities or time intervals |

Show the detail that actually answers the question: for a retry, include the triggering event, owner, and return path. Separate an overview from a detail diagram if together they mix levels or obscure labels.

**Give styling a job.** Use a labeled subgraph and background tint for ownership or trust boundaries, and node shape or class for role or outcome. Encode the same distinction in text or shape so color is optional. Label what arrows carry. Use an identified, animated edge to trace a retry or recurring transfer only if motion helps and the renderer supports it. Make the edge comprehensible in a static export. For concrete patterns, see [Mermaid examples](references/patterns.md).

Give the reader a short reading cue and state what the visualization establishes.

**For Mermaid**, return an editable block. Check target renderer support, parse syntax and render where available. Inspect label fit, crossings, contrast and the meaning of grouping and widths. Report separately what was parsed, rendered, and checked in the destination. When a feature is unsupported, use the documented static equivalent.

**For interactive HTML**, deliver a single local `.html` file that opens directly in a browser. Embed the required styles, data and scripts; avoid network dependencies or a server. Start with a readable overview. Choose controls tied to the reader's question, such as selecting a branch to highlight its path or expanding a component to inspect its dependencies. Label controls, support keyboard use, and keep the selected state visible. Open the file locally and exercise the relevant controls, checking that the diagram and details agree in each state. Report any checks you could not perform.

[Mermaid diagram syntax](https://mermaid.js.org/intro/syntax-reference.html)
