import pandas as pd
from faker import Faker
import random
from datetime import datetime

fake = Faker()

transactions = []

for i in range(1000):
    transactions.append({
        "transaction_id": i + 1,
        "customer_id": random.randint(1000, 5000),
        "merchant": fake.company(),
        "amount": round(random.uniform(5, 5000), 2),
        "transaction_type": random.choice(["purchase", "withdrawal", "transfer"]),
        "country": random.choice(["US", "UK", "NG", "CA"]),
        "status": random.choice(["approved", "declined"]),
        "timestamp": datetime.now(),
        "is_fraud": random.choice([0, 0, 0, 1])
    })

df = pd.DataFrame(transactions)

df.to_csv("data/raw/transactions.csv", index=False)

print("Transaction dataset generated successfully!")
