# Slotfill — LoRA vs prompt

Портал: http://localhost:4321/courses/slotfill

```bash
cd projects/slotfill
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
# GPU / local train extras: pip install -e ".[train]"
pytest
```

Test split must never overlap train. `results/table.md` and `results/verdict.md` — артефакты закрытия курса.
