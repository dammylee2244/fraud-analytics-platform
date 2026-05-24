import pandas as pd

df = pd.read_csv("data/silver/cleaned_transactions.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Extract date
df["transaction_date"] = df["timestamp"].dt.date

# Daily fraud counts
trend_df = (
    df.groupby("transaction_date")
    .agg(
        fraud_cases=("is_fraud", "sum"),
        suspicious_transactions=("suspicious_activity", "sum"),
        total_transactions=("transaction_id", "count")
    )
    .reset_index()
)

trend_df.to_csv(
    "data/gold/fraud_trend_analysis.csv",
    index=False
)

print("Fraud trend analysis completed!")
