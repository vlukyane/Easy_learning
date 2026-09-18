from pydantic import BaseModel, Field


class LineItem(BaseModel):
    description: str
    quantity: float
    unit_price: float
    amount: float


class InvoiceFields(BaseModel):
    invoice_id: str
    carrier: str
    total: float
    invoice_date: str
    shipper_address: str
    consignee_address: str
    line_items: list[LineItem] = Field(default_factory=list)
