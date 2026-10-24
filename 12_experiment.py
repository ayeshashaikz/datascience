"""
Experiment 12: Line and Scatter Plots of Monthly Temperature and Rainfall Data
Dataset: 12.Temprain.csv
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("12.Temprain.csv")
df = df.dropna(subset=["Month", "Year", "tem", "rain"]).copy()
df["Date"] = pd.to_datetime(dict(year=df["Year"].astype(int), month=df["Month"].astype(int), day=1))
df = df.sort_values("Date")

fig, axes = plt.subplots(2, 1, figsize=(11, 8), sharex=True)
axes[0].plot(df["Date"], df["tem"], color="tomato", linewidth=1.2)
axes[0].set_title("Monthly Temperature Over Time")
axes[0].set_ylabel("Temperature")
axes[0].grid(True, alpha=0.3)
axes[1].plot(df["Date"], df["rain"], color="royalblue", linewidth=1.2)
axes[1].set_title("Monthly Rainfall Over Time")
axes[1].set_ylabel("Rainfall")
axes[1].set_xlabel("Date")
axes[1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("12_line_plots.png", dpi=150)
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["tem"], df["rain"], alpha=0.55)
plt.title("Temperature vs Rainfall")
plt.xlabel("Temperature")
plt.ylabel("Rainfall")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("12_scatter_plot.png", dpi=150)
plt.show()

print("Rows plotted:", len(df))
print(df[["tem", "rain"]].describe())
