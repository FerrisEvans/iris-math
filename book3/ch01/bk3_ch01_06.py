import numpy as np

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 0, 0],
     [0, 1, 0]]

A_plus_B = [
    [A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))
]

print(A_plus_B)
print(np.array(A) + np.array(B))
print(np.add(A, B))