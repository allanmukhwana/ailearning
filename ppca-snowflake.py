import streamlit as st
import os
from snowflake.arctic import Arctic

# Set up Snowflake Arctic connection secrets
SF_ACCOUNT = st.secrets["SF_ACCOUNT"]
SF_USER = st.secrets["SF_USER"]
SF_PASSWORD = st.secrets["SF_PASSWORD"]
SF_WAREHOUSE = st.secrets["SF_WAREHOUSE"]
SF_DB = st.secrets["SF_DB"]
SF_SCHEMA = st.secrets["SF_SCHEMA"]

# Create an Arctic instance
arctic = Arctic(account=SF_ACCOUNT, user=SF_USER, password=SF_PASSWORD, warehouse=SF_WAREHOUSE, database=SF_DB, schema=SF_SCHEMA)

st.image('https://miro.medium.com/v2/resize:fit:690/1*vg8hAZtD0idNCVLf2tCpCA.jpeg')
st.title("PPCA - Prenatal and Postnatal Care Assistant")
st.write("Get personalized advice and guidance for a healthy pregnancy and parenthood journey.")

# Input fields
type_input = st.selectbox("Type", ["Pre Natal", "Post Natal"])
time_input = st.number_input("Time (weeks for Pre Natal, months for Post Natal)", value=0)
health_condition_input = st.text_input("Health Condition (for mother during Pre Natal or child during Post Natal)")

# Button to generate advice
generate_button = st.button("Get Advice")

if generate_button:
    prompt = f"Create a care plan for a {type.lower()} mother with a {time_label} of {time} and {health_condition_label} of {health_condition}."
    response = arctic.generate(prompt)
    st.write(response)
