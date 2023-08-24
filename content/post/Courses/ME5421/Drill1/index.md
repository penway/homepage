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

{{% toc %}}

## Drill 1: Spatial Descriptions & Homogenous Transformations

### Problem 1
Frame B is initially coincident to frame A in Figure1(a). Frame B is then rotated 30 degrees  about the vector described by the directed line segment from P to Q (following the right-hand rule). Determine the position and orientation of the new frame B with respect to frame A. Express your answer in the form of a homogeneous transformation matrix.

![Figure 1](./Figure1.png)

#### Solution1_1
1. Calculate the rotation matrix using the Rodrigues rotation formula. 
2. Then using a point on the line segment, calculate the translation vector. 
3. Combine the rotation matrix and translation vector into a homogeneous transformation matrix.

{{< math >}}
$$
\begin{align}
P &= \begin{bmatrix} 0 \\ 3 \\ 0 \end{bmatrix}, \quad Q = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}, \quad \theta = 30^{\circ} \\

k &= \frac{Q - P}{\|Q - P\|} \\

so, skew\ matrix\ K &= \begin{bmatrix} 0 & -k_z & k_y \\ k_z & 0 & -k_x \\ -k_y & k_x & 0 \end{bmatrix} \\

R &= I + \sin(\theta)K + (1 - \cos(\theta))K^2 \\

t &= -R \cdot P + P \\

T &= \begin{bmatrix} R & t \\ 0 & 1 \end{bmatrix}
\end{align}
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

### Solution1_2

{{< math >}}
$$
\begin{align}
^AT_{B_1} &= ^AT_C\ ^CRot(z, 30^{\circ})\ ^CT_A\ ^CT_{B_0}\\
^AT_C &= \begin{bmatrix}
^AR_C & ^AP_C \\
0 & 1
\end{bmatrix} \\

^AR_C &= \begin{bmatrix}
^Ax_C & ^Ay_C & ^APQ
\end{bmatrix} \\

^APQ &= (P - Q) / \|P - Q\| \\

^AxC &= \ ^APQ \times \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \\

^Ay_C &= \ ^APQ \times \ ^Ax_C \\
\end{align}
$$
{{< /math >}}

```python
'''
Frame B rotate around PQ
Need ATB
'''

import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ATB0 = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])

P = np.array([0, 3, 0])
Q = np.array([1, 0, 2])

theta = 30

# formula: ATB1 = ATC * C_Rot(z, 30) * CTA * ATB0

AzC = Q - P
AzC = AzC / np.linalg.norm(AzC)
AxC = np.cross(AzC, np.array([0, 0, 1]))
AxC = AxC / np.linalg.norm(AxC)
AyC = np.cross(AzC, AxC)
AyC = AyC / np.linalg.norm(AyC)

ATC = np.array([[AxC[0], AyC[0], AzC[0], P[0]],
                [AxC[1], AyC[1], AzC[1], P[1]],
                [AxC[2], AyC[2], AzC[2], P[2]],
                [0, 0, 0, 1]])

CTA = np.linalg.inv(ATC)

C_Rot = np.array([[math.cos(math.radians(theta)), -math.sin(math.radians(theta)), 0, 0],
                    [math.sin(math.radians(theta)), math.cos(math.radians(theta)), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

ATB1 = np.dot(np.dot(np.dot(ATC, C_Rot), CTA), ATB0)

# limit the number of digits to 3
np.set_printoptions(precision=3)
print(ATB1)
```

