import pandas as pd

df = pd.read_csv("data/silver/cleaned_transactions.csv")

# Fraud-only transactions
fraud_df = df[df["is_fraud"] == 1]

# Suspicious activity transactions
suspicious_df = df[df["suspicious_activity"] == True]

loss_metrics = {
    "total_fraud_transactions": len(fraud_df),
    "total_fraud_exposure": round(fraud_df["amount"].sum(), 2),
    "average_fraud_transaction": round(fraud_df["amount"].mean(), 2),
    "suspicious_transaction_exposure": round(suspicious_df["amount"].sum(), 2),
    "estimated_loss_prevention": round(
        suspicious_df["amount"].sum() * 0.7,
        2
    )
}

loss_df = pd.DataFrame([loss_metrics])

loss_df.to_csv(
    "data/gold/fraud_loss_analysis.csv",
    index=False
)

print("Fraud loss analysis completed!")

