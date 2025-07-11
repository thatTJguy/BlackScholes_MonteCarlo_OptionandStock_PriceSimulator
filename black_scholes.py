#functions

import numpy as np
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