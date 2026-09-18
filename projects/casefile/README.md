# Casefile — Multi-agent orchestration

Пилот: триаж синтетических insurance claims. Typed handoffs, cost ceiling, HITL на выплате.

Портал: http://localhost:4321/courses/casefile

```bash
cd projects/casefile
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
pytest
```

`test_no_payout_without_approval` уже красный/зелёный на инварианте: `execute_payout` без `approved=True` обязан падать. Не снимай эту проверку.

Стубы агентов и оркестратора — NotImplementedError до соответствующих глав.

## Числа в конце курса

Запиши в этот README: ¢/claim, доля ceiling-stop, route-match.
