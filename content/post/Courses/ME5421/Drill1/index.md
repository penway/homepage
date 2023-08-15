---
title: Robotics Kinematics Drill 1
subtitle: Spatial Descriptions & Homogenous Transformations

summary: Robotics Kinematics
projects: [ME5421]

date: '2023-08-15T00:00:00Z'
lastmod: '2023-08-15T00:00:00Z'

draft: false
featured: false

authors:
- penway

categories:
- Course Notes
---

## Drill 1: Spatial Descriptions & Homogenous Transformations

### Problem 1
Frame B is initially coincident to frame A in Figure1(a). Frame B is then rotated 30 degrees  about the vector described by the directed line segment from P to Q (following the right-hand rule). Determine the position and orientation of the new frame B with respect to frame A. Express your answer in the form of a homogeneous transformation matrix.

![Figure 1](./Figure1.png)

### Solution 1
1. Calculate the rotation matrix using the Rodrigues rotation formula. 
2. Then using a point on the line segment, calculate the translation vector. 
3. Combine the rotation matrix and translation vector into a homogeneous transformation matrix.

{{< math >}}
$$
P = \begin{bmatrix} 0 \\ 3 \\ 0 \end{bmatrix}, \quad Q = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}, \quad \theta = 30^{\circ} \\
k = \frac{Q - P}{\|Q - P\|} \\
so, skew\ matrix\ K = \begin{bmatrix} 0 & -k_z & k_y \\ k_z & 0 & -k_x \\ -k_y & k_x & 0 \end{bmatrix} \\
R = I + \sin(\theta)K + (1 - \cos(\theta))K^2 \\
t = -R \cdot P + P \\
T = \begin{bmatrix} R & t \\ 0 & 1 \end{bmatrix}
$$
{{< /math >}}

```python
import numpy as np
from scipy.spatial.transform import Rotation as R

# Given points P and Q
P = np.array([0, 3, 0])
Q = np.array([1, 0, 2])

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
```