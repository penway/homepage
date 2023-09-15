---
title: Robotics Kinematics Lesson 3
subtitle: Notes for ME5421

# Summary for listings and search engines
summary: Robotics Kinematics

# Link this post with a project
projects: [ME5421]

# Date published
date: '2023-09-12T00:00:00Z'

# Date updated
lastmod: '2023-09-12T00:00:00Z'

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: 'Image credit: [**Unsplash**](./featured.jpg)'
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- penway

tags:
- 

categories:
- Course Notes

gallery_item:
- album: 
  image:
  caption:

share: false
---

## TL;DR
- [ ] Homogeneous Transformation Matrix
- [ ] Jacobian Matrix
- [ ] Two transformation: Change of the reference (chaned base) and change of the expression (changed tool)

## Velocity Representation

### Translational Velocity

Speed of B relative to A and expressed in frame A. A is also called frame of differentiation.
{{< math >}}
$$
\begin{aligned}
{}^Au_B = \frac{d}{dt} {}^AP_B &= lim_{\Delta t \to 0} \frac{{}^AP_B(t+\Delta t) - {}^AP_B(t)}{\Delta t}
\end{aligned}
$$
{{< /math >}}

Speed of B relative to A and expressed in frame W. W is also called frame of expression.
{{< math >}}
$$
{}^W_Au_B = {}^WR_A \cdot {}^Au_B
$$
{{< /math >}}
As u is a vector, it can be expressed in any frame. We need this notation is because sometimes we need to add two vectors together, and they are expressed in different frames.

> The below formula shows that how Point C relative with B expressed in A is calculated.
{{< math >}}
$$
\begin{align}
{}^B_AP_C &= {}^AR_B \cdot {}^B_BP_C \\
{}^AP_C &= {}^AP_B + {}^AR_C \cdot {}^BP_C
\end{align}
$$
{{< /math >}}

### Rotational Velocity
{{< math >}}
Define: Rotational axis: k, then the rotational velocity is
$$
\omega = \begin{bmatrix} \omega_x \\ \omega_y \\ \omega_z \end{bmatrix}
= \begin{bmatrix} k_x \\ k_y \\ k_z \end{bmatrix} \dot{\theta}
$$
But, we want to express it as $\dot{R}$, so we need to get $\dot{X}, \dot{Y}, \dot{Z}$.
$$
\begin{aligned}
\dot{X} &= \omega \times X = \hat{\omega} X \\
\dot{Y} &= \omega \times Y = \hat{\omega} Y \\
\dot{Z} &= \omega \times Z = \hat{\omega} Z
\end{aligned}
$$
Reason: the magnitude of point on X-axis can the direction can be expressed as
$$
\begin{aligned}
mag &= |x| |\omega| sin\theta \\
direction &= \omega \times X \\
which\ makes\ \dot{X} &= \hat{\omega} X
\end{aligned}
$$
SO, we can get
$$
\dot{R} = \hat{\omega} R \Leftrightarrow \hat{\omega} = \dot{R} R^T
$$
However, if we want a intergrated version, using $\Delta R = \hat{\omega} R \Delta t$ is not a precise method. Converting R into Raw, Pitch, Yaw can get a precise result.
{{< /math >}}

### Homogeneous Transformation Matrix
{{< math >}}
$$
\dot{{}^AT_B} = \begin{bmatrix} 
\hat{{}^A\omega_B}{}^AR_B & {}^AU_B \\ 
0 & 0 
\end{bmatrix}
$$
{{< /math >}}

### Example 0: Earth, Plane and Man
{{< math >}}
Earth A, Plane B, Man C.

Given: $$\begin{matrix} {}^Au_B & ^Bu_C \\ {}^A\omega_B & {}^B\omega_C \end{matrix}$$

Find: $${}^Au_C, {}^A\omega_C$$

Solution:
$$
\begin{aligned}
\because {}^AT_C &= {}^AT_B {}^BT_C \\
\therefore \dot{{}^AT_C} &= \dot{{}^AT_B} {}^BT_C + {}^AT_B \dot{{}^BT_C} \\ \\
\begin{bmatrix}{}^A\omega_C{}^AR_B & {}^AU_C \\ 0 & 0\end{bmatrix}
&= \begin{bmatrix}{}^A\hat{\omega}_B{}^AR_B & {}^AU_B \\ 0 & 0\end{bmatrix}
\begin{bmatrix}{}^BR_C & {}^BP_C \\ 0 & 1\end{bmatrix} \\
&+ \begin{bmatrix}{}^AR_B & {}^AP_B \\ 0 & 1\end{bmatrix}
\begin{bmatrix}{}^B\omega_C{}^BR_C & {}^BU_C \\ 0 & 0\end{bmatrix} \\ \\

