#functions
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#sigma squared by ** keep that in your head
def calculate_d1(S, X, T, r, sigma):
    return (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

def calculate_d2(d1, sigma, T):
    return d1 - sigma * np.sqrt(T)

def calculate_call_price(S, X, T, r, sigma):
    d1 = calculate_d1(S, X, T, r, sigma)
    d2 = calculate_d2(d1, sigma, T)
    call_price = (S * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2))
    return call_price

def calculate_put_price(S, X, T, r, sigma):
    d1 = calculate_d1(S, X, T, r, sigma)
    d2 = calculate_d2(d1, sigma, T)
    put_price = (X * np.exp(-r * T) * norm.cdf(-d2)) - (S * norm.cdf(-d1))
    return put_price

def plot_option_vs_stock(S, X, T, r, sigma):
    prices = np.linspace(0.5 * S, 1.5 * S, 100)
    call_prices = [calculate_call_price(p, X, T, r, sigma) for p in prices]
    fig, ax = plt.subplots()
    ax.plot(prices, call_prices)
    ax.axvline(S, color='gray', linestyle='--', label='Current Price')
    ax.set_xlabel("Stock Price")
    ax.set_ylabel("Call Option Price")
    ax.set_title("Option Price vs. Stock Price")
    ax.legend()
    return fig

def plot_option_vs_time(S, X, r, sigma):
    T_range = np.linspace(0.01, 2.0, 100)
    prices = [calculate_call_price(S, X, t, r, sigma) for t in T_range]
    fig, ax = plt.subplots()
    ax.plot(T_range, prices)
    ax.set_xlabel("Time to Expiration (Years)")
    ax.set_ylabel("Call Option Price")
    ax.set_title("Option Price vs. Time to Expiration")
    return fig

def plot_option_vs_volatility(S, X, T, r):
    vol_range = np.linspace(0.01, 1.0, 100)
    prices = [calculate_call_price(S, X, T, r, vol) for vol in vol_range]
    fig, ax = plt.subplots()
    ax.plot(vol_range * 100, prices)
    ax.set_xlabel("Volatility (%)")
    ax.set_ylabel("Call Option Price")
    ax.set_title("Option Price vs. Volatility")
    return fig