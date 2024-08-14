import numpy as np

A = np.array([
   [1, -2, 1],
   [0, 2, -8],
   [-4, 5, 9] 
])

b = np.array([0, 8,-9])

solution = np.linalg.solve(A,b)

print("Solution:")
print("X1 = {solution[0]}")
print("X2 = {solution[1]}")
print("X3 = {solution[2]}")

print("Verification:")
for i, equation in enumerate(A):
   result = np.dot(equation, solution)
   print("Equation {i+1}: {result} = {b[i]}")