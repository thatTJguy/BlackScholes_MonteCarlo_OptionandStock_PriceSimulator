from monte_carlo_base import MonteCarloBase
import numpy as np

def run_monte_carlo_stock(S, r, sigma, T, steps, sims, seed=None):
    mc = MonteCarloBase(S, r, sigma, T, steps, sims, seed)
    paths = mc.simulate_paths()
    final = paths[:, -1]
    mean_price = np.mean(final)
    stderr = np.std(final, ddof=1) / np.sqrt(mc.sims)
    return mean_price, stderr