import pytest
from black_scholes import calculate_call_price

@pytest.mark.math
#Arrange
@pytest.mark.parametrize("S, X, T, r, sigma, expected", [
    (100.0, 95.0, 1.0, 0.05, 0.2, 13.35),  # Example case
    (50.0, 50.0, 0.5, 0.03, 0.25, 3.89),   # even with same strike price, different time and volatility
    (100.0, 105.0, 2.0, 0.04, 0.15, 9.94) # below strike price
])
def test_call_price(S, X, T, r, sigma, expected):
    # Act
    price = calculate_call_price(S, X, T, r, sigma)
    # Assert
    assert round(price, 2) == pytest.approx(expected, abs=.02)