"""
Experiment 13: Stock Price Variability Analysis from CSV Data
Dataset: 13.ADANIPORTS.csv
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("13.ADANIPORTS.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
df = df.dropna(subset=["Date", "Close"]).sort_values("Date")
df["Daily_Return_%"] = df["Close"].pct_change() * 100

fig, axes = plt.subplots(2, 1, figsize=(11, 8), sharex=True)
axes[0].plot(df["Date"], df["Close"], linewidth=1.1)
axes[0].set_title("Adani Ports Closing Stock Price")
axes[0].set_ylabel("Closing Price")
axes[0].grid(True, alpha=0.3)
axes[1].plot(df["Date"], df["Daily_Return_%"], linewidth=0.8)
axes[1].axhline(0, linewidth=0.8)
axes[1].set_title("Daily Percentage Returns")
axes[1].set_ylabel("Return (%)")
axes[1].set_xlabel("Date")
axes[1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("13_stock_variability.png", dpi=150)
plt.show()

print("Records analysed:", len(df))
print("Closing-price standard deviation:", round(df["Close"].std(), 3))
print("Daily-return standard deviation (%):", round(df["Daily_Return_%"].std(), 3))
print("Minimum close:", round(df["Close"].min(), 2))
print("Maximum close:", round(df["Close"].max(), 2))
