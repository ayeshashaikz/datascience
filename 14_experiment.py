"""
Experiment 14: Correlation Between Study Time and Exam Scores with Visualization
Dataset: 14.score_updated.csv
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("14.score_updated.csv")
df["Hours"] = pd.to_numeric(df["Hours"], errors="coerce")
df["Scores"] = pd.to_numeric(df["Scores"], errors="coerce")
df = df.dropna(subset=["Hours", "Scores"])

correlation = df["Hours"].corr(df["Scores"])
slope, intercept = np.polyfit(df["Hours"], df["Scores"], 1)
x = np.linspace(df["Hours"].min(), df["Hours"].max(), 100)

plt.figure(figsize=(8, 5))
plt.scatter(df["Hours"], df["Scores"], alpha=0.7, label="Students")
plt.plot(x, slope*x + intercept, linewidth=2, label="Best-fit line")
plt.title(f"Study Hours vs Exam Scores (r = {correlation:.3f})")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("14_study_score_correlation.png", dpi=150)
plt.show()

print("Number of records:", len(df))
print("Pearson correlation coefficient:", round(correlation, 4))
print("Interpretation:", "positive association" if correlation > 0 else "negative association" if correlation < 0 else "no linear association")
