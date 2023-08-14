import numpy as np
from scipy.spatial.transform import Rotation as R

# Given points P and Q
P = np.array([0, 1, 0])
Q = np.array([1, 3, 2])

# Calculate rotation axis (from P to Q) and normalize
rotation_axis = Q - P
rotation_axis = rotation_axis.astype(float)
rotation_axis /= np.linalg.norm(rotation_axis)

# Define rotation (30 degrees around the axis)
rotation = R.from_rotvec(30 * np.pi / 180 * rotation_axis)

# Rotation matrix
R_corrected = rotation.as_matrix()

# Homogeneous transformation matrix considering the rotation around line segment PQ
T_corrected = np.eye(4)
T_corrected[:3, :3] = R_corrected

# Translation part of the homogeneous transformation matrix (point P)
T_corrected[:3, 3] = -R_corrected @ P + P

# Resulting transformation matrix
print(T_corrected)


# check the answer by calculating the new position of Q, which should be [1, 3, 2] the same as the original Q
Q_corrected = T_corrected @ np.append(Q, 1)
print(Q_corrected[:3])
if np.allclose(Q_corrected[:3], Q):
    print('Correct')
else:
    print('Incorrect')


'''
$$
PQ = Q - P = \begin{bmatrix}1 \\ 3 \\ 2\end{bmatrix} - \begin{bmatrix}0 \\ 1 \\ 0\end{bmatrix} = \begin{bmatrix}1 \\ 2 \\ 2\end{bmatrix} = \begin{bmatrix}{1}/{3} \\ {2}/{3} \\ {2}/{3}\end{bmatrix} \\

\theta = 30^{\circ} = \frac{\pi}{6} \text{ rad} \\

K = \begin{bmatrix}
0 & -{2}/{3} & 2/3 \\
{2}/{3} & 0 & -{1}/{3} \\
-{2}/{3} & {1}/{3} & 0
\end{bmatrix} \\
R = I + \sin(\theta)K + (1 - \cos(\theta))K^2 \\

let\ T = \begin{bmatrix}
R & t \\
0 & 1
\end{bmatrix} \\

t = -RP + P \\

T = \begin{bmatrix}
R & -RP + P \\
0 & 1
\end{bmatrix}
$$
'''