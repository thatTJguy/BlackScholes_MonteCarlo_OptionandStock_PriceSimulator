# 📈 Black-Scholes & Monte Carlo Option and Stock Price Simulator

A Streamlit web app for pricing and visualizing **European options** and **stock forecasts** using:

* **Black-Scholes Model** (analytical pricing for calls and puts)
* **Monte Carlo Simulation** (multi-step stochastic modeling)

---

## 📌 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🚀 Features

* ✅ Black-Scholes pricing for European call and put options
* ✅ Monte Carlo simulations for both stock and option prices
* ✅ Visualization of **stock price paths** and **option price simulations**
* ✅ Sensitivity plots for option prices vs. stock price, time, and volatility
* ✅ Live stock price fetching from Yahoo Finance
* ✅ User-adjustable parameters including volatility, time to expiration, strike price, and random seed
* ✅ Reproducible simulations through seed control
* ✅ Open-source with MIT License

---

## 📦 Installation

```bash
git clone https://github.com/thatTJguy/BlackScholes_MonteCarlo_OptionandStock_PriceSimulator.git
cd BlackScholes_MonteCarlo_OptionandStock_PriceSimulator
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open the provided URL (e.g., [http://localhost:8501](http://localhost:8501)) to use the interface.

---

## 🧪 Testing

Current tests include:

* ✅ Black-Scholes call price calculation

Planned tests:

* 🔄 Black-Scholes put price calculation
* 🔄 Monte Carlo option price convergence
* 🔄 Monte Carlo path discretization accuracy

Run tests with:

```bash
pytest
```

---

## 📊 How It Works

### Model Behavior

* **Black-Scholes**: Uses closed-form formulas for European call and put pricing.
* **Monte Carlo**: Simulates asset paths under Geometric Brownian Motion (GBM), calculates option payoffs, and discounts to present.

### User Input Parameters

Users configure the models by specifying:

* **Stock Price (S)**: Current underlying asset price (from Yahoo Finance or manual entry).
* **Strike Price (X)**: Option strike price.
* **Time to Expiration (T)**: Time remaining until option maturity (in years).
* **Risk-Free Rate (r)**: Annualized risk-free interest rate.
* **Volatility (σ)**: Annualized volatility of the underlying asset.
* **Random Seed**: Ensures reproducible Monte Carlo results by controlling the random number generator.
* **Steps (Monte Carlo only)**: Number of time intervals per simulated path. More steps create smoother, more accurate simulations.
* **Simulations (Monte Carlo only)**: Number of simulated paths to generate.

### Outputs

* **Option Price**: Estimated price of the option under the selected model. For Monte Carlo, it is the average discounted payoff across simulated paths. For Black-Scholes, it is the analytical formula result.
* **Standard Error (Monte Carlo only)**: Quantifies uncertainty in the simulation estimate. Smaller values indicate more precise estimates, typically improving with more simulations.

### Role of Standard Deviation

In Monte Carlo, the **standard deviation** of simulated option payoffs is used to calculate the standard error. It measures how much individual simulated outcomes vary around the mean price. The standard error is derived by dividing this standard deviation by the square root of the number of simulations.
