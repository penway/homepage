import numpy as np
from scipy.spatial.transform import Rotation as R

# Given points P and Q
P = np.array([0, 3, 0])
Q = np.array([1, 0, 2])
degree = 30

# Calculate rotation axis (from P to Q) and normalize
rotation_axis = Q - P
rotation_axis = rotation_axis.astype(float)
rotation_axis /= np.linalg.norm(rotation_axis)

print(rotation_axis)

# Define rotation (30 degrees around the axis)
rotation = R.from_rotvec(np.deg2rad(degree) * rotation_axis)

# Rotation matrix
R_corrected = rotation.as_matrix()

# Homogeneous transformation matrix considering the rotation around line segment PQ
T_corrected = np.eye(4)
T_corrected[:3, :3] = R_corrected

# Translation part of the homogeneous transformation matrix (point P)
T_corrected[:3, 3] = -R_corrected @ P + P

# Resulting transformation matrix, with precision of 3 decimal places
print(np.round(T_corrected, 3))


# check the answer by calculating the new position of Q, which should be [1, 3, 2] the same as the original Q
Q_corrected = T_corrected @ np.append(Q, 1)
print(Q_corrected[:3])
if np.allclose(Q_corrected[:3], Q):
    print('Correct')
else:
    print('Incorrect')


'''

'''