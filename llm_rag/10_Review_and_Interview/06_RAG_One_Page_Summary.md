# RAG One Page Summary

## What is RAG?

RAG = Retrieval-Augmented Generation.

## Why RAG?

- Fresh knowledge
- Private knowledge
- Lower hallucination risk
- Easier updates than fine-tuning

## Naive RAG

1. Indexing
2. Retrieval
3. Generation

## Common Failure Points

1. Missing content
2. Missed top-ranked documents
3. Not in context
4. Not extracted by LLM
5. Wrong format
6. Incorrect specificity
7. Incomplete answer

## Production-Level RAG

Production RAG is not just vector database + LLM.

You need to solve:

1. How to chunk documents well
2. How to retrieve accurately
3. How to assemble useful context
4. How to evaluate continuously
