# Mermaid patterns

## Interaction across a timeout

Read from top to bottom. The timeout is an event observed by the caller; it leaves the server's completion status unknown.

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Service
    C->>S: Submit request with ID
    alt Reply arrives
        S-->>C: Result
    else Deadline passes
        C->>S: Query status by ID
        S-->>C: Current status
    end
```

## A boundary and a return path

The shaded group identifies who owns both steps. The labeled return edge shows which condition causes another attempt. On a renderer without edge IDs or motion, replace the two retry lines with `W -->|Retry after transient failure| Q`.

```mermaid
flowchart LR
    subgraph jobs["Job service"]
        Q["Pending queue"] -->|Deliver| W["Worker"]
        W retry@-->|Retry after transient failure| Q
        retry@{ animate: true }
    end
    W -->|Completed| R(["Result"])
    style jobs fill:#edf3fa,stroke:#48617d,color:#172b3a
    classDef outcome fill:#e6f3e8,stroke:#32623d,color:#16321d
    class R outcome
```

## Quantitative split

Illustrative counts only: 100 requests split into 70 completed and 30 deferred. Width encodes request count. Use observed values and the reporting period for a real system.

```mermaid
sankey-beta
Received,Completed,70
Received,Deferred,30
```

## Hierarchy without weights

Indentation means containment; reading order implies no execution order.

```mermaid
mindmap
  root(Service)
    Interface
      Submit
      Query
    Processing
      Queue
      Worker
```

Verify the syntax accepted by the destination version, particularly the Sankey declaration and animated edge attributes. [Sequence diagrams](https://mermaid.js.org/syntax/sequenceDiagram.html) · [Flowcharts](https://mermaid.js.org/syntax/flowchart.html) · [Sankey](https://mermaid.js.org/syntax/sankey.html) · [Mind maps](https://mermaid.js.org/syntax/mindmap.html)
