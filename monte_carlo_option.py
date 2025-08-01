from monte_carlo_base import MonteCarloBase
import numpy as np

def run_monte_carlo_option(S, X, r, sigma, T, steps, sims, seed=42, call=True):
    np.random.seed(seed)
    dt = T / steps
    # Simulate lognormal paths with Euler discretization
    Z = np.random.standard_normal((sims, steps))
    ST = S * np.exp(np.cumsum((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z, axis=1)[:, -1])

    # Payoffs
    payoffs = np.maximum(ST - X, 0) if call else np.maximum(X - ST, 0)

    price = np.exp(-r * T) * np.mean(payoffs)
    stderr = np.exp(-r * T) * np.std(payoffs) / np.sqrt(sims)
    return price, stderr
