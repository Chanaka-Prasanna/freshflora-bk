from pydantic import BaseModel, Field
from typing import Optional, List
from app.models.user import PyObjectId

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    image_url: str
    category: str
    is_hot: bool = False
    stock: int = 10
    orders: int = 0
    availability: str = "In Stock"

class ProductCreate(ProductBase):
    pass

class ProductInDB(ProductBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
    }

class ProductResponse(ProductBase):
    id: str

class PaginatedProductsResponse(BaseModel):
    items: List[ProductResponse]
    total: int
    page: int
    size: int
    pages: int
