import streamlit as st
import plotly.express as px

from utils.data_loader import *
from utils.finance_engine import *
from utils.helpers import *

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

transactions = load_transactions()

# ---------------------------------------------------------
# PAGE
# ---------------------------------------------------------

st.title("📈 Trends Dashboard")
st.caption("Financial trends across time.")

st.markdown("---")

# ---------------------------------------------------------
# LOAD TREND DATA
# ---------------------------------------------------------

income_df = monthly_income_trend(transactions)
expense_df = monthly_expense_trend(transactions)
cashflow_df = monthly_cash_flow(transactions)
txn_df = monthly_transactions(transactions)
program_df = program_trend(transactions)

# ---------------------------------------------------------
# KPI ROW
# ---------------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "💰 Total Income",
        format_currency(total_income(transactions))
    )

with c2:
    st.metric(
        "💸 Total Expenses",
        format_currency(total_expenses(transactions))
    )

with c3:
    st.metric(
        "💵 Net Cash Flow",
        format_currency(net_cash_flow(transactions))
    )

with c4:
    st.metric(
        "🧾 Transactions",
        len(transactions)
    )

st.markdown("---")

# ---------------------------------------------------------
# Income & Expense Trend
# ---------------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("📈 Monthly Income")

    fig = px.line(
        income_df,
        x="Date",
        y="Amount",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("📉 Monthly Expenses")

    fig = px.line(
        expense_df,
        x="Date",
        y="Amount",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------
# Cash Flow & Transactions
# ---------------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("💵 Monthly Cash Flow")

    fig = px.bar(
        cashflow_df,
        x="Date",
        y="Amount"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("🧾 Monthly Transactions")

    fig = px.line(
        txn_df,
        x="Date",
        y="Transactions",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------
# Program Trend
# ---------------------------------------------------------

st.subheader("🏥 Program Spending")

fig = px.bar(
    program_df,
    x="Program_ID",
    y="Amount",
    color="Amount"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------
# Table
# ---------------------------------------------------------

st.subheader("📋 Program Summary")

st.dataframe(
    program_df,
    use_container_width=True
)

st.markdown("---")
st.subheader("📥 Download Trend Data")

csv = transactions.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Trend Data",
    data=csv,
    file_name="financial_trends.csv",
    mime="text/csv"
)

st.markdown("---")

st.caption(
    "Finance Operations Analytics Platform | Built with Python, Pandas, Plotly & Streamlit"
)


st.title("📈Financial Trends")