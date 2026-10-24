"""
Experiment 11: Line, Scatter and Bar Plots of Monthly Product Sales Using Matplotlib
Dataset: 2,4,11Sales.xlsx
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("2,4,11Sales.xlsx", sheet_name="Sales")
df["Month_sales"] = pd.to_datetime(df["Month_sales"], errors="coerce")
df["Total"] = pd.to_numeric(df["Total"], errors="coerce")
df = df.dropna(subset=["Month_sales", "Total"])

monthly = (df.groupby(df["Month_sales"].dt.to_period("M"))["Total"]
             .sum().sort_index().reset_index())
monthly["Month_sales"] = monthly["Month_sales"].astype(str)

fig, axes = plt.subplots(3, 1, figsize=(10, 12))
axes[0].plot(monthly["Month_sales"], monthly["Total"], marker="o")
axes[0].set_title("Monthly Product Sales — Line Plot")
axes[0].set_ylabel("Total Sales")
axes[0].tick_params(axis="x", rotation=35)
axes[0].grid(True, alpha=0.3)

axes[1].scatter(monthly["Month_sales"], monthly["Total"], alpha=0.75)
axes[1].set_title("Monthly Product Sales — Scatter Plot")
axes[1].set_ylabel("Total Sales")
axes[1].tick_params(axis="x", rotation=35)
axes[1].grid(True, alpha=0.3)

axes[2].bar(monthly["Month_sales"], monthly["Total"])
axes[2].set_title("Monthly Product Sales — Bar Plot")
axes[2].set_xlabel("Month")
axes[2].set_ylabel("Total Sales")
axes[2].tick_params(axis="x", rotation=35)
axes[2].grid(True, axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("11_monthly_sales_plots.png", dpi=150)
plt.show()

print("Monthly totals:")
print(monthly.to_string(index=False))
