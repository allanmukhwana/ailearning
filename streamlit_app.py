# app.py
import streamlit as st
import pandas as pd
import snowflake.connector
from snowflake.connector import ProgrammingError

# Set up secrets for Snowflake connection
st.secrets["SNOWFLAKE_ACCOUNT"] = "your_account_name"
st.secrets["SNOWFLAKE_USER"] = "your_username"
st.secrets["SNOWFLAKE_PASSWORD"] = "your_password"
st.secrets["SNOWFLAKE_WAREHOUSE"] = "your_warehouse_name"
st.secrets["SNOWFLAKE_DB"] = "your_database_name"
st.secrets["SNOWFLAKE_SCHEMA"] = "your_schema_name"

# Create Snowflake connection
conn = snowflake.connector.connect(
    user=st.secrets["SNOWFLAKE_USER"],
    password=st.secrets["SNOWFLAKE_PASSWORD"],
    account=st.secrets["SNOWFLAKE_ACCOUNT"],
    warehouse=st.secrets["SNOWFLAKE_WAREHOUSE"],
    database=st.secrets["SNOWFLAKE_DB"],
    schema=st.secrets["SNOWFLAKE_SCHEMA"]
)

# Create a cursor object
cur = conn.cursor()

def get_prenatal_care(type, time, health_condition):
    query = """
        SELECT *
        FROM prenatal_care
        WHERE type = %s AND duration_of_pregnancy = %s AND health_condition = %s
    """
    cur.execute(query, (type, time, health_condition))
    results = cur.fetchall()
    return pd.DataFrame(results, columns=["recommendation", "description"])

def get_postnatal_care(type, time, health_condition):
    query = """
        SELECT *
        FROM postnatal_care
        WHERE type = %s AND age_of_child = %s AND health_condition = %s
    """
    cur.execute(query, (type, time, health_condition))
    results = cur.fetchall()
    return pd.DataFrame(results, columns=["recommendation", "description"])

st.title("Prenatal and Postnatal Care Assistant")

type = st.selectbox("Select type", ["Pre Natal", "Post Natal"])
time = st.slider("Duration of pregnancy (weeks) or Age of child (months)", 0, 40)
health_condition = st.text_input("Enter health condition (e.g. diabetes, hypertension)")

if st.button("Get Recommendations"):
    if type == "Pre Natal":
        results = get_prenatal_care(type, time, health_condition)
    else:
        results = get_postnatal_care(type, time, health_condition)
    
    st.write(results)
