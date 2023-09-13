import streamlit as st
import yfinance as yf
from candlestick import candlestick

# Define the ticker symbol
tickerSymbol = 'AAPL'



def app():
    st.markdown("## CandleLight Try - Rishabh")
    
    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2023-1-1', end='2023-09-12')

    # Select only the 'Open', 'High', 'Low', 'Close' columns
    
    print(tickerDf)
    candles_df = tickerDf[['Open', 'High', 'Low', 'Close']]
    candles_df = candles_df.iloc[1:]

    # Print the first 4 rows
    st.markdown(candles_df.head(4))
    
    target = 'InvertedHammers'
    candles_df = candlestick.inverted_hammer(candles_df, target=target)
    st.markdown(candles_df)