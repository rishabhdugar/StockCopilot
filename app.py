import streamlit as st
from multipage import MultiPage
from know_company import app as know_company_app
from buy_sell import app as buy_sell_app
from market_senti import app as market_senti_app

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.set_page_config(layout="wide")
app.add_page("Know About Company", know_company_app)
app.add_page("Buy/Sell Recommendation", buy_sell_app)
app.add_page("Market Sentiments", market_senti_app)
# The main app
app.run()