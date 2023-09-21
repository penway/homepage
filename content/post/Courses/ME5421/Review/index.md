---
title: Robotics Kinematics Review: Fast Version for Everything
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


