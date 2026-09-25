"""JSONL-лог каждого вызова модели. Глава 02-setup.

Пишет строку на вызов: модель, шаг, превью вход/выход, токены, латентность,
стоимость, ok/ошибка. Этот лог — сырьё для метрик стоимости во всём курсе.
"""

from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

LOG_PATH = Path(__file__).resolve().parents[1] / "logs" / "calls.jsonl"


def log_call(
    *,
    model: str,
    step: str,
    input_preview: str,
    output_preview: str,
    input_tokens: int,
    output_tokens: int,
    latency_ms: float,
    cost_usd: float,
    ok: bool = True,
    error: str | None = None,
) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    row: dict[str, Any] = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "step": step,
        "input_preview": input_preview[:500],
        "output_preview": output_preview[:500],
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "latency_ms": latency_ms,
        "cost_usd": cost_usd,
        "ok": ok,
        "error": error,
    }
    with LOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def smoke() -> None:
    """Крошечный вызов Haiku. В главе 02 заменишь заглушку реальным anthropic SDK."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        from dotenv import load_dotenv

        load_dotenv()
    started = time.perf_counter()
    # Ученик: замени реальным anthropic.Anthropic().messages.create(...)
    output = "smoke stub — подключи Anthropic в главе 02"
    latency_ms = (time.perf_counter() - started) * 1000
    log_call(
        model=os.environ.get("FIELDNOTE_MODEL", "claude-haiku-4-5-20251001"),
        step="smoke",
        input_preview="ping",
        output_preview=output,
        input_tokens=0,
        output_tokens=0,
        latency_ms=latency_ms,
        cost_usd=0.0,
        ok=True,
    )
    print(output)
    print(f"logged → {LOG_PATH}")
