import streamlit as st

from utils.data_loader import *
from utils.validator import *

# -------------------------------------------------------
# LOAD DATA
# -------------------------------------------------------

transactions = load_transactions()
programs = load_programs()
grants = load_grants()

# -------------------------------------------------------
# VALIDATION REPORT
# -------------------------------------------------------

report = generate_validation_report(
    transactions,
    programs,
    grants
)

# -------------------------------------------------------
# PAGE
# -------------------------------------------------------

st.title("✅ Validation Dashboard")

st.caption("Finance data quality report.")

st.markdown("---")

# -------------------------------------------------------
# KPIs
# -------------------------------------------------------

total_checks = len(report)

passed = len(
    report[
        report["Status"] == "PASS"
    ]
)

failed = len(
    report[
        report["Status"] == "FAIL"
    ]
)

pass_rate = (passed / total_checks) * 100

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Validation Checks",
        total_checks
    )

with c2:
    st.metric(
        "Passed",
        passed
    )

with c3:
    st.metric(
        "Failed",
        failed
    )

with c4:
    st.metric(
        "Pass %",
        f"{pass_rate:.1f}%"
    )

st.markdown("---")

# -------------------------------------------------------
# REPORT
# -------------------------------------------------------

st.subheader("Validation Summary")

def color_status(value):

    if value == "PASS":
        return "background-color:#14532d;color:white"

    return "background-color:#991b1b;color:white"

styled = report.style.map(
    color_status,
    subset=["Status"]
)

st.dataframe(
    styled,
    use_container_width=True
)

st.markdown("---")

# -------------------------------------------------------
# DETAILS
# -------------------------------------------------------

st.subheader("Validation Details")

checks = {

    "Duplicate Transactions":
        check_duplicate_transactions(transactions),

    "Expense Amount Validation":
        check_expense_amounts(transactions),

    "Income Amount Validation":
        check_income_amounts(transactions),

    "Salary Validation":
        validate_salary_employee(transactions),

    "Vendor Validation":
        validate_vendor_transactions(transactions),

    "Program Validation":
        validate_program_ids(
            transactions,
            programs
        ),

    "Grant Validation":
        validate_grant_ids(
            transactions,
            grants
        ),

    "Payment Method Validation":
        validate_payment_method(
            transactions
        ),

    "Transaction Type Validation":
        validate_transaction_type(
            transactions
        ),

    "Status Validation":
        validate_status(
            transactions
        ),

    "Date Validation":
        validate_dates(
            transactions
        )

}

for name, result in checks.items():

    with st.expander(name):

        if len(result) == 0:

            st.success("No issues found.")

        else:

            st.error(
                f"{len(result)} records failed."
            )

            st.dataframe(
                result,
                use_container_width=True
            )

st.markdown("---")
st.subheader("📥 Download Validation Report")

csv = report.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Validation Report",
    data=csv,
    file_name="validation_report.csv",
    mime="text/csv"
)   

st.markdown("---")

st.caption(
    "Finance Operations Analytics Platform | Built with Python, Pandas, Plotly & Streamlit"
)


st.title("✅ Data Validation")