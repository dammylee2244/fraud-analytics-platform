import pandas as pd

df = pd.read_csv("data/silver/cleaned_transactions.csv")

customer_risk = (
    df.groupby("customer_id")
    .agg(
        total_transactions=("transaction_id", "count"),
        fraud_cases=("is_fraud", "sum"),
        high_risk_txns=("high_risk_transaction", "sum"),
        international_txns=("international_transaction", "sum"),
        suspicious_txns=("suspicious_activity", "sum"),
        total_amount=("amount", "sum")
    )
    .reset_index()
)

# Risk scoring formula
customer_risk["risk_score"] = (
    customer_risk["fraud_cases"] * 50 +
    customer_risk["high_risk_txns"] * 20 +
    customer_risk["international_txns"] * 10 +
    customer_risk["suspicious_txns"] * 25
)

# Risk category
customer_risk["risk_level"] = customer_risk["risk_score"].apply(
    lambda x: (
        "High" if x >= 100
        else "Medium" if x >= 50
        else "Low"
    )
)

# Sort highest risk first
customer_risk = customer_risk.sort_values(
    by="risk_score",
    ascending=False
)

customer_risk.to_csv(
    "data/gold/customer_risk_scores.csv",
    index=False
)

print("Customer risk scoring completed!")
