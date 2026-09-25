"""Константы гейта. Меняешь порог качества — меняешь здесь, в одном месте.

K          — отсечка для recall@k / precision@k.
EPSILON    — допустимая просадка: гейт валит PR при recall < baseline - EPSILON.
GATE_SPLIT — на каком сплите судит гейт (dev), heldout держим для честной проверки.
"""

K = 10
EPSILON = 0.01
GATE_SPLIT = "dev"
