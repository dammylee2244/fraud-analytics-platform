import pandas as pd

df = pd.read_csv("data/silver/cleaned_transactions.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Transaction counts per customer
velocity_df = (
    df.groupby("customer_id")
    .agg(
        transaction_count=("transaction_id", "count"),
        total_amount=("amount", "sum")
    )
    .reset_index()
)

# Velocity rules
velocity_df["high_velocity_flag"] = (
    velocity_df["transaction_count"] > 5
)

velocity_df["velocity_risk_score"] = (
    velocity_df["transaction_count"] * 10
)

velocity_df["velocity_risk_level"] = velocity_df[
    "velocity_risk_score"
].apply(
    lambda x: (
        "High" if x >= 100
        else "Medium" if x >= 50
        else "Low"
    )
)

velocity_df = velocity_df.sort_values(
    by="velocity_risk_score",
    ascending=False
)

velocity_df.to_csv(
    "data/gold/velocity_risk_analysis.csv",
    index=False
)

print("Velocity risk analysis completed!")
