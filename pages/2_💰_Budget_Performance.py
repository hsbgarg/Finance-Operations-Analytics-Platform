import streamlit as st
import plotly.express as px

from utils.data_loader import *
from utils.finance_engine import *
from utils.helpers import *

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------

transactions = load_transactions()
budget = load_budget()

budget_total = total_budget(budget)
expenses = total_expenses(transactions)
remaining = budget_remaining(transactions, budget)
utilization = budget_utilization(transactions, budget)

comparison = budget_vs_actual(transactions, budget)

# ---------------------------------------------------
# Page
# ---------------------------------------------------

st.title("💰 Budget Dashboard")

st.caption("Budget planning and utilization overview.")

st.markdown("---")

# ---------------------------------------------------
# KPI Cards
# ---------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Approved Budget",
    format_currency(budget_total)
)

col2.metric(
    "Actual Spend",
    format_currency(expenses)
)

col3.metric(
    "Remaining Budget",
    format_currency(remaining)
)

col4.metric(
    "Budget Utilization",
    format_percentage(utilization)
)

st.markdown("---")

# ---------------------------------------------------
# Budget Alerts
# ---------------------------------------------------

st.subheader("🚨 Budget Alerts")

if utilization < 80:

    st.success("Budget utilization is healthy.")

elif utilization <= 100:

    st.warning("Budget utilization approaching limit.")

else:

    st.error("Budget exceeded.")

st.markdown("---")

# ---------------------------------------------------
# Budget vs Actual
# ---------------------------------------------------

st.subheader("📊 Budget vs Actual")

fig = px.bar(

    comparison,

    x="Department",

    y=["Budget", "Actual"],

    barmode="group",

    title="Department Budget Comparison"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# Department Utilization
# ---------------------------------------------------

comparison["Utilization %"] = (
    comparison["Actual"] /
    comparison["Budget"] * 100
)

st.subheader("📈 Department Utilization")

fig = px.bar(

    comparison,

    x="Department",

    y="Utilization %",

    color="Utilization %",

    text_auto=".1f"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# Budget Table
# ---------------------------------------------------

st.subheader("📋 Budget Summary")

comparison["Budget"] = comparison["Budget"].apply(format_currency)
comparison["Actual"] = comparison["Actual"].apply(format_currency)
comparison["Utilization %"] = comparison["Utilization %"].round(2)

st.dataframe(
    comparison,
    use_container_width=True
)

st.markdown("---")
st.subheader("📥 Download Budget Report")

csv = comparison.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Budget Summary",
    data=csv,
    file_name="budget_summary.csv",
    mime="text/csv"
)

st.markdown("---")

st.caption(
    "Finance Operations Analytics Platform | Built with Python, Pandas, Plotly & Streamlit"
)

st.title("💰 Budget Performance")