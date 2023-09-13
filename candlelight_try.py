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
    candles_df_orig.index = candles_df_orig.index.tz_convert(None)
    
    # List of targets
    targets = ['InvertedHammers', 'HangingMan']

    # Initialize an empty list to store the results
    results = []

    # Dictionary of functions
    functions = {
        'InvertedHammers': candlestick.inverted_hammer,
        'HangingMan': candlestick.hanging_man
        # Add more functions here
    }

    # Iterate over the targets
    for target in targets:
        # Apply the function to the dataframe
        candles_df_target = functions[target](candles_df_orig, target=target)

        # Find all rows where the target is True
        true_rows = candles_df_target[candles_df_target[target] == True]

        # Iterate over the rows
        for index, row in true_rows.iterrows():
            # Create a string with the date and price and add it to the list
            results.append(f"{target} formed on Date: {index}, Price: {row['Close']}")

    # Print the results
    for result in results:
        print(result)

    st.markdown(results)