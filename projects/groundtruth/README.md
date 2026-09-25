# Groundtruth — evals as a merge gate

Eval-харнесс для юридического ресёрча, который **валит PR при падении recall**.

Портал: http://localhost:4321/courses/groundtruth

API-ключ не нужен: проект про retrieval-метрики и гейт, не про генерацию.

## Стенд и локальный гейт (это и есть DoD)

```bash
cd projects/groundtruth
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest                              # метрики на фикстурах — зелёные из коробки
python scripts/ci_eval.py; echo exit:$?
```

`ci_eval.py` и `.github/workflows/eval.yml` уже рабочие. До реализации `evaluate`
гейт честно валится с `GATE_FAIL` — это ожидаемо.

## Что готово, а что пишешь ты

```
eval/metrics.py   recall@k/precision@k/mrr/validate_gold [готово] · evaluate/write_baseline [ты]
scripts/ci_eval.py  гейт: recall < baseline-EPSILON → exit 1          [готово]
.github/workflows/eval.yml  запуск гейта на PR                        [готово]
src/ingest.py     build() — корпус в стабильные doc_id             [пишешь ты]
src/retrieve.py   retrieve() — детерминированные doc_id            [пишешь ты]
src/constants.py  K, EPSILON, GATE_SPLIT                              [готово]
```

## Данные и форматы

Корпус юридических текстов → `data/corpus/`. Золото (`eval/gold.jsonl.example`):

```json
{"qid":"q1","query":"duty to warn in product liability","relevant_ids":["doc-001","doc-014"],"split":"dev"}
```

`relevant_ids` ссылаются на стабильные `doc_id` из ingest. `split`: `dev` (по нему
судит гейт) или `heldout` (держим для честной проверки, чтобы не подогнать под гейт).

```bash
cp eval/gold.jsonl.example eval/gold.jsonl
python -c "from eval.metrics import validate_gold; validate_gold('eval/gold.jsonl')"
```

## Ожидаемый вывод гейта

```
GATE_OK   recall=0.812 baseline=0.805 eps=0.01 split=dev     # PR зелёный
GATE_FAIL recall=0.760 baseline=0.805 eps=0.01 split=dev     # PR красный
```

Продемонстрируй гейт: сделай PR, ухудшающий retrieve, и покажи красный CI.

## DoD

PR, роняющий recall ниже `baseline - EPSILON`, автоматически краснеет; сохраняющий —
зелёный. Числа recall видны в выводе прогона.
