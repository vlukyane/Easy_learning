---
section: ai
order: 3
title: Warmstart
skill: Трёхслойный LLM-кэш, где доля ложных попаданий измерена, а не предположена.
goal: Кривая hit-rate / false-hit vs порог, выбранная рабочая точка с числом и оценка экономии на 400k запросов в месяц.
metric: hit-rate / false-hit rate · $ / 400k
pilot: Кэш-прослойка перед ботом поддержки — exact, normalized, semantic.
stack:
  - Python 3.12
  - embeddings
  - SQLite / JSONL логи
projectDir: projects/warmstart
dod:
  - Работают все три слоя, метрики по каждому.
  - Есть кривая порогов и обоснованная рабочая точка с числовым false-hit rate.
  - Есть оценка экономии в деньгах.
---

Трёхслойный кэш над 400k вопросов поддержки в месяц, где доля ложных попаданий измерена, а не предположена.
