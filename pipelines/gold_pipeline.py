import pandas as pd

df = pd.read_csv("data/silver/cleaned_transactions.csv")

gold_metrics = {
    "total_transactions": len(df),
    "total_fraud_cases": df["is_fraud"].sum(),
    "fraud_rate_percent": round((df["is_fraud"].sum() / len(df)) * 100, 2),
    "high_risk_transactions": df["high_risk_transaction"].sum(),
    "international_transactions": df["international_transaction"].sum(),
    "suspicious_transactions": df["suspicious_activity"].sum(),
    "approved_transactions": (df["status"] == "approved").sum(),
    "declined_transactions": (df["status"] == "declined").sum(),
    "total_transaction_amount": round(df["amount"].sum(), 2)
}

gold_df = pd.DataFrame([gold_metrics])

gold_df.to_csv("data/gold/fraud_kpis.csv", index=False)

print("Gold layer KPI generation completed!")
