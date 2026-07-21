import streamlit as st
import plotly.express as px

from utils.data_loader import *
from utils.finance_engine import *
print(expense_by_category)
from utils.helpers import *

from utils.filter_engine import *


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# LOAD DATA
# ============================================================

transactions = load_transactions()

budget = load_budget()
grants = load_grants() 
transactions = apply_filters(transactions)


# ============================================================
# KPI CALCULATIONS
# ============================================================

income = total_income(transactions)
expenses = total_expenses(transactions)
cashflow = net_cash_flow(transactions)

budget_used = budget_utilization(transactions, budget)
grant_used = grant_utilization(transactions, grants)

# ============================================================
# PAGE HEADER
# ============================================================

st.title("📊 Executive Dashboard")
st.caption("High-level financial overview of the organization.")

st.divider()

# ============================================================
# KPI CARDS
# ============================================================

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "💰 Total Income",
    format_currency(income)
)

c2.metric(
    "💸 Total Expenses",
    format_currency(expenses)
)

c3.metric(
    "💵 Net Cash Flow",
    format_currency(cashflow)
)

c4.metric(
    "📈 Budget Utilization",
    format_percentage(budget_used)
)

c5.metric(
    "🎯 Grant Utilization",
    format_percentage(grant_used)
)

st.divider()

# ============================================================
# EXECUTIVE ALERTS
# ============================================================

st.subheader("⚠ Executive Alerts")

if budget_used < 80:

    st.success("🟢 Budget utilization is healthy.")

elif budget_used <= 100:

    st.warning("🟡 Budget utilization is approaching the approved limit.")

else:

    st.error("🔴 Budget exceeded. Immediate financial review required.")

if grant_used > 100:

    st.error("🔴 Grant utilization exceeds available grant funding.")

st.divider()

# ============================================================
# CHARTS
# ============================================================

left, right = st.columns(2)

# ------------------------------------------------------------
# MONTHLY CASH FLOW
# ------------------------------------------------------------

with left:

    st.subheader("📈 Monthly Cash Flow")

    cashflow_df = monthly_cash_flow(transactions)

    fig_cash = px.line(
        cashflow_df,
        x="Date",
        y="Amount",
        markers=True,
        title="Monthly Net Cash Flow"
    )

    fig_cash.update_layout(
        height=420,
        xaxis_title="Month",
        yaxis_title="Cash Flow"
    )

    st.plotly_chart(
        fig_cash,
        use_container_width=True
    )

# ------------------------------------------------------------
# EXPENSE BREAKDOWN
# ------------------------------------------------------------

with right:

    st.subheader("💸 Expense Breakdown")

    expense_df = expense_by_category(transactions)

    fig_pie = px.pie(
        expense_df,
        names="Category",
        values="Amount",
        hole=0.45
    )

    fig_pie.update_layout(height=420)

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

st.divider()

# ============================================================
# TOP PROGRAMS
# ============================================================

st.subheader("🏥 Top Programs by Spend")

program_df = top_programs(transactions)

fig_program = px.bar(
    program_df,
    x="Program_ID",
    y="Amount",
    color="Amount",
    text_auto=".2s",
    title="Top Programs"
)

fig_program.update_layout(
    height=500,
    xaxis_title="Program",
    yaxis_title="Total Spend"
)

st.plotly_chart(
    fig_program,
    use_container_width=True
)

st.divider()

# ============================================================
# DASHBOARD FOOTER
# ============================================================

st.caption(
    "Finance Operations Analytics Platform | Executive Dashboard"
)

st.markdown("---")

st.subheader("📥 Download Reports")

csv = transactions.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Transactions",
    data=csv,
    file_name="executive_transactions.csv",
    mime="text/csv"
)

st.markdown("---")

st.caption(
    "Finance Operations Analytics Platform | Built with Python, Pandas, Plotly & Streamlit"
)

st.title("📊 Executive Dashboard")