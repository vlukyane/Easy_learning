# Warmstart — LLM cache

Трёхслойный кэш над вопросами поддержки с **измеренной** долей ложных попаданий.

Портал: http://localhost:4321/courses/warmstart

Формула false-hit (не меняй молча): `false_hits / semantic_hits`.

## Стенд

```bash
cd projects/warmstart
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env   # впиши ANTHROPIC_API_KEY
pytest                 # test_false_hit зелёный из коробки
```

`pytest` проверяет реализованный `false_hit_rate` на фикстуре, а не твои эмбеддинги.

## Что готово, а что пишешь ты

```
src/cache/exact.py       точный кэш + TTL                         [готово]
src/cache/normalize.py   нормализованный ключ                     [готово]
src/metrics.py           false_hit_rate [готово] · eval_layers/monthly_savings [ты]
src/cache/semantic.py    lookup / dump_scores (эмбеддинги)      [пишешь ты]
src/data/generate.py     синтетика intents.jsonl                [пишешь ты]
src/eval_curve.py        кривая порогов → logs/curve.json       [пишешь ты]
```

## Данные и форматы

`data/intents.jsonl` — ground truth (какие фразы к какому интенту):

```json
{"intent_id":"mfa-reset","canonical_answer":"MFA reset requires a verified device.","phrases":["reset my authenticator","how do I reset MFA"]}
```

Заложи конфликтные почти-дубликаты (password-reset vs mfa-reset) — иначе false-hit
искусственно нулевой.

`logs/semantic-scores.jsonl` (из `semantic.dump_scores`) — вход для метрик и кривой:

```json
{"score":0.94,"query_intent":"password-reset","neighbor_intent":"mfa-reset"}
```

## Ожидаемый вывод кривой (`eval_curve.main`)

```
threshold  hit_rate  false_hit
0.82       0.41      0.031
0.86       0.33      0.009   ← рабочая точка
0.90       0.24      0.002
```

Рабочая точка выбирается по кривой, а не назначается заранее.

## Числа в конце курса

Запиши сюда: выбранный порог, hit-rate и false-hit в нём, $ экономии при 400k/мес.
