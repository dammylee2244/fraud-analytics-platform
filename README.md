# Fraud Analytics Platform

A modern analytics engineering project simulating real-time fraud analytics workflows using medallion architecture principles.
## Architecture Diagram

![Architecture Diagram](dashboards/architecture_diagram.png)

## Architecture

Bronze Layer
- Raw transaction ingestion

Silver Layer
- Fraud enrichment
- High-risk transaction detection
- International transaction analysis
- Suspicious activity flagging

Gold Layer
- Executive KPI reporting
- Merchant fraud analytics
- Country risk analysis
- Approval trend analysis

## Technologies Used

- Python
- Pandas
- Jupyter Notebook
- Medallion Architecture
- GitHub
- Fraud Analytics
- Analytics Engineering Concepts

## Project Structure

data/
- raw/
- silver/
- gold/

pipelines/
- silver_pipeline.py
- gold_pipeline.py
- analytics_pipeline.py

scripts/
- generate_transactions.py
- run_pipeline.py

## Example KPIs

- Fraud Rate %
- Suspicious Transactions
- Approval Rate
- High-Risk Transactions
- Country Risk Analysis
- Merchant Fraud Trends

## Future Enhancements

- PySpark Migration
- Apache Airflow Orchestration
- Docker Containerization
- Tableau / Power BI Dashboarding
- Real-time Streaming Pipelines
- Azure / Databricks Integration
