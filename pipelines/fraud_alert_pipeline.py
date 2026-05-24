import pandas as pd

df = pd.read_csv("data/silver/cleaned_transactions.csv")

alerts = df[
    (
        (df["suspicious_activity"] == True)
        |
        (df["high_risk_transaction"] == True)
        |
        (df["is_fraud"] == 1)
    )
][[
    "transaction_id",
    "customer_id",
    "merchant",
    "amount",
    "country",
    "timestamp"
]]

# Alert severity
def assign_severity(amount):
    if amount >= 4000:
        return "Critical"
    elif amount >= 2000:
        return "High"
    else:
        return "Medium"

alerts["alert_severity"] = alerts["amount"].apply(assign_severity)

alerts["alert_status"] = "Open"

alerts = alerts.sort_values(
    by="amount",
    ascending=False
)

alerts.to_csv(
    "data/gold/fraud_alerts.csv",
    index=False
)

print("Fraud alerts generated successfully!")
