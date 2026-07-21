import streamlit as st

from utils.data_loader import *

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Finance Operations Analytics Platform",
    page_icon="💰",
    layout="wide"
)
st.sidebar.success("🏠 Home")
# =====================================================
# LOAD DATA
# =====================================================

transactions = load_transactions()
employees = load_employees()
vendors = load_vendors()
programs = load_programs()
grants = load_grants()
budget = load_budget()

# =====================================================
# KPIs
# =====================================================

total_transactions = len(transactions)
total_employees = len(employees)
total_vendors = len(vendors)
total_programs = len(programs)
total_grants = len(grants)
total_budget = budget["Budget_Amount"].sum()

# =====================================================
# TITLE
# =====================================================

st.title("💰 Finance Operations Analytics Platform")

st.caption(
    "Enterprise Finance Analytics Solution for Budgeting, Grants, Vendors, Employees and Financial Reporting."
)

st.markdown("---")

# =====================================================
# OVERVIEW METRICS
# =====================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Transactions",
        f"{total_transactions:,}"
    )

with c2:
    st.metric(
        "Employees",
        total_employees
    )

with c3:
    st.metric(
        "Vendors",
        total_vendors
    )

c4, c5, c6 = st.columns(3)

with c4:
    st.metric(
        "Programs",
        total_programs
    )

with c5:
    st.metric(
        "Grants",
        total_grants
    )

with c6:
    st.metric(
        "Approved Budget",
        f"₹{total_budget/1e7:.2f} Cr"
    )

st.markdown("---")

# =====================================================
# PROJECT OVERVIEW
# =====================================================

st.header("📌 Project Overview")

st.write("""
This project simulates a Finance Operations Analytics Platform used by NGOs,
healthcare organizations and consulting firms to monitor financial operations.

The platform combines finance, analytics and business intelligence into a
single interactive application.
""")

st.markdown("### Core Modules")

col1, col2 = st.columns(2)

with col1:

    st.success("Executive Dashboard")

    st.success("Budget Dashboard")

    st.success("Employee Dashboard")

with col2:

    st.success("Vendor Dashboard")

    st.success("Financial Trends Dashboard")

    st.success("Validation Dashboard")

st.markdown("---")

# =====================================================
# FEATURES
# =====================================================

st.header("🚀 Platform Features")

feature1, feature2 = st.columns(2)

with feature1:

    st.markdown("""
✔ Executive KPIs

✔ Budget Monitoring

✔ Grant Utilization

✔ Vendor Analytics

✔ Employee Analytics

✔ Financial Trends
""")

with feature2:

    st.markdown("""
✔ Data Upload

✔ Validation Engine

✔ Interactive Charts

✔ Downloadable Reports

✔ Global Filters

✔ Finance KPI Engine
""")

st.markdown("---")

# =====================================================
# TECH STACK
# =====================================================

st.header("🛠 Tech Stack")

st.markdown("""
- Python

- Pandas

- Plotly

- Streamlit

- NumPy

- Modular Analytics Engine

- CSV Data Warehouse
""")

st.markdown("---")

st.info("👈 Use the navigation menu on the left to explore each dashboard.")