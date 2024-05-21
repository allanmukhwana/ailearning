import streamlit as st
from arctic import Arctic
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to Snowflake Arctic using environment variables
conn_details = {
    'account': os.getenv('SNOWFLAKE_ACCOUNT'),
    'user': os.getenv('SNOWFLAKE_USER'),
    'password': os.getenv('SNOWFLAKE_PASSWORD'),
    'database': os.getenv('SNOWFLAKE_DATABASE'),
    'schema': os.getenv('SNOWFLAKE_SCHEMA')
}
arctic = Arctic(**conn_details)

def main():
    # Set up the app layout and sidebar inputs
    st.title("Prenatal and Postnatal Care Advice")
    type_input = st.sidebar.selectbox("Type", ["Pre Natal", "Post Natal"])
    time_input = st.sidebar.number_input("Time (in weeks for prenatal or months for postnatal)", min_value=0)
    health_condition = st.sidebar.text_input("Health Condition (optional)")
