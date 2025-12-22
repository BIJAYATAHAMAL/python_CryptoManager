from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["crypto_manager"]
risk_trends = db["risk_trends"]

risk_trends.delete_many({})  # Clear old data

risk_trends.insert_many([
    {"asset": "Bitcoin", "risk_level": "Low", "prediction": "Stable", "timestamp": "2025-12-10"},
    {"asset": "Ethereum", "risk_level": "High", "prediction": "Volatile", "timestamp": "2025-12-10"},
    {"asset": "Solana", "risk_level": "Medium", "prediction": "Moderate Growth", "timestamp": "2025-12-10"}
])

print("Risk trends seeded successfully!")