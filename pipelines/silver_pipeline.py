import pandas as pd

df = pd.read_csv("data/raw/transactions.csv")

# Clean column names
df.columns = df.columns.str.lower()

# Fraud rules
df["high_risk_transaction"] = df["amount"] > 3000

df["international_transaction"] = df["country"] != "US"

df["suspicious_activity"] = (
    df["high_risk_transaction"] &
    df["international_transaction"]
)

# Save silver layer
df.to_csv("data/silver/cleaned_transactions.csv", index=False)

print("Silver layer transformation completed!")
