# Fieldnote — Multimodal RAG

Пилот курса: ассистент по техническим PDF. Ответ + кроп региона страницы.

Портал: http://localhost:4321/courses/fieldnote

## Стенд

```bash
cd projects/fieldnote
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

Главы портала указывают, какие стубы наполнять. `pytest` на форме отчёта можно гонять без API.

## DoD

Таблица text-only vs multimodal по `text`/`visual`. Visual-ratio ≥ 2 или честный разбор, почему нет.
