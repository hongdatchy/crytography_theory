import numpy as np

A = np.array([
    [12, 0, 19],
    [12, 0, 7],
    [14, 0, 25]
])
K = np.array([
    [0, 11, 15],
    [7, 0, 1],
    [4, 19 ,0]
])
invOfK = np.array([
    [-19*19, 285*19, 11*19],
    [4*19, -60*19, 105*19],
    [133*19, 44*19 ,-77*19]
])
# C = np.mod(A.dot(K), 26)
# print(C)
# print(np.mod(C.dot(invOfK),26))
print(np.linalg.det(K))