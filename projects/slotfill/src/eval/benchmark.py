"""Бенчмарк A vs B. Главы 05–06.

Один harness (src.harness), тот же test-набор и тот же parse для обеих систем.
Три оси сравнения: качество (field-level + exact-doc), стоимость за 1000 док, латентность.
"""


def main() -> None:
    """Прогнать A и B на одних test id одним парсером; посчитать три оси. Глава 05."""
    raise NotImplementedError("глава 05: те же test id, тот же parser, A и B")


def write_table() -> None:
    """Заполнить results/table.md тремя осями из прогона main(). Глава 06."""
    raise NotImplementedError("глава 06: заполни results/table.md по трём осям")
