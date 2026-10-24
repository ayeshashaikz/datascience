"""
Experiment 9: Property Data Analysis Using Pandas DataFrame
Dataset: 9_property_data.csv
"""
import pandas as pd

df = pd.read_csv("9_property_data.csv")
print("Property dataset preview:")
print(df.head().to_string(index=False))
print("\nSummary statistics:")
print(df[["Bedrooms", "Area_sqft", "Price_INR"]].describe().round(2))
print("\nAverage property price by city:")
print(df.groupby("City")["Price_INR"].mean().sort_values(ascending=False).map(lambda x: f"INR {x:,.2f}"))
print("\nProperties with 3 or more bedrooms:")
print(df[df["Bedrooms"] >= 3].to_string(index=False))
