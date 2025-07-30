import streamlit as st
import yfinance as yf
from black_scholes import calculate_call_price

st.title("Black-Scholes Option Pricing Calculator")

# give user option for price data source
input_mode = st.radio("Select Source of Stock Price Data:", ["Yahoo Finance", "Manual Entry"])


#User adds ticker symbol
if input_mode == "Yahoo Finance":
    ticker = st.text_input("Enter the stock ticker symbol (e.g., AAPL, MSFT, NVDA):", value = "NVDA")

# get stock data
    try:
        stock_data = yf.Ticker(ticker)
        stock_info = stock_data.info
        S = stock_info['currentPrice']
        st.write(f"Current stock price for {ticker}: ${S:.2f}")
    except Exception as e:
        st.error("Error Fetching stock data. Please check the ticker symbol and try again.")
        S = None

else:
    S = st.number_input("Enter the current stock price:", value=100.00)

# User inputs for option parameters

X = st.number_input ("Strike Price", value = 55.00)
T = st.number_input ("Time to Expiration (in years)", value = 1.0)
r = st.number_input ("Risk-Free Interest Rate", value = 0.05)
sigma = st.number_input ("Volatility (in %)", value = 20.0)

if S is not None:
    # Calculate the call option price
    price = calculate_call_price(S, X, T, r, sigma / 100)
    st.write(f"The call option price is: ${price:.2f}")