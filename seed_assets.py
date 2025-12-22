from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["crypto_manager"]
assets = db["assets"]

# Optional: clear old data to avoid duplicates
assets.delete_many({})

# Insert sample assets
assets.insert_many([
    {"name": "Bitcoin", "allocation": 40},
    {"name": "Ethereum", "allocation": 35},
    {"name": "Solana", "allocation": 25}
])

print("Assets seeded successfully!")