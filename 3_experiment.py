"""
Experiment 3: Average Sale Price of Houses with More Than Four Bedrooms Using NumPy
Dataset: 3_house_prices.csv
"""
import pandas as pd
import numpy as np

df = pd.read_csv("3_house_prices.csv")
eligible = df[df["Bedrooms"] > 4]
prices = eligible["Price_INR"].to_numpy(dtype=float)

print("Houses with more than four bedrooms:")
print(eligible.to_string(index=False))
if prices.size:
    print(f"\nAverage sale price: INR {np.mean(prices):,.2f}")
else:
    print("No houses meet the bedroom condition.")
