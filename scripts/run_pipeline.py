import subprocess

print("Starting Fraud Analytics Pipeline...")

steps = [
    "python scripts/generate_transactions.py",
    "python pipelines/silver_pipeline.py",
    "python pipelines/gold_pipeline.py",
    "python pipelines/analytics_pipeline.py",
    "python pipelines/customer_risk_pipeline.py",
    "python pipelines/velocity_risk_pipeline.py",
    "python pipelines/fraud_loss_pipeline.py",
    "python pipelines/watchlist_pipeline.py",
    "python pipelines/fraud_alert_pipeline.py",
    "python pipelines/sql_warehouse_pipeline.py"
]

for step in steps:
    print(f"Running: {step}")
    subprocess.run(step, shell=True, check=True)

print("Fraud Analytics Pipeline Completed Successfully!")
