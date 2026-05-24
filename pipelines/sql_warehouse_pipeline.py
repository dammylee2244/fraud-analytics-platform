import sqlite3
import pandas as pd

conn = sqlite3.connect("warehouse/fraud_analytics.db")

datasets = {
    "transactions": "data/silver/cleaned_transactions.csv",
    "fraud_kpis": "data/gold/fraud_kpis.csv",
    "merchant_fraud_analysis": "data/gold/merchant_fraud_analysis.csv",
    "country_risk_analysis": "data/gold/country_risk_analysis.csv",
    "approval_analysis": "data/gold/approval_analysis.csv",
    "customer_risk_scores": "data/gold/customer_risk_scores.csv",
    "velocity_risk_analysis": "data/gold/velocity_risk_analysis.csv",
    "fraud_loss_analysis": "data/gold/fraud_loss_analysis.csv",
    "fraud_watchlist": "data/gold/fraud_watchlist.csv",
    "fraud_alerts": "data/gold/fraud_alerts.csv",
    "fraud_trend_analysis": "data/gold/fraud_trend_analysis.csv"
}

for table_name, file_path in datasets.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded {table_name}")

conn.close()

print("SQLite fraud analytics warehouse created successfully!")
