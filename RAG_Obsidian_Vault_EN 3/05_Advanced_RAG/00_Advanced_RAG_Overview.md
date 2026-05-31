---
tags:
  - llm
  - rag
---

# Advanced RAG Overview

Advanced RAG is not one single technique. It is a set of engineering optimizations around common RAG failure points.

```mermaid
flowchart TD
A[Pre-Retrieval] --> B[Retrieval]
B --> C[Post-Retrieval]
```

## Key Idea

Improve query quality, retrieval quality, and context quality before generation.
