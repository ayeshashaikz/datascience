"""
Experiment 7: Customer Order Analysis Using Pandas DataFrame
Dataset: 7_customer_orders.csv
"""
import pandas as pd

df = pd.read_csv("7_customer_orders.csv", parse_dates=["Order_Date"])
df["Line_Total_INR"] = df["Quantity"] * df["Unit_Price_INR"]

print("Customer order data:")
print(df.to_string(index=False))
print("\nTotal order value by customer:")
print(df.groupby("Customer")["Line_Total_INR"].sum().sort_values(ascending=False))
print("\nQuantity sold by product:")
print(df.groupby("Product")["Quantity"].sum().sort_values(ascending=False))
print("\nTotal revenue: INR", f"{df['Line_Total_INR'].sum():,.2f}")
