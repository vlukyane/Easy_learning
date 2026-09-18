# Groundtruth — evals as a merge gate

Портал: http://localhost:4321/courses/groundtruth

Локальный гейт (если нет GitHub remote) — это и есть DoD:

```bash
cd projects/groundtruth
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
python scripts/ci_eval.py; echo exit:$?
```

Шаблон Action: `.github/workflows/eval.yml`.
