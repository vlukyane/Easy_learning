# Warmstart — LLM cache

Портал: http://localhost:4321/courses/warmstart

Формула false-hit (не меняй молча): `false_hits / semantic_hits`.

```bash
cd projects/warmstart
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```
