from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from app.models.user import PyObjectId

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float

class OrderBase(BaseModel):
    total_amount: float
    items: List[OrderItem]
    status: str = "pending" # pending, paid, shipped, delivered, cancelled

class OrderCreate(OrderBase):
    pass

class OrderInDB(OrderBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    user_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
    }

class OrderResponse(OrderBase):
    id: str
    user_id: str
    created_at: datetime
