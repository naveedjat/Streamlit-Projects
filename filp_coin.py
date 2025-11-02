import streamlit as st
import requests
import random

coins = ['http://re-bol.com/heads.jpg', 'http://re-bol.com/tails.jpg']

# Flip coin when button is pressed
if st.button('Flip'):
    coin = random.choice(coins)
    st.image(coin)

