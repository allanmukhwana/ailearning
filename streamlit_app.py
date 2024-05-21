import streamlit as st
from arctic_helper import conn
import pandas as pd

st.title("Pre and Post Natal Care Advice")
type_input = st.selectbox("Select Type", ["Pre Natal", "Post Natal"])
time_input = st.number_input("Enter Time (Duration of Pregnancy for Prenatal or Age of Child for Post Natal)", min_value=0)
health_condition = st.text_input("Enter Health Condition (Condition for mother during prenatal or condition of child for Post Natal)")
if type_input == "Pre Natal":
    query = f"SELECT advice FROM pre_natal WHERE duration={time_input} AND mother_condition='{health_condition}'"
else:
    query = f"SELECT advice FROM post_natal WHERE age={time_input} AND child_condition='{health_condition}'"
cursor = conn.cursor()
cursor.execute(query)
result = cursor.fetchone()[0]
st.write(result)
