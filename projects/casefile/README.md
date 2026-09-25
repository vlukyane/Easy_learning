# Casefile — Multi-agent orchestration

Пилот: триаж синтетических insurance claims. Typed handoffs, cost ceiling, HITL на выплате.

Портал: http://localhost:4321/courses/casefile

## Стенд

```bash
cd projects/casefile
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env   # впиши ANTHROPIC_API_KEY
pytest                 # зелёный из коробки
cp data/claims.jsonl.example data/claims.jsonl
```

`pytest` проверяет реализованный фундамент, а не твоих агентов:
`test_handoff_schema` — что кривой Handoff не проходит; `test_no_payout_without_approval` —
инвариант «`execute_payout` без `approved=True` кидает PermissionError». Не снимай его.

## Что готово, а что пишешь ты

```
src/contracts.py    Handoff + ClaimIntake/IntakeResult/.../PayoutDecision   [готово]
src/cost.py         CostClock: учёт токенов, would_exceed                   [готово]
src/payout.py       execute_payout — единственная дверь к выплате           [готово]
src/hitl.py         request_approval → PayoutDecision                    [пишешь ты]
src/agents/*.py     intake / classifier / fraud / assessor (LLM)         [пишешь ты]
src/orchestrator.py run_claim / run_batch: FSM + cost + hitl             [пишешь ты]
```

Правило: агенты обмениваются **payload из моделей contracts.py**, не текстом;
выплата — **только** через `payout.execute_payout`.

## Данные

`data/claims.jsonl.example` — строки с `expected_route` и `is_fraud` (это и есть
ground truth для проверки маршрутизации):

```json
{"claim_id":"CLM-002","narrative":"Total loss, claimed 25000, third similar claim this month.","claimed_amount":25000.0,"incident_date":"2026-02-01","expected_route":["intake","classify","fraud_check","human_review"],"is_fraud":true,"notes":"high-fraud"}
```

## Ожидаемая трасса `run_claim('CLM-002')`

```
intake → classify(type=auto, prio=high) → fraud(risk=high, send_to_human=True)
→ human_review: одобрить $25000? [y/N]   (без 'y' выплаты нет)
cost: $0.0031 / ceiling $0.15
```

## Числа в конце курса

Запиши сюда: ¢/claim, доля ceiling-stop, route-match (vs expected_route), 0 выплат без approval.
