from fastapi import APIRouter, Query
from app.models.product import ProductResponse, PaginatedProductsResponse
from app.db.mongodb import db_client
import math
from typing import Optional, Any

router = APIRouter()

async def get_products_common(
    page: int = 1,
    size: int = 10,
    search: Optional[str] = None,
    sort_by: Optional[str] = None,
    sort_order: str = "asc",
    category: Optional[str] = None,
    is_hot: Optional[bool] = None
):
    query = {}
    
    if search:
        query["$or"] = [
            {"name": {"$regex": search, "$options": "i"}},
            {"description": {"$regex": search, "$options": "i"}}
        ]
        
    if category:
        query["category"] = category
        
    if is_hot is not None:
        query["is_hot"] = is_hot

    sort_criteria = []
    if sort_by:
        order = 1 if sort_order == "asc" else -1
        sort_criteria.append((sort_by, order))
    else:
        sort_criteria.append(("_id", 1))

    skip = (page - 1) * size
    
    cursor = db_client.db["products"].find(query).sort(sort_criteria).skip(skip).limit(size)
    products_list = await cursor.to_list(length=size)
    total = await db_client.db["products"].count_documents(query)
    
    items = []
    for prod in products_list:
        prod["id"] = str(prod["_id"])
        items.append(ProductResponse(**prod))
        
    pages = math.ceil(total / size) if size > 0 else 0
    
    return PaginatedProductsResponse(
        items=items,
        total=total,
        page=page,
        size=size,
        pages=pages
    )

@router.get("", response_model=PaginatedProductsResponse)
async def get_products(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    search: Optional[str] = None,
    sort_by: Optional[str] = None,
    sort_order: str = Query("asc", pattern="^(asc|desc)$"),
    category: Optional[str] = None
) -> Any:
    return await get_products_common(page, size, search, sort_by, sort_order, category)

@router.get("/hot", response_model=PaginatedProductsResponse)
async def get_hot_products(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    search: Optional[str] = None,
    sort_by: Optional[str] = None,
    sort_order: str = Query("asc", pattern="^(asc|desc)$"),
    category: Optional[str] = None
) -> Any:
    return await get_products_common(page, size, search, sort_by, sort_order, category, is_hot=True)
