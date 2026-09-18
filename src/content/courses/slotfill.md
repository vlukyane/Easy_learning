---
section: ai
order: 5
title: Slotfill
skill: LoRA vs хороший промпт — решение на измерении, а не на вере.
goal: Таблица A vs B по точности, стоимости за 1000 документов и латентности на held-out test плюс письменный вывод.
metric: field-level accuracy · $ / 1k · latency
pilot: Экстрактор полей грузовых инвойсов. Few-shot Claude против маленькой модели + LoRA на 40k примерах.
stack:
  - Python 3.12
  - Claude API
  - peft / transformers
projectDir: projects/slotfill
dod:
  - Обе реализации работают на одном test-наборе.
  - Есть таблица по трём осям и вывод «что выбрать и почему».
---

LoRA-адаптер на 40k грузовых инвойсов, честно сравнённый с промптом, который он пытается заменить.
