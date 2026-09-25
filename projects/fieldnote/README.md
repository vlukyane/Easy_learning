# Fieldnote — Multimodal RAG

Пилот курса: ассистент по техническим PDF. Ответ + кроп региона страницы.

Портал: http://localhost:4321/courses/fieldnote

## Стенд

```bash
cd projects/fieldnote
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env   # впиши ANTHROPIC_API_KEY
```

Проверка без API (должно работать сразу):

```bash
pytest                 # тест формы отчёта: text и visual раздельно
python -c "from src.eval import validate_gold; validate_gold('data/gold.jsonl.example')"
```

`pytest` зелёный из коробки — он проверяет `require_split_metrics`, а не твой
пайплайн. Стубы кидают `NotImplementedError("глава NN: ...")` — сообщение
указывает главу портала.

## Данные

5–20 технических PDF с картинками/таблицами/схемами (открытые user/service
manual). Клади в `data/pdfs/`, URL и лицензии записывай в `data/SOURCES.md`.
Половина вопросов золота обязана отвечаться только по картинке/таблице.

Золото — формат строки (`data/gold.jsonl.example`):

```json
{"id":"q002","question":"...","kind":"visual","pdf":"example-manual.pdf","page":12,"answer":"X2-3","notes":"answer lives in the diagram"}
```

`kind ∈ {text, visual}`; `pdf`+`page` — где живёт ответ (нужно для цитаты-кропа).

```bash
cp data/gold.jsonl.example data/gold.jsonl
python -c "from src.eval import validate_gold; validate_gold('data/gold.jsonl')"
```

## Структура

```
src/
  ingest.py    Page + render_pages / ingest_pdf                 [пишешь ты]
  index.py     build_text_index / build_image_index            [пишешь ты]
  retrieve.py  retrieve_text / retrieve_hybrid (RRF)            [пишешь ты]
  generate.py  answer_text_only / answer_multimodal / demo      [пишешь ты]
  eval.py      validate_gold, require_split_metrics [готово] · run_all [пишешь ты]
  log.py       log_call, smoke                                   [готово]
data/pdfs/     сюда PDF        data/pages/  сюда рендер PNG
logs/          calls.jsonl, eval-report.json, citations/*.png
```

## Ожидаемый вывод `run_all`

```json
{"text":   {"text_only": 0.80, "multimodal": 0.82},
 "visual": {"text_only": 0.20, "multimodal": 0.70},
 "visual_ratio": 3.5}
```

`visual_ratio ~ 1` → в генерацию не уходит кроп, либо image-индекс хранит подпись
(caption-ловушка).

## DoD

Таблица text-only vs multimodal по `text`/`visual`. Visual-ratio ≥ 2 или честный
разбор с планом, почему нет.
