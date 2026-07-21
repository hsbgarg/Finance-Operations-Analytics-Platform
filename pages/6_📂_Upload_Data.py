import streamlit as st
import pandas as pd

st.title("📂 Upload Data")

st.caption("Upload finance datasets for analysis.")

st.markdown("---")

uploaded_file = st.file_uploader(
    "Upload Transactions CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Rows",
            len(df)
        )

    with c2:
        st.metric(
            "Columns",
            len(df.columns)
        )

    with c3:
        st.metric(
            "Missing Values",
            int(df.isna().sum().sum())
        )

    with c4:
        st.metric(
            "Duplicates",
            int(df.duplicated().sum())
        )

    st.markdown("---")

    st.subheader("Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Column Information")

    info = pd.DataFrame({

        "Column": df.columns,

        "Datatype": df.dtypes.astype(str),

        "Missing": df.isna().sum().values

    })

    st.dataframe(
        info,
        use_container_width=True
    )

st.markdown("---")

st.caption(
    "Finance Operations Analytics Platform | Built with Python, Pandas, Plotly & Streamlit"
)


st.title("📂 Upload Data")