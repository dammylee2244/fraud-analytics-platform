import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(
    page_title="Fraud Analytics Dashboard",
    layout="wide"
)

st.title("🚨 Fraud Analytics Monitoring Dashboard")

conn = sqlite3.connect("warehouse/fraud_analytics.db")

# Load datasets
kpi_df = pd.read_sql("SELECT * FROM fraud_kpis", conn)

alerts_df = pd.read_sql(
    "SELECT * FROM fraud_alerts LIMIT 10",
    conn
)

watchlist_df = pd.read_sql(
    "SELECT * FROM fraud_watchlist LIMIT 10",
    conn
)

country_df = pd.read_sql(
    "SELECT * FROM country_risk_analysis",
    conn
)
trend_df = pd.read_sql(
    "SELECT * FROM fraud_trend_analysis",
    conn
)
# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric(
    "Fraud Cases",
    int(kpi_df["total_fraud_cases"][0])
)

col2.metric(
    "Suspicious Transactions",
    int(kpi_df["suspicious_transactions"][0])
)

col3.metric(
    "Fraud Rate %",
    float(kpi_df["fraud_rate_percent"][0])
)

st.divider()

# Country Risk Chart
st.subheader("Fraud Cases by Country")

st.bar_chart(
    country_df.set_index("country")["fraud_cases"]
)
st.subheader("🚨 Critical Fraud Alerts")

critical_alerts = pd.read_sql(
    """
    SELECT *
    FROM fraud_alerts
    WHERE alert_severity = 'Critical'
    LIMIT 20
    """,
    conn
)

st.dataframe(critical_alerts)
st.subheader("📈 Fraud Trends Over Time")

trend_chart = trend_df.set_index(
    "transaction_date"
)[[
    "fraud_cases",
    "suspicious_transactions"
]]

st.line_chart(trend_chart)
# Fraud Alerts
st.subheader("🚨 Fraud Alerts")

st.dataframe(alerts_df)
st.subheader("⚠️ High Risk Watchlist")

watchlist = pd.read_sql(
    """
    SELECT *
    FROM fraud_watchlist
    LIMIT 20
    """,
    conn
)

st.dataframe(watchlist)
# Watchlist
st.subheader("⚠️ Fraud Watchlist")

st.dataframe(watchlist_df)
st.subheader("👤 Top High-Risk Customers")

top_customers = pd.read_sql(
    """
    SELECT customer_id, risk_score, risk_level
    FROM customer_risk_scores
    ORDER BY risk_score DESC
    LIMIT 10
    """,
    conn
)

st.dataframe(top_customers)
conn.close()
