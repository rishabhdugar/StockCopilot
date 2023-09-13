import streamlit as st
import yfinance as yf
from candlestick import candlestick
import datetime

# Define the ticker symbol
tickerSymbol = 'AAPL'



def app():
    st.markdown("## CandleLight Try - Rishabh")
    
    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    # Get the historical prices for this ticker# Calculate the end date as today
    end = datetime.date.today()

    # Calculate the start date as 15 days before the end date
    start = end - datetime.timedelta(days=15)

    # Download the data
    tickerDf = yf.Ticker(tickerSymbol).history(period='1d', start=start, end=end)

    # Select only the 'Open', 'High', 'Low', 'Close' columns
    
    candles_df_ticker = tickerDf[['Open', 'High', 'Low', 'Close']]
    candles_df_orig = candles_df_ticker.iloc[1:]

    target = 'InvertedHammers'
    candles_df_orig.index = candles_df_orig.index.tz_convert(None)
    candles_df_inverted = candlestick.inverted_hammer(candles_df_orig, target=target)

    # Find all rows where 'InvertedHammers' is True
    true_rows = candles_df_inverted[candles_df_inverted['InvertedHammers'] == True]

    # Initialize an empty list to store the strings
    results = []

    # Iterate over the rows
    for index, row in true_rows.iterrows():
        # Create a string with the date and price and add it to the list
        results.append(f"{target}  formed on Date: {index}, Price: {row['Close']}")

    target = 'HangingMan'
    candles_df_hanging = candlestick.hanging_man(candles_df_orig, target=target)

    # Find all rows where 'InvertedHammers' is True
    true_rows = candles_df_hanging[candles_df_hanging['HangingMan'] == True]

    # Iterate over the rows
    for index, row in true_rows.iterrows():
        # Create a string with the date and price and add it to the list
        results.append(f"{target}  formed on Date: {index}, Price: {row['Close']}")

    # Print the results
    print(results)
    print("final")
    for result in results:
        print(result)

    st.markdown(results)