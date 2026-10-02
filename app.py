import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Tilak Nagar Civic Pulse",
    page_icon="🏙️",
    layout="wide"
)

DATA_FILE = Path("data/processed/responses_clean.csv")

FORM_URL = (
    "https://docs.google.com/forms/d/e/"
    "1FAIpQLSfoHwmxp7nqI7llEDLzGhurB_3PtyoFnDqt0Ou4lsFUmL722A/"
    "viewform?usp=header"
)

st.title("🏙️ Tilak Nagar Civic Pulse")
st.subheader("Resident Satisfaction with Local Government Services")

st.write(
    "This project analyses residents' opinions about water supply, "
    "garbage collection, roads, cleanliness and other local services."
)

st.markdown(f"[📝 Open the Community Survey]({FORM_URL})")

tab1, tab2, tab3 = st.tabs([
    "Project Overview",
    "Dashboard",
    "Methodology"
])

with tab1:
    st.header("About the Project")

    st.write(
        "The purpose of this project is to understand residents' "
        "satisfaction with basic local government services in Tilak Nagar, Mumbai."
    )

    st.subheader("Project Objectives")

    st.markdown("""
    - Measure resident satisfaction.
    - Identify services needing improvement.
    - Analyse community suggestions.
    - Present findings through charts and a dashboard.
    """)

with tab2:
    st.header("Survey Dashboard")

    if not DATA_FILE.exists():
        st.info(
            "Survey data is not available yet. "
            "After collecting responses, place responses_clean.csv "
            "inside data/processed/."
        )

    else:
        df = pd.read_csv(DATA_FILE)

        if df.empty:
            st.warning("The cleaned dataset is currently empty.")

        else:
            st.metric("Total Responses", len(df))
            st.dataframe(df, use_container_width=True)

with tab3:
    st.header("Methodology")

    st.write("""
    Responses will be collected through a Google Form.
    Python Pandas will be used to clean the data.
    Matplotlib and Seaborn will be used to create visualisations.
    Streamlit will display the final project website.
    """)

    st.warning(
        "The findings will represent only the surveyed participants "
        "and not the entire population of Mumbai."
    )