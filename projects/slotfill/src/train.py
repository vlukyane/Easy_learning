"""Обучение LoRA. Глава 04. Требует extras: pip install -e ".[train]".

Обучай ТОЛЬКО на train-срезе, early-stop по val. test не показывай модели никогда.
Правила скоринга сюда не копируй — они живут в harness.py (единый источник).
"""


def main() -> None:
    """Обучить LoRA-адаптер на train, early-stop на val. Глава 04."""
    raise NotImplementedError("глава 04: обучи LoRA только на train; early-stop по val")
