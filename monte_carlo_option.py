from monte_carlo_base import MonteCarloBase
import numpy as np

def run_monte_carlo_option(S, K, r, sigma, T, steps, sims, seed=None, call=True):
    mc = MonteCarloBase(S, r, sigma, T, steps, sims, seed)
    paths = mc.simulate_paths()
    final = paths[:, -1]
    payoffs = np.maximum(final - K, 0) if call else np.maximum(K - final, 0)
    return mc.payoff_statistics(payoffs, r)