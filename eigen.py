import numpy as np

A = np.array([[4, -2],
              [1, 1]])

eigen_values, eigen_vectors = np.linalg.eig(A)

print("Matrix A:\n", A)
print("Eigen Values:\n", eigen_values)
print("Eigen Vectors:\n", eigen_vectors)