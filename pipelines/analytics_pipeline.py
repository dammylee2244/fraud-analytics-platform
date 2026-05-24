import pandas as pd

df = pd.read_csv("data/silver/cleaned_transactions.csv")

# Merchant Fraud Analysis
merchant_analysis = (
    df.groupby("merchant")
    .agg(
        total_transactions=("transaction_id", "count"),
        fraud_cases=("is_fraud", "sum"),
        total_amount=("amount", "sum")
    )
    .reset_index()
)

merchant_analysis["fraud_rate_percent"] = round(
    (merchant_analysis["fraud_cases"] / merchant_analysis["total_transactions"]) * 100,
    2
)

merchant_analysis.to_csv(
    "data/gold/merchant_fraud_analysis.csv",
    index=False
)

# Country Analysis
country_analysis = (
    df.groupby("country")
    .agg(
        total_transactions=("transaction_id", "count"),
        fraud_cases=("is_fraud", "sum"),
        suspicious_transactions=("suspicious_activity", "sum")
    )
    .reset_index()
)

country_analysis.to_csv(
    "data/gold/country_risk_analysis.csv",
    index=False
)

# Approval Rate Analysis
approval_analysis = (
    df.groupby("status")
    .agg(
        total_transactions=("transaction_id", "count"),
        total_amount=("amount", "sum")
    )
    .reset_index()
)

approval_analysis.to_csv(
    "data/gold/approval_analysis.csv",
    index=False
)

print("Analytics datasets generated successfully!")
