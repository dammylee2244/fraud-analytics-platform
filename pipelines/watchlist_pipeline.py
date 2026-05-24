import pandas as pd

customer_df = pd.read_csv("data/gold/customer_risk_scores.csv")

merchant_df = pd.read_csv("data/gold/merchant_fraud_analysis.csv")

# High-risk customers
high_risk_customers = customer_df[
    customer_df["risk_level"] == "High"
][[
    "customer_id",
    "risk_score",
    "fraud_cases",
    "suspicious_txns"
]]

high_risk_customers["watchlist_type"] = "Customer"

# High-risk merchants
high_risk_merchants = merchant_df[
    merchant_df["fraud_rate_percent"] > 20
][[
    "merchant",
    "fraud_cases",
    "fraud_rate_percent"
]]

high_risk_merchants["watchlist_type"] = "Merchant"

# Standardize columns
high_risk_customers = high_risk_customers.rename(
    columns={
        "customer_id": "entity",
        "risk_score": "score"
    }
)

high_risk_merchants = high_risk_merchants.rename(
    columns={
        "merchant": "entity",
        "fraud_rate_percent": "score"
    }
)

watchlist_df = pd.concat([
    high_risk_customers[["entity", "score", "watchlist_type"]],
    high_risk_merchants[["entity", "score", "watchlist_type"]]
])

watchlist_df = watchlist_df.sort_values(
    by="score",
    ascending=False
)

watchlist_df.to_csv(
    "data/gold/fraud_watchlist.csv",
    index=False
)

print("Fraud watchlist generated successfully!")
