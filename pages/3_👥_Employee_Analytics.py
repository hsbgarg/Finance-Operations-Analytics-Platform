import streamlit as st
import plotly.express as px

from utils.data_loader import *
from utils.finance_engine import *
from utils.helpers import *

# ======================================================
# LOAD DATA
# ======================================================

transactions = load_transactions()
employees = load_employees()

# ======================================================
# PAGE CONFIG
# ======================================================

st.title("👨 Employee Dashboard")

st.caption("Payroll and workforce analytics.")

st.markdown("---")

# ======================================================
# KPIs
# ======================================================

total_emp = len(employees)

payroll = payroll_cost(transactions)

avg_salary = average_salary(employees)

highest = highest_salary(employees)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "👥 Employees",
        format_number(total_emp)
    )

with c2:
    st.metric(
        "💰 Payroll Cost",
        format_currency(payroll)
    )

with c3:
    st.metric(
        "📈 Average Salary",
        format_currency(avg_salary)
    )

with c4:
    st.metric(
        "🏆 Highest Salary",
        format_currency(highest)
    )

st.markdown("---")

# ======================================================
# CHARTS
# ======================================================

left, right = st.columns(2)

# -----------------------------------------------------

with left:

    st.subheader("🏢 Salary by Department")

    dept = salary_by_department(
        transactions,
        employees
    )

    fig = px.bar(
        dept,
        x="Department",
        y="Amount",
        color="Amount",
        text="Amount"
    )

    fig.update_layout(height=450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------------------------------

with right:

    st.subheader("🥧 Designation Distribution")

    desig = designation_distribution(employees)

    fig = px.pie(
        desig,
        names="Designation",
        values="Employees",
        hole=0.45
    )

    fig.update_layout(height=450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# ======================================================
# SECOND ROW
# ======================================================

left, right = st.columns(2)

# -----------------------------------------------------

with left:

    st.subheader("🌍 Employees by State")

    state = employee_state_distribution(employees)

    fig = px.bar(
        state,
        x="State",
        y="Employees",
        color="Employees",
        text="Employees"
    )

    fig.update_layout(height=450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------------------------------

with right:

    st.subheader("📈 Monthly Payroll")

    payroll_df = monthly_salary(transactions)

    fig = px.line(
        payroll_df,
        x="Date",
        y="Amount",
        markers=True
    )

    fig.update_layout(height=450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# ======================================================
# EMPLOYEE TABLE
# ======================================================

st.subheader("📋 Employee Master")

table = employee_table(employees)

table["Salary"] = table["Salary"].apply(format_currency)

st.dataframe(
    table,
    hide_index=True,
    use_container_width=True
)

st.markdown("---")
st.subheader("📥 Download Employee Report")

csv = employees.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Employee Data",
    data=csv,
    file_name="employees.csv",
    mime="text/csv"
)
st.markdown("---")

st.caption(
    "Finance Operations Analytics Platform | Built with Python, Pandas, Plotly & Streamlit"
)


st.title("👥 Employee Analytics")