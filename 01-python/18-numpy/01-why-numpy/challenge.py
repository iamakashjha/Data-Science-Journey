import numpy as np

temperatures = np.array([
    32, 35, 31, 29, 36, 34, 30
])

ferenheit_temperatures = (temperatures * 9/5) + 32

print("Temperatures:", temperatures)
print("Fahrenheit Temperatures:", ferenheit_temperatures)
print("Average Temperature:", np.mean(temperatures))
print("Maximum Temperature:", np.max(temperatures))
print("Minimum Temperature:", np.min(temperatures))


prices = np.array([
    100,
    250,
    500,
    750,
    1000
])

price_increase = prices * 1.10

print("Prices:", prices)
print("Price Increase (10%):", price_increase)