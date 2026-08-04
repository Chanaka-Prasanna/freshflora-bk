import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

flowers_data = [
    {
        "name": "Ruby Red Romance",
        "description": "Two dozen premium long-stemmed red roses arranged with baby's breath.",
        "price": 1250,
        "image_url": "https://images.unsplash.com/photo-1531874824027-2a0d33bd6338?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Roses",
        "is_hot": True,
        "stock": 15,
        "orders": 120,
        "availability": "In Stock"
    },
    {
        "name": "Midnight Orchids",
        "description": "Elegant purple phalaenopsis orchids in a ceramic pot.",
        "price": 1300,
        "image_url": "https://images.unsplash.com/photo-1582862058398-c157c8424b54?q=80&w=2127&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Orchids",
        "is_hot": False,
        "stock": 0,
        "orders": 45,
        "availability": "Out of Stock"
    },
    {
        "name": "Sunflower Sunshine",
        "description": "A bright burst of fresh sunflowers to lighten up any room.",
        "price": 1450,
        "image_url": "https://images.unsplash.com/photo-1533523611631-15e4ef69be08?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Sunflowers",
        "is_hot": True,
        "stock": 20,
        "orders": 310,
        "availability": "In Stock"
    },
    {
        "name": "Spring Tulips",
        "description": "A colorful mix of imported Dutch tulips.",
        "price": 1100,
        "image_url": "https://images.unsplash.com/photo-1614791199038-6869a104fe5f?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Tulips",
        "is_hot": False,
        "stock": 5,
        "orders": 12,
        "availability": "Limited Season"
    },
    {
        "name": "White Lilies Elegance",
        "description": "Pure white oriental lilies symbolizing peace and purity.",
        "price": 1450,
        "image_url": "https://images.unsplash.com/photo-1695556557825-97adbe470fd6?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Lilies",
        "is_hot": False,
        "stock": 0,
        "orders": 85,
        "availability": "Pre-Order"
    },
    {
        "name": "Blushing Peonies",
        "description": "Lush pink peonies that are a seasonal favorite.",
        "price": 1600,
        "image_url": "https://images.unsplash.com/photo-1557926005-012bd4382a0d?q=80&w=1972&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Peonies",
        "is_hot": True,
        "stock": 8,
        "orders": 200,
        "availability": "Limited Season"
    },
    {
        "name": "Hydrangea Heaven",
        "description": "Voluminous blue and white hydrangeas.",
        "price": 950,
        "image_url": "https://images.unsplash.com/photo-1531875565264-5b473e59fa07?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Hydrangeas",
        "is_hot": False,
        "stock": 30,
        "orders": 140,
        "availability": "In Stock"
    },
    {
        "name": "Autumn Mixed Bouquet",
        "description": "A stunning mix of orange, yellow, and red seasonal blooms.",
        "price": 1200,
        "image_url": "https://images.unsplash.com/photo-1620752379460-d4adfe02a5ce?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Mixed Bouquets",
        "is_hot": False,
        "stock": 0,
        "orders": 45,
        "availability": "Out of Stock"
    },
    {
        "name": "Royal Red Orchids",
        "description": "Rare deep red orchids for a touch of luxury.",
        "price": 2200,
        "image_url": "https://images.unsplash.com/photo-1562133558-4a3906179c67?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Orchids",
        "is_hot": True,
        "stock": 0,
        "orders": 29,
        "availability": "Pre-Order"
    },
    {
        "name": "Golden Roses",
        "description": "Stunning yellow roses wrapped in premium paper.",
        "price": 1150,
        "image_url": "https://plus.unsplash.com/premium_photo-1688045713393-53ed4a31202b?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Roses",
        "is_hot": False,
        "stock": 23,
        "orders": 150,
        "availability": "In Stock"
    },
    {
        "name": "Lavender Dream",
        "description": "A fragrant bouquet of lavender and mixed purple florals.",
        "price": 2000,
        "image_url": "https://plus.unsplash.com/premium_photo-1674581217534-d2c84b63bbd7?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Mixed Bouquets",
        "is_hot": False,
        "stock": 11,
        "orders": 90,
        "availability": "In Stock"
    },
    {
        "name": "Stargazer Lilies",
        "description": "Vibrant pink lilies known for their striking appearance and sweet scent.",
        "price": 1300,
        "image_url": "https://plus.unsplash.com/premium_photo-1676068243733-df1880c2aef8?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Lilies",
        "is_hot": True,
        "stock": 65,
        "orders": 310,
        "availability": "In Stock"
    },
    {
        "name": "Classic White Roses",
        "description": "A serene bouquet of 12 pristine white roses.",
        "price": 1440,
        "image_url": "https://images.unsplash.com/photo-1518895949257-7621c3c786d7?q=80&w=1976&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Roses",
        "is_hot": False,
        "stock": 56,
        "orders": 210,
        "availability": "In Stock"
    },
    {
        "name": "Pink Peony Bliss",
        "description": "Delicate and fluffy light pink peonies in a glass vase.",
        "price": 1750,
        "image_url": "https://images.unsplash.com/photo-1575178114667-c8a832c61f45?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Peonies",
        "is_hot": False,
        "stock": 0,
        "orders": 120,
        "availability": "Out of Stock"
    },
    {
        "name": "Sunny Yellow Tulips",
        "description": "A cheerful bunch of yellow tulips to brighten the day.",
        "price": 1050,
        "image_url": "https://images.unsplash.com/photo-1468327768560-75b778cbb551?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Tulips",
        "is_hot": False,
        "stock": 129,
        "orders": 60,
        "availability": "Limited Season"
    },
    {
        "name": "Pastel Hydrangea Mix",
        "description": "A soft pastel blend of pink, blue, and white hydrangeas.",
        "price": 1400,
        "image_url": "https://images.unsplash.com/photo-1593624212435-0d075a890bdb?q=80&w=1976&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Hydrangeas",
        "is_hot": True,
        "stock": 0,
        "orders": 150,
        "availability": "Pre-Order"
    },
    {
        "name": "Rustic Sunflowers",
        "description": "Sunflowers arranged with rustic greenery and wheat.",
        "price": 100,
        "image_url": "https://images.unsplash.com/photo-1597848212624-a19eb35e2651?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Sunflowers",
        "is_hot": False,
        "stock": 245,
        "orders": 280,
        "availability": "In Stock"
    },
    {
        "name": "Tropical Orchid Mix",
        "description": "A vivid arrangement of tropical orchids and exotic leaves.",
        "price": 1900,
        "image_url": "https://plus.unsplash.com/premium_photo-1676253694654-79c2214ccbc7?q=80&w=1976&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Orchids",
        "is_hot": False,
        "stock": 483,
        "orders": 75,
        "availability": "In Stock"
    },
    {
        "name": "Romantic Red Mixed",
        "description": "Red roses mixed with deep red carnations and greenery.",
        "price": 1100,
        "image_url": "https://plus.unsplash.com/premium_photo-1713823800827-4c10d4d37585?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Mixed Bouquets",
        "is_hot": True,
        "stock": 200,
        "orders": 340,
        "availability": "In Stock"
    },
    {
        "name": "Springtime Magic",
        "description": "A vibrant mix of tulips, roses, and daisies in spring colors.",
        "price": 1500,
        "image_url": "https://plus.unsplash.com/premium_photo-1670426502036-a27ea107b22b?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Mixed Bouquets",
        "is_hot": True,
        "stock": 40,
        "orders": 410,
        "availability": "Limited Season"
    },
    {
        "name": "Elegant White Lilies",
        "description": "Classic white oriental lilies in a tall crystal vase.",
        "price": 1350,
        "image_url": "https://images.unsplash.com/photo-1657023649437-30ed616a6e6d?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Lilies",
        "is_hot": False,
        "stock": 0,
        "orders": 65,
        "availability": "Pre-Order"
    },
    {
        "name": "Sunset Peonies",
        "description": "Coral and orange peonies reminiscent of a summer sunset.",
        "price": 1700,
        "image_url": "https://images.unsplash.com/photo-1620221759647-a53656905677?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Peonies",
        "is_hot": True,
        "stock": 6,
        "orders": 143,
        "availability": "Limited Season"
    },
    {
        "name": "Mixed Bouquets",
        "description": " a vibrant mixed bouquet featuring pink and orange peonies reminiscent of a summer sunset.",
        "price": 1200,
        "image_url": "https://images.unsplash.com/photo-1541275055241-329bbdf9a191?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "category": "Mixed Bouquets",
        "is_hot": True,
        "stock": 25,
        "orders": 190,
        "availability": "Limited Season"
    }
]

async def seed_db():
    client = AsyncIOMotorClient(settings.mongodb_url)
    db = client[settings.database_name]
    
    # Clear existing products to ensure a clean slate with 20+ items
    await db.products.delete_many({})
    
    # Insert new sample products
    result = await db.products.insert_many(flowers_data)
    print(f"Successfully seeded {len(result.inserted_ids)} products into the database!")

if __name__ == "__main__":
    asyncio.run(seed_db())
