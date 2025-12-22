# ⚙️ Crypto Manager Backend

The **backend** of the Crypto Manager project handles all logic and database operations.  
It connects to MongoDB, defines collections, and provides modules for portfolio management, risk analysis, alerts, and reporting.

---

## 🚀 Purpose
The backend is responsible for:
- Connecting to the MongoDB database (`crypto_manager`).
- Managing collections (`assets`, `prices`, `risk_trends`, `alerts`).
- Implementing business logic:
  - Portfolio allocation and investment mix.
  - Risk checking and predictions.
  - Alert generation for significant changes.
  - Report saving and rule setting.

This ensures the frontend can fetch structured data through APIs and display insights to users.

---

## 🗂 Project Structure
