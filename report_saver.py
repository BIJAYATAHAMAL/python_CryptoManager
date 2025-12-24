import csv
from backend.mongo_db import alerts

def export_alerts_to_csv(filename="alerts_report.csv"):
    all_alerts = list(alerts.find())

    # Remove MongoDB's _id field
    for alert in all_alerts:
        alert.pop("_id", None)

    # Open file with UTF-8 encoding to handle special characters
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["asset", "message", "timestamp"])
        writer.writeheader()
        writer.writerows(all_alerts)

    return f"Report saved as {filename}"

if __name__ == "__main__":
    print(export_alerts_to_csv())