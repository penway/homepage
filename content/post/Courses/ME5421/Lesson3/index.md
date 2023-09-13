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

### TL;DR
- [ ] Homogeneous Transformation Matrix
- [ ] Jacobian Matrix

### Velocity Representation

#### Translational Velocity

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

#### Rotational Velocity
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

#### Homogeneous Transformation Matrix
{{< math >}}
$$
\dot{{}^AT_B} = \begin{bmatrix} 
\hat{{}^A\omega_B}{}^AR_B & {}^AU_B \\ 
0 & 0 
\end{bmatrix}
$$
{{< /math >}}

#### Example 0: Earth, Plane and Man
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

## Summerize Example

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