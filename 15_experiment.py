"""
Experiment 15: Temperature Variability Analysis for Different Cities
Dataset: 15.weather.csv
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("15.weather.csv")
df["AvgTemperature"] = pd.to_numeric(df["AvgTemperature"], errors="coerce")
df = df.dropna(subset=["City", "AvgTemperature"]).copy()

# Select up to 8 cities with the most observations so the plot remains readable.
city_counts = df["City"].value_counts()
selected_cities = city_counts.head(8).index
city_df = df[df["City"].isin(selected_cities)]

plt.figure(figsize=(11, 6))
city_df.boxplot(column="AvgTemperature", by="City", rot=35, grid=False)
plt.title("Temperature Variability Across Cities")
plt.suptitle("")
plt.xlabel("City")
plt.ylabel("Average Temperature (dataset units)")
plt.tight_layout()
plt.savefig("15_city_temperature_boxplot.png", dpi=150)
plt.show()

stats = city_df.groupby("City")["AvgTemperature"].agg(["count", "mean", "std", "min", "max"])
print("Cities plotted:", ", ".join(selected_cities))
print(stats.round(2))
print("\\nNote: only the 8 cities with the most records are plotted.")
