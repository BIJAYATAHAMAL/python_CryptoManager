from backend.mongo_db import assets

def rebalance_portfolio(new_rules):
    for asset_name, new_allocation in new_rules.items():
        assets.update_one({"name": asset_name}, {"$set": {"allocation": new_allocation}})
    return list(assets.find())

if __name__ == "__main__":
    rules = {"Bitcoin": 50, "Ethereum": 30, "Solana": 20}
    print(rebalance_portfolio(rules))