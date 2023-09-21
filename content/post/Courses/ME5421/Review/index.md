---
title: 'Robotics Kinematics Review: Fast Version for Everything'
subtitle: Notes for ME5421

# Summary for listings and search engines
summary: Robotics Kinematics

# Link this post with a project
projects: [ME5421]

date: '2023-09-12T00:00:00Z'
lastmod: '2023-09-12T00:00:00Z'

authors:
- penway

tags:
- 

categories:
- Course Notes

share: false
---

## Force of one joint
{{< math >}}
$$
\begin{aligned}
& \sum F = 0 \\
& i.e.\ f_i - f_{i+1} = 0 \\

& \sum T_{\text{torques about origin i-1}} = 0 \\
& i.e.\ n_i - n_{i+1} + (p_i - p_{i-1}) \times - f_{i+1} = 0
\end{aligned}
$$
Another view:
$$
\begin{aligned}
f_i &= f_{i+1} \\
n_i &= n_{i+1} + (p_i - p_{i-1}) \times f_{i+1}
\end{aligned}
$$
If robot arm is rigid, the force needed in the joint is shown. Where z indicate the direction and n or f indicate the force.
$$
\begin{aligned}
T_i &= n_i^T z_{i-1} \text{ (rotational)} \\
T_i &= f_i^T z_{i-1} \text{ (translational)}
\end{aligned}
$$
{{< /math >}}

## Force and Jacobian
{{<math>}}
$\tau$ is the force the every joint. shape: (n, 1)
$$
\begin{aligned}
\tau &= J^T F \\
\end{aligned}
$$
{{</math>}}
Singularity: J in not full rank.

## Force transformation
{{<math>}}
Let $^AF_B$ be the force and moment experienced at B, $^AF_C$ be the force and moment excerted on C. B C are linked by a rigid body. Then:
$$
\begin{aligned}
^Af_B &= {}^Af_C \\
^An_B &= {}^An_C + (^Ap_B - {}^Ap_C) \times {}^Af_C \\
\begin{bmatrix} {}^Af_B \\ ^An_B \end{bmatrix} &= 
\begin{bmatrix} 
I & 0 \\
\hat{{}^AR_B{}^Bp_C} & I
\end{bmatrix}
\begin{bmatrix} {}^Af_C \\ {}^An_C \end{bmatrix} \\ \\

\begin{bmatrix} {}^Bf_B \\ ^Bn_B \end{bmatrix} &=
\begin{bmatrix}
{}^BR_A{}^AR_C & 0 \\
{}^BR_A (\hat{{}^AR_B{}^Bp_C}) {}^AR_C & {}^BR_A{}^AR_C
\end{bmatrix}
\begin{bmatrix} {}^Cf_C \\ {}^Cn_C \end{bmatrix} \\

\end{aligned}
$$

> Note: $
\begin{bmatrix} {}^Af_C \\ {}^An_C \end{bmatrix} =
\begin{bmatrix}
{}^AR_C & 0 \\
0 & {}^AR_C
\end{bmatrix}
\begin{bmatrix} {}^Cf_C \\ {}^Cn_C \end{bmatrix} \\\\
$
{{</math>}}
