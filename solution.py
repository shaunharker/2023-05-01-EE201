import numpy as np
from scipy.linalg import solve

# Graph structure
graph = {
    1: [2, 9, 10, 11],
    2: [3, 11],
    3: [4, 11, 12],
    4: [5, 12, 13],
    5: [6, 13],
    6: [7, 13, 14],
    7: [8, 15],
    8: [9, 15],
    9: [10, 14],
    10: [13],
    11: [13, 15],
    12: [13],
    13: [14],
    14: [],
    15: []
}

# Create the A matrix
A = np.zeros((15, 15))

node_count = len(graph)
for node, neighbors in graph.items():
    if node not in [1, 5]:
        A[node - 1, node - 1] += len(neighbors)
        for neighbor in neighbors:
            A[node - 1, neighbor - 1] = -1
            if neighbor not in [1, 5]:
                A[neighbor - 1, neighbor - 1] += 1
                A[neighbor - 1, node - 1] = -1
    elif node in [1, 5]:
        A[node - 1, node - 1] = 1
        for neighbor in neighbors:
            A[neighbor - 1, neighbor - 1] += 1
            A[neighbor - 1, node - 1] = -1
            
# Create the B matrix, where B[n] = V[n + 1] - V[n]
B = np.zeros((15, 1))
B[4] = 1

print(A)
print(B)

# Solve the linear system of equations
V = solve(A, B)

print(V)

# Calculate the effective resistance between nodes 1 and 5
R_effective = 1 / (V[2] + V[3] + V[8])

print("The effective resistance between nodes 1 and 5 is approximately: {:.4f} ohms.".format(R_effective[0]))
