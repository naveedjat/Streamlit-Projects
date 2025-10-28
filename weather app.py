import streamlit as st

import requests
import json
import matplotlib.pyplot as plt



# Add background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("Your background image");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color:black;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Know  Weather ")
city = st.text_input("Enter city name: ")

Url= f"Your api "

r = requests.get(Url)
# print(r.text)
wdic = json.loads(r.text)




try:
    st.write(f"The temperature of  {city} is approximately {wdic['current']['temp_c']} degrees celsius")

except Exception as KeyError:
    print("Sorry")


