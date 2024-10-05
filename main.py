import subprocess

def install_requirements(requirements_file):
    subprocess.check_call(['pip', 'install', '-r', requirements_file])

# Example usage:
requirements_file = 'requirements.txt'
install_requirements(requirements_file)


import streamlit as st
import ydata_profiling as ydp
import pandas as pd

def analyze_csv(uploaded_file):
    if uploaded_file is not None:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)

        # Generate a yData profile report
        profile = ydp.ProfileReport(df)

        # Generate the HTML output
        html = profile.to_html()

        return html

st.title("CSV File Analyzer")

# Upload file
uploaded_file = st.file_uploader("Upload a CSV file")

# Analyze and display output
if st.button("Analyze"):
    html = analyze_csv(uploaded_file)
    if html:
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.warning("Please upload a valid CSV file.")