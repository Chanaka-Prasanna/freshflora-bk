from fastapi import APIRouter, Depends, HTTPException
from app.models.order import OrderCreate, OrderResponse, OrderInDB
from app.api.deps import get_current_user
from app.db.mongodb import db_client
from typing import List, Any
from bson import ObjectId

router = APIRouter()

@router.post("", response_model=OrderResponse)
async def create_order(
    order_in: OrderCreate,
    current_user: dict = Depends(get_current_user)
) -> Any:
    # In a real application, you would verify product prices and handle payment processing here.
    # We will just mark it as paid for this mock implementation.
    
    order_dict = order_in.model_dump()
    order_dict["status"] = "paid"
    
    order_data = OrderInDB(
        **order_dict,
        user_id=str(current_user["_id"])
    )
    
    result = await db_client.db["orders"].insert_one(order_data.model_dump(by_alias=True, exclude={"id"}))
    
    # Increment orders count for each product in the order
    for item in order_in.items:
        try:
            await db_client.db["products"].update_one(
                {"_id": ObjectId(item.product_id)},
                {"$inc": {"orders": item.quantity}}
            )
        except Exception as e:
            # If product not found or invalid ObjectId, ignore
            pass
    
    # Return the created order
    created_order = await db_client.db["orders"].find_one({"_id": result.inserted_id})
    created_order["id"] = str(created_order["_id"])
    return OrderResponse(**created_order)

@router.get("", response_model=List[OrderResponse])
async def get_orders(
    current_user: dict = Depends(get_current_user)
) -> Any:
    cursor = db_client.db["orders"].find({"user_id": str(current_user["_id"])})
    orders = await cursor.to_list(length=100)
    
    response = []
    for order in orders:
        order["id"] = str(order["_id"])
        response.append(OrderResponse(**order))
        
    return response
