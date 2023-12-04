import numpy as np

# coding: utf-8
X = np.column_stack([np.ones(12), np.random.randint(24, 36, 12), np.random.randint(60, 83, 12)])
print(X)
Y = np.random.uniform(13.5, 18.6, (12, 1))
print(Y)
A = np.linalg.inv(X.T @ X) @ X.T @ Y
print("Вектор А: ")
print(A)
Y_pr = A[0] + A[1] * X[:, 1] + A[2] * X[:, 2]
print("Вектор до: ")
print(Y)
print("Вектор после: ")
print(Y_pr)
