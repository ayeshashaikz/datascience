"""
Experiment 10: Line Plot and Bar Plot of Monthly Sales Data Using Matplotlib
Dataset: 10_monthly_sales.csv
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("10_monthly_sales.csv")
plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["Sales_INR"], marker="o")
plt.title("Monthly Sales — Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales (INR)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("10_monthly_sales_line.png", dpi=150)
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(df["Month"], df["Sales_INR"])
plt.title("Monthly Sales — Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales (INR)")
plt.tight_layout()
plt.savefig("10_monthly_sales_bar.png", dpi=150)
plt.show()

print("Monthly sales data:")
print(df.to_string(index=False))
print(f"\nTotal annual sales: INR {df['Sales_INR'].sum():,.2f}")
print(f"Average monthly sales: INR {df['Sales_INR'].mean():,.2f}")
