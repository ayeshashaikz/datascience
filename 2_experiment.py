"""
Experiment 2: Average Product Price Calculation Using a NumPy 2D Array
Dataset: 2,4,11Sales.xlsx
"""
import pandas as pd
import numpy as np

df = pd.read_excel("2,4,11Sales.xlsx", sheet_name="Sales")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df = df.dropna(subset=["Price"])

# A 2D array containing product ID and price (the price is the value analysed).
arr = df[["Product_ID", "Price"]].to_numpy(dtype=float)
print("NumPy 2D array [Product_ID, Price]:")
print(arr)
print(f"\nAverage product price: {np.mean(arr[:, 1]):.2f}")

print("\nAverage price by product category:")
print(df.groupby("Product_Name")["Price"].mean().round(2))
