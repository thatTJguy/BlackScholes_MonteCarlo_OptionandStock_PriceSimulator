import numpy as np

#class for the base of Monte Carlo use cases
class MonteCarloBase:
    def __init__(self, S, mu, sigma, T, steps=100, sims = 10000, seed=None):
        
        self.S = S
        self.mu = mu
        self.sigma = sigma
        self.T = T
        self.steps = steps
        self.sims = sims
        if seed is not None:
            np.random.seed(seed)
        self.dt = T / steps

# This function generates simulated paths for the underlying asset price using geometric Brownian motion.
    def simulate_paths(self):
        increments = np.random.normal(
            loc=(self.mu - 0.5 * self.sigma ** 2) * self.dt,
            scale=self.sigma * np.sqrt(self.dt),
            size=(self.sims, self.steps)
        )
        log_paths = np.cumsum(increments, axis=1)
        paths = self.S * np.exp(
            np.hstack([np.zeros(self.sims,1), log_paths]), 
        )
        return paths
    
    # this function calculates mean price and stderror of the simulated paths
    def payoff_stats(self, payoffs, r):
        discounted = np.exp(-r * self.T) * payoffs
        mean_price = np.mean(discounted)
# The parameter ddof stands for “delta degrees of freedom.”
# By default, NumPy uses ddof=0, which computes the population standard deviation:
# σ_population = sqrt( sum((xi – x̄)²) / N )


# When you set ddof=1, the formula becomes the sample standard deviation (Bessel’s correction):
# σ_sample = sqrt( sum((xi – x̄)²) / (N – 1) )


# Here, N is the number of observations (your self.sims).
# Why use ddof=1 in Monte Carlo payoffs
# - You’re estimating the true volatility of the discounted payoffs from a finite simulation.
# - Dividing by N–1 instead of N removes the small bias in the variance estimate, giving an unbiased estimator.
        std_error = np.std(discounted, ddof=1) / np.sqrt(self.sims)
        return mean_price, std_error
