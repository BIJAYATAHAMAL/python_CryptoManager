from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["crypto_manager"]
prices = db["prices"]

# Optional: clear old data
prices.delete_many({})

# Insert sample prices
prices.insert_many([
    {"asset": "Bitcoin", "date": "2025-12-10", "price": 45000},
    {"asset": "Ethereum", "date": "2025-12-10", "price": 3200},
    {"asset": "Solana", "date": "2025-12-10", "price": 150}
])

print("Prices seeded successfully!")