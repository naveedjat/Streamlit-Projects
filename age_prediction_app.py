import streamlit as st
import requests

# Age guessing using  agify api
st.header('Guess Age From Name')
name=st.text_input('Your Name')
if name:
     r=requests.get(f'Your api from agify').json()
     st.write(f'Your age is predicted to be {r ["age"]}')

