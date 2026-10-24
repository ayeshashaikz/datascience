"""
Experiment 4: Total Annual Sales and Percentage Increase Using NumPy Arithmetic Operations
Dataset: 2,4,11Sales.xlsx
"""
import pandas as pd
import numpy as np

df = pd.read_excel("2,4,11Sales.xlsx", sheet_name="Sales")
df["Month_sales"] = pd.to_datetime(df["Month_sales"], errors="coerce")
df["Total"] = pd.to_numeric(df["Total"], errors="coerce")
df = df.dropna(subset=["Month_sales", "Total"]).sort_values("Month_sales")

annual_sales = np.sum(df["Total"].to_numpy(dtype=float))
monthly_sales = df.groupby(df["Month_sales"].dt.to_period("M"))["Total"].sum().sort_index()

print(f"Total annual sales in the supplied dataset: {annual_sales:.2f}")
print("\nMonthly sales totals:")
print(monthly_sales)

if len(monthly_sales) >= 2 and monthly_sales.iloc[0] != 0:
    percentage_change = ((monthly_sales.iloc[-1] - monthly_sales.iloc[0]) /
                         abs(monthly_sales.iloc[0])) * 100
    print(f"\nPercentage change from first recorded month to last recorded month: {percentage_change:.2f}%")
else:
    print("\nPercentage change cannot be calculated: insufficient monthly data or zero starting sales.")
