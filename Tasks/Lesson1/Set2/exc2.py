import pandas as pd
import numpy as np

data_task2 = pd.read_csv('Data/Zadanie_2.csv', delimiter=';', header=None)

eig = np.linalg.eig(data_task2)
print(f"Eig0: {eig[0]}")
print(f"Eig1: {eig[1]}")