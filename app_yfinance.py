import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""

### Stock Price App

Shown are the stock **closing price** and ***volume*** of Google.

""") # write the intro text

tickerSymbol = 'GOOGL' # Google stock 

tickerData = yf.Ticker(tickerSymbol) # get the data

tickerDF = tickerData.history(period='1d', start='2020-01-01', end='2020-04-01') # get the dataframe

st.line_chart(tickerDF.Close) # plot the closing price
st.line_chart(tickerDF.Volume) # plot the volume