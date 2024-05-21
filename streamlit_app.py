import streamlit as st
import os
#from snowflake.arctic import Arctic

# Set up Snowflake Arctic connection secrets
SF_ACCOUNT = st.secrets["SF_ACCOUNT"]
SF_USER = st.secrets["SF_USER"]
SF_PASSWORD = st.secrets["SF_PASSWORD"]
SF_WAREHOUSE = st.secrets["SF_WAREHOUSE"]
SF_DB = st.secrets["SF_DB"]
SF_SCHEMA = st.secrets["SF_SCHEMA"]

# Create an Arctic instance
#arctic = Arctic(account=SF_ACCOUNT, user=SF_USER, password=SF_PASSWORD, warehouse=SF_WAREHOUSE, database=SF_DB, schema=SF_SCHEMA)

# Define the Streamlit app
st.title("Prenatal and Postnatal Care Assistant")

type = st.selectbox("Select Type", ["Pre Natal", "Post Natal"])

if type == "Pre Natal":
    time_label = "Duration of Pregnancy (weeks)"
    health_condition_label = "Mother's Health Condition"
else:
    time_label = "Age of Child (months)"
    health_condition_label = "Child's Health Condition"

time = st.slider(time_label, 0, 40, 20)
health_condition = st.text_input(health_condition_label)

generate_button = st.button("Generate Care Plan")

#if generate_button:
   # prompt = f"Create a care plan for a {type.lower()} mother with a {time_label} of {time} and {health_condition_label} of {health_condition}."
    #response = arctic.generate(prompt)
    #st.write(response)
