---
section: ai
order: 1
title: Fieldnote
skill: Мультимодальный retrieval — ответ по картинке, таблице и схеме, а не только по тексту.
goal: На визуальных вопросах multimodal-пайплайн обыгрывает text-only baseline минимум в 2 раза.
metric: accuracy visual vs text-only
pilot: Ассистент по 5–20 техническим PDF. Ответ + вырезанный регион страницы, на котором он основан.
stack:
  - Python 3.12
  - Claude vision
  - pymupdf
  - chromadb / lancedb
projectDir: projects/fieldnote
dod:
  - Визуальный вопрос даёт правильный ответ и кроп региона страницы.
  - Есть таблица text-only vs multimodal по текстовым и визуальным вопросам.
---

Field service assistant, который отвечает по графику на странице 112, а не по подписи к нему.
