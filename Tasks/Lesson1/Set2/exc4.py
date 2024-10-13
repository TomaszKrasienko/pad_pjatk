import numpy as np

A = [0,3,2,5]
B = [0,3,1,4]

numpy_add = np.add(A,B)
print(f"Result - adding A and B: {numpy_add}")

numpy_subtract = np.subtract(A,B)
print(f"Result - Subtracting B from A: {numpy_subtract}")

scalar_a = 4
numpy_A_4_multiply = np.multiply(A,scalar_a)
print(f"Result - Multiplying vector A by scalar a=4: {numpy_A_4_multiply}")

scalar_A_B = np.dot(A,B)
print(f"Result - The dot product of A and B: {scalar_A_B}")

length_b = np.linalg.norm(B)
print(f"Result - The length of vector B is space: {length_b}")