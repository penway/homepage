# import numpy as np
# Q = np.array([1, 3, 2])
# P = np.array([0, 1, 0])
# theta = np.pi/6


# PQ = Q - P
# print("PQ:", PQ)
# PQ = PQ / np.linalg.norm(PQ)
# print("PQ, normalized", PQ)

# K = np.array([
#     [0, -PQ[2], PQ[1]],
#     [PQ[2], 0, -PQ[0]],
#     [-PQ[1], PQ[0], 0]
#     ])
# print("K:", K)

# I = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])


# R = I + np.sin(theta)*K + (1-np.cos(theta))*np.matmul(K, K)
# print("R:", R)

# # make R into homogeneous matrix
# R = np.pad(R, ((0, 1), (0, 1)), 'constant')
# R[3, 3] = 1
# print("RT:", R)

# '''
# T_A^P = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \\

# T_{B'}^B = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \\
# '''
# T_AP = np.array([
#     [1, 0, 0, 0], 
#     [0, 1, 0, 1], 
#     [0, 0, 1, 0], 
#     [0, 0, 0, 1]]
#     )
# T_BpB = np.array([
#     [1, 0, 0, 0],
#     [0, 1, 0, -1],
#     [0, 0, 1, 0],
#     [0, 0, 0, 1]]
#     )

# '''
# T_A^B = T_A^P \cdot R_{A'}^{B'} \cdot T_{B'}^B \\
# '''
# T_AB = np.matmul(np.matmul(T_BpB, R), T_AP)
# print(T_AB)

# '''

# '''

import numpy as np
T = np.array([
 [ 0.88091147, -0.3035612,   0.36310547,  0.3035612 ],
 [ 0.36310547,  0.92556967, -0.1071224,   0.07443033],
 [-0.3035612,   0.22621093,  0.92556967, -0.22621093],
 [ 0.,          0.,          0.,          1.        ]])
T = np.array([
    [0.876, 0.296, 0.382, 0.888],
    [0.239, 0.952, 0.191, 0.144],
    [0.42,  0.0762, 0.904, 0.229],
    [0, 0, 0, 1]
])

# P is point (0, 1, 0)
P = np.array([0, 1, 0, 1])
# Q is point (1, 3, 2)
Q = np.array([1, 3, 2, 1])

trans_P = np.matmul(T, P)
print(trans_P)
trans_Q = np.matmul(T, Q)
print(trans_Q)