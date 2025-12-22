from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["crypto_manager"]

print("Connected to MongoDB:", db.name)

# Define collections
assets = db["assets"]
prices = db["prices"]
risk_trends = db["risk_trends"]
alerts = db["alerts"]

print("Collections ready!")