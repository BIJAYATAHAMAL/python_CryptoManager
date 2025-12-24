from backend.mongo_db import risk_trends

def get_risk_for_asset(asset_name):
    return risk_trends.find_one({"asset": asset_name}, sort=[("timestamp", -1)])

def get_all_risks():
    return list(risk_trends.find())

if __name__ == "__main__":
    print(get_all_risks())