"""Схема извлекаемых полей инвойса. Общий контракт для систем A и B.

Обе системы (промпт и LoRA) обязаны возвращать один и тот же объект InvoiceFields —
иначе бенчмарк A vs B несравним.
"""

from pydantic import BaseModel, Field


class LineItem(BaseModel):
    """Строка инвойса."""

    description: str
    quantity: float
    unit_price: float
    amount: float


class InvoiceFields(BaseModel):
    """Извлечённые поля одного инвойса — единый выход A и B."""

    invoice_id: str
    carrier: str
    total: float
    invoice_date: str
    shipper_address: str
    consignee_address: str
    line_items: list[LineItem] = Field(default_factory=list)
