import streamlit as st
import yfinance as yf
from candlestick import candlestick
import datetime
from openai import *

# Define the ticker symbol
tickerSymbol = 'SPOT'



def app():
    st.markdown("## CandleLight Try - Rishabh")
    
    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    # Get the historical prices for this ticker# Calculate the end date as today
    end = datetime.date.today()

    # Calculate the start date as 15 days before the end date
    start = end - datetime.timedelta(days=15)

    # Download the data
    # tickerDf = yf.Ticker(tickerSymbol).history(period='1d', start=start, end=end)
    
    tickerDf = yf.Ticker(tickerSymbol).history(period='1d', start='2023-06-10', end='2023-07-10')

    # Select only the 'Open', 'High', 'Low', 'Close' columns
    
    candles_df_ticker = tickerDf[['Open', 'High', 'Low', 'Close']]
    candles_df_orig = candles_df_ticker.iloc[1:]
    candles_df_orig.index = candles_df_orig.index.tz_convert(None)
    
    # List of targets
    targets = ['InvertedHammers', 'HangingMan', 'ShootingStar', 'Doji', 'RainDropDoji', 'BearishHarami', 'BullishHarami', 'GravestoneDoji', 'Star', 'RainDrop', 'PiercingPattern', 'MorningStarDoji', 'MorningStar', 'Hammer', 'BullishEngulfing', 'BearishEngulfing', 'DragonflyDoji', 'DojiStar', 'Doji', 'DarkCloudCover']

    # Initialize an empty list to store the results
    results = []

    # Dictionary of functions
    functions = {
        'InvertedHammers': candlestick.inverted_hammer,
        'HangingMan': candlestick.hanging_man,
        'ShootingStar': candlestick.shooting_star,
        'Doji': candlestick.doji,
        'RainDropDoji': candlestick.rain_drop_doji,
        'BearishHarami': candlestick.bearish_harami,
        'BullishHarami': candlestick.bullish_harami,
        'GravestoneDoji': candlestick.gravestone_doji,
        'Star': candlestick.star,
        'RainDrop': candlestick.rain_drop,
        'PiercingPattern': candlestick.piercing_pattern,
        'MorningStarDoji': candlestick.morning_star_doji,
        'MorningStar': candlestick.morning_star,
        'Hammer': candlestick.hammer,
        'BullishEngulfing': candlestick.bullish_engulfing,
        'BearishEngulfing': candlestick.bearish_engulfing,
        'DragonflyDoji': candlestick.dragonfly_doji,
        'DojiStar': candlestick.doji_star,
        'Doji': candlestick.doji,
        'DarkCloudCover': candlestick.dark_cloud_cover,
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

    st.write(
            chat_completion(
                f"You are a Stock assistant. This is some technical analysis on {tickerSymbol}: {results}",
                f"Categories into bullish / bearish /uncertain patterns for {tickerSymbol}",
            )
        )

    