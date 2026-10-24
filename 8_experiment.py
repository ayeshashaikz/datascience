"""
Experiment 8: Top 5 Best-Selling Products Using Pandas
Dataset: 8_best_selling_products.csv
"""
import pandas as pd

df = pd.read_csv("8_best_selling_products.csv")
top5 = df.sort_values("Units_Sold", ascending=False).head(5)
print("Top 5 best-selling products:")
print(top5.to_string(index=False))
