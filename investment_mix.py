from backend.mongo_db import assets, prices

def get_portfolio_allocation():
    portfolio = []
    for asset in assets.find():
        latest_price = prices.find_one({"asset": asset["name"]}, sort=[("date", -1)])
        portfolio.append({
            "asset": asset["name"],
            "allocation": asset["allocation"],
            "latest_price": latest_price["price"] if latest_price else None
        })
    return portfolio

if __name__ == "__main__":
    print(get_portfolio_allocation())