\therefore 
{}^AU_C &= {}^A\hat{\omega}_B{}^AR_B{}^BP_C + {}^AU_B + {}^AR_B{}^BU_C \\
{}^A\omega_C{}^AR_B &= {}^A\hat{\omega}_B{}^AR_B{}^BR_C + {}^AR_B{}^B\omega_C{}^BR_C \\\\

\therefore
{}^Au_C &= 
\underbrace{{}^Au_B}_{\text{plane movement}} + 
\underbrace{{}^AR_B{}^Bu_C}_{\text{human movement}} +
\underbrace{{}^A\omega_B \times {}^AR_B{}^BP_C }_{\text{plane changing orientation}}
\\
{}^A\omega_C &= {}^A\omega_B + {}^AR_B {}^B\omega_C
\end{aligned}
$$
{{< /math >}}

## End-Effector Velocity from Joint Velocity
### Total
{{< math >}}
$$
{}^0V_N = \begin{bmatrix} {}^0u_N \\ {}^0\omega_N \end{bmatrix}
= \sum_{i=1}^N {}^0J_i \dot{q}_i = {}^0J_N \dot{q}
$$
where $J_i \dot{q}_i $ is the effect of joint i on the end-effector alone
{{< /math >}}
0 can be replaced by any frame of expression and differentiation and N can be replaced by any frame of interest.

### For only one joint
One joint i is either rotating or translating with respect to Frame i-1.

#### Rotational Joint
{{< math >}}
The joint rotate around $k = z_{i-1}$ with speed $\dot{q}_i$.
$$
\begin{aligned}
\omega_i &= z_{i-1} \dot{q}_i \\
u_i &= \omega \times (P_N - P_{i-1}) \\
&= z_{i-1} \times (P_N - P_{i-1}) \dot{q}_i \\ \\
\therefore
J_i &= \begin{bmatrix} z_{i-1} \times (P_N - P_{i-1}) \\ z_{i-1} \end{bmatrix} \\
v &= J_i \dot{q}_i
\end{aligned}
$$
{{< /math >}}

#### Translational Joint
{{< math >}}
$$
\begin{aligned}
u_i &= z_{i-1} \dot{q}_i \\
\therefore
J_i &= \begin{bmatrix} z_{i-1} \\ 0 \end{bmatrix} \\
\end{aligned}
$$
{{< /math >}}

#### What is Jacobian Matrix in Mathematics?
In mathematics, the Jacobian matrix is the matrix of all first-order partial derivatives of a vector-valued function. When the matrix is a square matrix, both the matrix and its determinant are referred to as the Jacobian in literature. The matrix can be seen as a linear approximation of the multivariate function near a given point. The Jacobian matrix plays an important role in many applications such as change of variables in multiple integrals, implicit function theorem, etc.

#### Example 1: Holding a Pen
{{< math >}}
Given:
$$
{}^0V_3 = {}^0J_3 \dot{q}_3
$$

Find:
$$
{}^0V_E
$$

Solution:
$$
\begin{aligned}
{}^0\omega_E &= {}^0\omega_3 \\
{}^0u_E &= {}^0u_3 + {}^0\omega_3 \times ({}^0R_3 {}^3P_E)\\
&= {}^0u_3 + {}^0\omega_3 \times ({}^0P_E - {}^0P_3) \\
\end{aligned} \\ \\
\therefore
\begin{bmatrix} {}^0u_E \\ {}^0\omega_E \end{bmatrix}
=
\begin{bmatrix} I & \hat{-({}^0P_E - {}^0P_3)} \\ 0 & I \end{bmatrix}
\begin{bmatrix} {}^0u_3 \\ {}^0\omega_3 \end{bmatrix} \\
\therefore
{}^0J_E = \begin{bmatrix} I & \hat{-({}^0P_E - {}^0P_3)} \\ 0 & I \end{bmatrix} {}^0J_3
$$
{{< /math >}}

### Jacobian Transformation
{{< math >}}
$$
\begin{aligned}
{}^AJ_N = \begin{bmatrix} {}^AR_B & 0 \\ 0 & {}^AR_B \end{bmatrix} {}^BJ_N \\
{}^AV_N = \begin{bmatrix} {}^AR_B & 0 \\ 0 & {}^AR_B \end{bmatrix} {}^BV_N \\
\end{aligned}
$$
{{< /math >}}

### Summerize Example

The robot starts at joint 0 and end at joint N. The base frame is A and the robot is hold a tool E.

