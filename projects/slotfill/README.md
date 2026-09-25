# Slotfill — LoRA vs prompt

Извлечение полей из грузовых инвойсов. LoRA-адаптер, **честно** сравнённый с
промптом, который он пытается заменить.

Портал: http://localhost:4321/courses/slotfill

## Стенд

```bash
cd projects/slotfill
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"          # для A (промпт) и бенчмарка
pip install -e ".[train]"        # extras для B (torch/transformers/peft) — только для LoRA
cp .env.example .env             # впиши ANTHROPIC_API_KEY
pytest                           # test_split зелёный из коробки
```

`pytest` проверяет `assert_disjoint` (нет утечки test в train) — а не твои модели.

## Что готово, а что пишешь ты

```
src/schema.py            InvoiceFields — единый выход A и B                 [готово]
src/data/split.py        assert_disjoint / load_splits [готово] · main [ты]
src/harness.py           field_level_accuracy / exact_doc_match [готово] · run_test [ты]
src/data/generate.py     синтетика инвойсов                             [пишешь ты]
src/prompt_extract.py    система A: few-shot → InvoiceFields             [пишешь ты]
src/baselines/prompt.py  прогон A по срезу                              [пишешь ты]
src/baselines/lora.py    прогон B (LoRA)                                [пишешь ты]
src/train.py             обучение LoRA (train only, early-stop val)     [пишешь ты]
src/eval/benchmark.py    A vs B на одном test/parser                    [пишешь ты]
```

Правила скоринга живут **только** в `harness.py` — не копируй их в `train.py`.

## Три оси сравнения (`results/table.md`)

| system   | field-level | exact-doc | USD/1000 | p50 ms | p95 ms |
|----------|-------------|-----------|----------|--------|--------|
| A prompt | 0.94        | 0.71      | 5.20     | 900    | 1600   |
| B LoRA   | 0.96        | 0.78      | 0.40     | 120    | 260    |

(числа — иллюстрация формы вывода; свои впишешь в главе 06)

Для B укажи стоимость честно: только инференс vs инференс + амортизированное обучение.

## Правильный результат

Любой из исходов, если он **измерен** на held-out test: B лучше, A лучше, или
«зависит от объёма». Провал — только если сравнение нечестное (нет baseline-промпта,
утечка test, разный parser/метрика).

## DoD

Таблица A vs B по трём осям на одном test-наборе + `results/verdict.md` с выводом «что выбрать и почему».
