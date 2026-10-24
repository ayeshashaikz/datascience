"""
Experiment 1: Subject-wise Average Score Analysis Using NumPy Arrays
Dataset: 1_subject_scores.csv
"""
import pandas as pd
import numpy as np

df = pd.read_csv("1_subject_scores.csv")
subjects = df.drop(columns=["Student_ID"])
scores = subjects.to_numpy(dtype=float)

print("Subject-wise average scores:")
for i, subject in enumerate(subjects.columns):
    print(f"{subject}: {np.mean(scores[:, i]):.2f}")

print(f"\nOverall average score: {np.mean(scores):.2f}")