It is like A → 0 → ... → N → E.
{{< math >}}
$$
\begin{aligned}
{}^0V_N &= {}^0J_N \dot{q}_N \\
{}^0V_E &= {}^0J_E \dot{q}_N, {}^0J_E = \begin{bmatrix} I & \hat{-({}^0P_E - {}^0P_N)} \\ 0 & I \end{bmatrix} {}^0J_N \\
{}^AV_N &= \begin{bmatrix} {}^AR_0 & 0 \\ 0 & ^AR_0 \end{bmatrix} \dot{q}_N
\end{aligned}
$$
{{< /math >}}

## Inverse Kinematics of Velocity

{{< math >}}

Given: ${}^0V_N$

Find: $\dot{q}_N$

{{< /math >}}

### General Inverse of J
{{< math >}}
$$
\begin{aligned}
J^\# &\dot{=} \text{General Inverse of J} \\
J J^\# J &= J \\ \\

v &= J \dot{q} \\
\dot{q} &= J^\# v + [I - J^\# J] w \text{ , where w is any vector} \\
\end{aligned}
$$

> The $J^{-1}$ is a special case of $J^\#$, where J is square.

In this case when you multiply J on both sides, you will get $v = JJ^\#v + 0$. and this $[I - J^\#J]w$ is the null space of $J$, where this part of w will not affect the result. But this means that the solution is not unique. J# is a family of solutions. But left pseudo inverse is unique and is the best solution.
{{< /math >}}

Solution exists if and only if 
- rank(J) = min(m, n), i.e. full rank.
- each column of J is linearly independent
- J is "generalized invertible" if and only if columns of J are linearly independent
- Robot is at a non-singular configuration

The above conditions are equivalent.

> {{< math >}}
We need basic Jacobian. Basic Jacobian is the Jacobian when $\dot{x}$ is expressed in $\begin{bmatrix} u_x & u_y & u_z & \omega_x & \omega_y & \omega_z \end{bmatrix}^T$. Other cases are like x exp in $\begin{bmatrix} p_x &p_y & p_z & R & P & Y \end{bmatrix}^T$, and $\dot{x}$ is expressed in $\begin{bmatrix} \dot{p}_x &\dot{p}_y & \dot{p}_z & \dot{R} & \dot{P} & \dot{Y} \end{bmatrix}^T$, which corresponding J is not basic Jacobian. But of course we can convert RPY into omega.
{{< /math >}}

### Possible Solutions
#### Case 1: m = n
{{< math >}}
$$
J^\#(q) = J^{-1}
$$
Sometimes J is not invertible when the robot is at a singular configuration. Mathematically, $det(J) = 0$.
{{< /math >}}

#### Case 2: m > n, m < 6 (Underdetermined Robot)
Overdetermined system. Like robot with 2 joints but is asked to move in 3D space and achieve 6DOF.

However, we can still find a solution. The solution is the least square solution. using Left pseudo inverse.

{{< math >}}
$$
\begin{aligned}
J^{*\#} &= (J^T J)^{-1} J^T \text{ exist if and only if } rank(J) = n \\
\dot{q}^* &= J^{*\#} v_{real} \\
v_{pseudo} &= J \dot{q}^* \\
\end{aligned}
$$
In this solution, $||v_{real} - v_{pseudo}||_2$ is minimized. And we need $det(J^T J) \neq 0$, i.e. full rank.
{{< /math >}}

> **RANK** is the number of linearly independent rows or columns in a matrix. The rank of a matrix is the largest number of rows or columns that are linearly independent.
>
> We can understand it as independent pieces of information that a linear equation system can provide. So, *RANK <= min(m, n)*.

#### Case 3: m < n, m < 6 (Redundant Robot)
It is like we have a planer robot with 3 rot joints but we only ask for x,y.

#### Example 2: 3R Robot
Question: what are the singularities of this robot? i.e. what are the joint configurations that make the system lose full rank?

If there are cases that it can only achieve the position by specify all the joint angles, then it is singular. In this case, it is when the robot is fully stretched out.

{{< math >}}
$$
\begin{aligned}
J = \begin{bmatrix}
a & b & c \\
d & e & f \\
\end{bmatrix}  \\

J_{12} = \begin{bmatrix}
a & b \\
d & e \\
\end{bmatrix}
J_{23} = \begin{bmatrix}
b & c \\
e & f \\
\end{bmatrix}
J_{13} = \begin{bmatrix}
a & c \\
d & f \\
\end{bmatrix} \\
\text{Either of these J is non-singular, then the system is non-singular.}
\end{aligned}
$$
{{< /math >}}

For any given mxn Matrix, to determin rank, we should calculate the determinant of all the sub-matrix of size min(m,n) x min(m,n). If any of them is non-zero, then it is full rank.