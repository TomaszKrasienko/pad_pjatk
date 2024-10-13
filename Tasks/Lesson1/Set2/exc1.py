import pandas as pd
import numpy as np

data = pd.read_csv('Data/president_heights.csv')
heights = np.array(data['height(cm)'])

mean = np.mean(heights)
print(f"Średnia: {mean}")

std_dev = np.std(heights)
print(f"Odchylenie standardowe: {std_dev}")

min_value = np.min(heights)
print(f"Minimum: {min_value}")

max_value = np.max(heights)
print(f"Maksimum: {max_value}")

quantile_25 = np.percentile(heights, 25)
print(f"25. kwantyl: {quantile_25}")

quantile_75 = np.percentile(heights, 75)
print(f"75. kwantyl: {quantile_75}")

median = np.median(heights)
print(f"Mediana: {median}")