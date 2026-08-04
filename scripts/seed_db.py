import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import sys
import os

# Add the parent directory to sys.path so we can import from app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import settings

async def seed():
    client = AsyncIOMotorClient(settings.mongodb_url)
    db = client[settings.database_name]
    
    print("Clearing existing products...")
    await db["products"].delete_many({})
    
    sample_products = [
        {
            "name": "Red Roses Bouquet",
            "description": "A classic bouquet of red roses for your loved one.",
            "price": 29.99,
            "image_url": "https://images.unsplash.com/photo-1563241527-3004b7be023b?q=80&w=600&auto=format&fit=crop",
            "category": "Roses",
            "is_hot": True,
            "stock": 50
        },
        {
            "name": "Sunflower Sunshine",
            "description": "Brighten up the day with these fresh sunflowers.",
            "price": 24.99,
            "image_url": "https://images.unsplash.com/photo-1597848212624-a19eb35e2651?q=80&w=600&auto=format&fit=crop",
            "category": "Sunflowers",
            "is_hot": True,
            "stock": 30
        },
        {
            "name": "Elegant Orchids",
            "description": "Beautiful orchids perfect for any occasion.",
            "price": 45.00,
            "image_url": "https://images.unsplash.com/photo-1565011523534-747a8601f10a?q=80&w=600&auto=format&fit=crop",
            "category": "Orchids",
            "is_hot": False,
            "stock": 15
        },
        {
            "name": "Mixed Tulip Delight",
            "description": "A colorful mix of fresh tulips.",
            "price": 34.99,
            "image_url": "https://images.unsplash.com/photo-1520763185298-1b434c919102?q=80&w=600&auto=format&fit=crop",
            "category": "Tulips",
            "is_hot": False,
            "stock": 40
        },
        {
            "name": "White Lilies Elegance",
            "description": "Pure white lilies, perfect for a peaceful vibe.",
            "price": 39.99,
            "image_url": "https://images.unsplash.com/photo-1552554523-d34cb0a5dc50?q=80&w=600&auto=format&fit=crop",
            "category": "Lilies",
            "is_hot": True,
            "stock": 25
        }
    ]
    
    print("Inserting sample products...")
    await db["products"].insert_many(sample_products)
    
    print("Seeding completed!")
    client.close()

if __name__ == "__main__":
    asyncio.run(seed())
