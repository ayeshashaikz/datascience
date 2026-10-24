"""
Experiment 5: Average Fuel Efficiency and Percentage Improvement Between Car Models Using NumPy
Dataset: 5_car_fuel_efficiency.csv
"""
import pandas as pd
import numpy as np

df = pd.read_csv("5_car_fuel_efficiency.csv")
efficiency = df["Fuel_Efficiency_km_per_l"].to_numpy(dtype=float)

print("Car fuel efficiency:")
print(df.to_string(index=False))
print(f"\nAverage fuel efficiency: {np.mean(efficiency):.2f} km/l")

if len(efficiency) >= 2 and efficiency[0] != 0:
    improvement = ((efficiency[-1] - efficiency[0]) / efficiency[0]) * 100
    print(f"Percentage improvement from {df.iloc[0]['Car_Model']} to {df.iloc[-1]['Car_Model']}: {improvement:.2f}%")
