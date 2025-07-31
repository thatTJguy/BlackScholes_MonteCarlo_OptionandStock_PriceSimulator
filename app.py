import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

from black_scholes import (
    calculate_call_price,
    plot_option_vs_stock,
    plot_option_vs_time,
    plot_option_vs_volatility
)
from monte_carlo_option import run_monte_carlo_option
from monte_carlo_stock import run_monte_carlo_stock
from monte_carlo_base import MonteCarloBase

# --- Plotting function for Black-Scholes ---
def plot_option_vs_stock(S, X, T, r, sigma):
    prices = np.linspace(0.5 * S, 1.5 * S, 100)
    call_prices = [calculate_call_price(price, X, T, r, sigma) for price in prices]

    fig, ax = plt.subplots()
    ax.plot(prices, call_prices, label='Call Option Price')
    ax.axvline(S, color='gray', linestyle='--', label='Current Price')
    ax.set_xlabel('Stock Price')
    ax.set_ylabel('Option Price')
    ax.set_title('Black-Scholes Call Option Price vs. Stock Price')
    ax.legend()
    return fig

# --- App Title ---
st.title("Option and Stock Pricing Simulator")

# --- Model Selection ---
model = st.radio("Select Pricing Model:", ["Black-Scholes", "Monte Carlo"])

# --- Simulation Type Based on Model ---
if model == "Black-Scholes":
    sim_type = "Option Pricing"
else:
    sim_type = st.radio("Simulation Type:", ["Option Pricing", "Stock Forecasting"])

# --- Stock Price Source ---
input_mode = st.radio("Stock Price Source:", ["Yahoo Finance", "Manual Entry"])

if input_mode == "Yahoo Finance":
    ticker = st.text_input("Enter Stock Ticker:", value="NVDA")
    try:
        stock_data = yf.Ticker(ticker)
        S = stock_data.info['currentPrice']
        st.write(f"Current stock price for {ticker}: ${S:.2f}")
    except:
        st.error("Failed to fetch stock data.")
        S = None
else:
    S = st.number_input("Enter Current Stock Price:", value=100.0)

# --- Option-specific Inputs ---
if sim_type == "Option Pricing":
    X = st.number_input("Strike Price", value=55.0)
    option_type = st.radio("Option Type", ["Call", "Put"])
    call = option_type == "Call"
else:
    X = None
    call = None

# --- Shared Inputs ---
T = st.number_input("Time to Expiration (Years)", value=1.0)
r = st.number_input("Risk-Free Interest Rate (Annual)", value=0.05)
sigma = st.number_input("Volatility (in %)", value=20.0) / 100

# --- Monte Carlo Specific Inputs ---
if model == "Monte Carlo":
    steps = st.slider("Steps", 50, 500, 100, step=50)
    sims = st.slider("Simulations", 1000, 20000, 10000, step=1000)
    seed = st.number_input("Random Seed", value=42)
    show_plot = st.checkbox("Plot Sample Simulated Paths?", value=True)
    if show_plot:
        n_plot_paths = st.slider("Number of Paths to Plot", 10, 200, 50)

# --- Run Simulation ---
if S is not None:
    if model == "Black-Scholes" and sim_type == "Option Pricing":
        price = calculate_call_price(S, X, T, r, sigma)
        st.success(f"Black-Scholes Call Option Price: ${price:.2f}")

        if st.checkbox("Show Option Price vs. Stock Price Plot"):
            fig = plot_option_vs_stock(S, X, T, r, sigma)
            st.pyplot(fig)

    elif model == "Monte Carlo":
        if sim_type == "Option Pricing":
            price, stderr = run_monte_carlo_option(S, X, r, sigma, T, steps, sims, seed, call=call)
            st.success(f"Monte Carlo {'Call' if call else 'Put'} Option Price: ${price:.2f}")
            st.info(f"Standard Error: {stderr:.4f}")

            if show_plot:
                mc = MonteCarloBase(S, r, sigma, T, steps, sims, seed)
                paths = mc.simulate_paths()
                fig, ax = plt.subplots(figsize=(10, 4))
                for i in range(min(n_plot_paths, sims)):
                    ax.plot(np.linspace(0, T, steps + 1), paths[i])
                ax.set_title("Monte Carlo Option Price Simulated Paths")
                ax.set_xlabel("Time (Years)")
                ax.set_ylabel("Price")
                st.pyplot(fig)

        elif sim_type == "Stock Forecasting":
            mean_price, stderr = run_monte_carlo_stock(S, r, sigma, T, steps, sims, seed)
            st.success(f"Expected Stock Price at T={T}: ${mean_price:.2f}")
            st.info(f"Standard Error: {stderr:.4f}")

            if show_plot:
                mc = MonteCarloBase(S, r, sigma, T, steps, sims, seed)
                paths = mc.simulate_paths()
                fig, ax = plt.subplots(figsize=(10, 4))
                for i in range(min(n_plot_paths, sims)):
                    ax.plot(np.linspace(0, T, steps + 1), paths[i])
                ax.set_title("Monte Carlo Stock Price Simulated Paths")
                ax.set_xlabel("Time (Years)")
                ax.set_ylabel("Price")
                st.pyplot(fig)
