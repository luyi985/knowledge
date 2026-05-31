# Failure Diagnosis Table

| Symptom | Likely Failure Point | Fix |
|---|---|---|
| No useful answer | FP1 Missing Content | Add or update source documents |
| Right document not found | FP2 Missed Top Ranked Documents | Improve retrieval or rerank |
| Context too long | FP3 Not In Context | Compress or filter context |
| Answer ignores evidence | FP4 Not Extracted By LLM | Improve prompt and extraction constraints |
| Output format wrong | FP5 Wrong Format | Add schema validation |
| Too broad or too narrow | FP6 Incorrect Specificity | Clarify answer granularity |
| Missing part of answer | FP7 Incomplete Answer | Improve context recall |
