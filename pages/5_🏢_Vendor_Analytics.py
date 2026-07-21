import streamlit as st
import plotly.express as px

from utils.data_loader import *
from utils.finance_engine import *
from utils.helpers import *

# ======================================================
# LOAD DATA
# ======================================================

transactions = load_transactions()

# ======================================================
# PAGE CONFIG
# ======================================================

st.title("🏢 Vendor Dashboard")

st.caption("Vendor spending and payment analytics.")

st.markdown("---")

# ======================================================
# KPI SECTION
# ======================================================

vendor_df = vendor_spend(transactions)

total_vendor_spend = vendor_df["Amount"].sum()

top_vendor_amount = vendor_df.iloc[0]["Amount"]

total_vendors = len(vendor_df)

avg_vendor_spend = total_vendor_spend / total_vendors

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "💰 Total Vendor Spend",
        format_currency(total_vendor_spend)
    )

with c2:
    st.metric(
        "🏢 Vendors",
        format_number(total_vendors)
    )

with c3:
    st.metric(
        "🥇 Highest Vendor Spend",
        format_currency(top_vendor_amount)
    )

with c4:
    st.metric(
        "📊 Average Spend",
        format_currency(avg_vendor_spend)
    )

st.markdown("---")

# ======================================================
# CHARTS
# ======================================================

left, right = st.columns(2)

# ------------------------------------------------------

with left:

    st.subheader("🏆 Top 10 Vendors")

    top10 = top_vendors(transactions)

    fig = px.bar(
        top10,
        x="Vendor_ID",
        y="Amount",
        color="Amount",
        text="Amount"
    )

    fig.update_traces(
        texttemplate="%{text:.2s}",
        textposition="outside"
    )

    fig.update_layout(height=450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ------------------------------------------------------

with right:

    st.subheader("💳 Payment Methods")

    payment = payment_method_breakdown(transactions)

    fig = px.pie(
        payment,
        names="Payment_Method",
        values="Transactions",
        hole=0.45
    )

    fig.update_layout(height=450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# ======================================================
# STATE CHART
# ======================================================

st.subheader("🗺️ Vendor Spend by State")

state_df = vendor_state_distribution(transactions)

fig = px.bar(
    state_df,
    x="State",
    y="Amount",
    color="Amount",
    text="Amount"
)

fig.update_layout(height=500)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ======================================================
# TABLE
# ======================================================

st.subheader("📋 Vendor Spend Table")

vendor_table = vendor_spend(transactions)

vendor_table["Amount"] = vendor_table["Amount"].apply(format_currency)

st.dataframe(
    vendor_table,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")
st.subheader("📥 Download Vendor Report")

csv = vendor_summary.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Vendor Summary",
    data=csv,
    file_name="vendor_summary.csv",
    mime="text/csv"
)

st.markdown("---")

st.caption(
    "Finance Operations Analytics Platform | Built with Python, Pandas, Plotly & Streamlit"
)


st.title("🏢 Vendor Analytics")