# 📊 Crypto Manager Database (Short Overview)

This project uses **MongoDB** to store and manage cryptocurrency data.  
We created a clean structure with one connection file and separate seed scripts for each collection.

---

## 🚀 What We Did
- Connected to MongoDB (`mongo_db.py`) and defined collections:
  - `assets` → crypto names + allocation percentages
  - `prices` → daily/hourly price data
  - `risk_trends` → risk levels + predictions
  - `alerts` → alerts for big changes
- Added seed scripts in the `seeds/` folder to insert sample data for each collection.
- Ensured seeds clear old data before inserting new records (so no duplicates).
- Built backend modules to query and update these collections.

---

---

## ⚙️ How to Use
1. Start MongoDB locally (`localhost:27017`).
2. Run seed scripts to populate collections:
   ```bash
   python seeds/seed_assets.py
   python seeds/seed_prices.py
   python seeds/seed_risk_trends.py
   python seeds/seed_alerts.py
