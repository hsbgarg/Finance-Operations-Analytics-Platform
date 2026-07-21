import streamlit as st


def apply_filters(transactions):

    st.sidebar.header("🔍 Filters")

    # -----------------------------
    # State
    # -----------------------------

    states = sorted(transactions["State"].dropna().unique())

    selected_states = st.sidebar.multiselect(
        "State",
        states,
        default=states
    )

    # -----------------------------
    # Program
    # -----------------------------

    programs = sorted(transactions["Program_ID"].dropna().unique())

    selected_programs = st.sidebar.multiselect(
        "Program",
        programs,
        default=programs
    )

    # -----------------------------
    # Transaction Type
    # -----------------------------

    types = sorted(transactions["Type"].dropna().unique())

    selected_types = st.sidebar.multiselect(
        "Transaction Type",
        types,
        default=types
    )

    # -----------------------------
    # Apply Filters
    # -----------------------------

    filtered = transactions.copy()

    filtered = filtered[
        filtered["State"].isin(selected_states)
    ]

    filtered = filtered[
        filtered["Program_ID"].isin(selected_programs)
    ]

    filtered = filtered[
        filtered["Type"].isin(selected_types)
    ]

    return filtered