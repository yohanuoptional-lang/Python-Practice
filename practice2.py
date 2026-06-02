import numpy as np

np.set_printoptions(precision=3, suppress=True)

a = np.array([[1, 2], [3, 4]])
print(a)

b = np.array([[5, 6], [7, 8]])
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)