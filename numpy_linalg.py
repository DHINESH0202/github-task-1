import numpy as np

A = np.array([[2, 3],
              [4, 5]])

B = np.array([[1, 2],
              [3, 4]])
result = A @ B
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Multiplication:\n", result)