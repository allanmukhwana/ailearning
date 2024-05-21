# app.py
import streamlit as st
import os
import openai

# Set up OpenAI API connection using Streamlit secrets
openai_api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = openai_api_key

# Define the app layout
st.title("Prenatal and Postnatal Care Assistant")
st.write("Get personalized advice and guidance for a healthy pregnancy and parenthood journey.")

# Input fields
type_input = st.selectbox("Type", ["Pre Natal", "Post Natal"])
time_input = st.number_input("Time (weeks for Pre Natal, months for Post Natal)", value=0)
health_condition_input = st.text_input("Health Condition (for mother during Pre Natal or child during Post Natal)")

# Button to generate advice
generate_button = st.button("Get Advice")

# Function to generate advice using GPT-4
def generate_advice(type, time, health_condition):
    prompt = f"Provide personalized advice and guidance for a {type} mother with a {time} {'' if type == 'Pre Natal' else 'onth old'} {'' if type == 'Pre Natal' else 'child'} who has a {health_condition}."
    response = openai.chat.completions.create(
         model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": prompt
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
    )

   return response.choices[0].message.content

# Display generated advice
if generate_button:
    advice = generate_advice(type_input, time_input, health_condition_input)
    st.write(advice)
