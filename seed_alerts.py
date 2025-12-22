from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["crypto_manager"]
alerts = db["alerts"]

alerts.delete_many({})  # Clear old data

alerts.insert_many([
    {"asset": "Ethereum", "message": "⚠ Price dropped 10% today", "timestamp": "2025-12-10"},
    {"asset": "Solana", "message": "📈 Risk level increased", "timestamp": "2025-12-10"}
])

print("Alerts seeded successfully!")