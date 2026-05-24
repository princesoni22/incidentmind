import streamlit as st
import requests

st.set_page_config(
    page_title="IncidentMind",
    layout="wide"
)

st.title("🚨 IncidentMind")
st.subheader(
    "AI-Powered Incident RCA Agent"
)

uploaded_file = st.file_uploader(
    "Upload Incident Logs CSV",
    type=["csv"]
)

if uploaded_file:

    with st.spinner(
        "Analyzing incident..."
    ):

        files = {
            "file": uploaded_file
        }

        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            files=files
        )

        data = response.json()

        st.success(
            "Incident analysis completed."
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("📌 Timeline")

            for event in data["timeline"]:
                st.write(event)

        with col2:

            st.subheader("🧠 AI Hypothesis")

            st.write(
                data["hypothesis"]
            )

        st.subheader(
            "📚 Similar Historical Incidents"
        )

        for incident in data["incidents"]:

            st.info(incident)

        st.subheader(
            "📄 Root Cause Analysis Report"
        )

        st.markdown(data["rca"])