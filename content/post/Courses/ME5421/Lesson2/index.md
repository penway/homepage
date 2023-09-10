---
title: Robotics Kinematics Lesson 2
subtitle: Notes for ME5421

# Summary for listings and search engines
summary: Robotics Kinematics

# Link this post with a project
projects: [ME5421]

# Date published
date: '2023-09-10T00:00:00Z'

# Date updated
lastmod: '2023-09-10T00:00:00Z'

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

## Denavit-Hartenberg Representation
- two rules to limit 6 DOF to 4 variables representation
1. z-axis is the axis of motion (Link i moves around or along z-axis of frame i-1)
2. x-axis is the common normal of z-axis of frame i-1 and frame i

### Four parameters

The four parameters are the four elementary motions:
1. {{< math >}}$\theta_i$: bring $x_{i-1} // x_i$, around $z_{i-1}${{< /math >}}
2. {{< math >}}$r_i$: bring $x_{i-1} = x_i$, along $z_{i-1}${{< /math >}}
3. {{< math >}}$d_i$: bring origin $O_{i-1} = O_i$, along $x_i${{< /math >}}
4. {{< math >}}$\alpha_i$: bring $z_{i-1} = z_i$, around $x_i${{< /math >}}

For each joint, only one parameter is variable.
- Rotational joint: {{< math >}}$\theta_i${{< /math >}}
- Translational joint: {{< math >}}$r_i${{< /math >}}
These are called the {{< math >}}**joint variables $q_i$**{{< /math >}}

### Forward Kinematic Problem

> know joint, find hand

**Given**: {q_i}, {DH parameters}; 
**Find**: End-effector position {{< math >}}$P_E$ and orientation $R_E${{< /math >}}

1. Assign Frame
2. Identify joint variables and link kinematic parameters
3. Define like transformation matrices. $^{i-1}T_i = A_i$
4. Compute {{< math >}}$^{0}T_N(q_1q_2...q_N) = A_1A_2...A_n${{< /math >}}

### Inverse Kinematic Problem
> know hand, find how to move joints

**Given**: {DH parameters}, P_E, R_E;
**Find**: {q_i}

*ISSUE*: the solution is not unique or may not exist 
- Existence
    - $P_E$ must be within the workspace
    - Dexterous workspace: the position and orientation can be fully controlled
        - but sometimes dexterous workspace can mean the workspace we are interested in, which might not be the full position and orientation
    - is P is in Dexterous workspace, then there is a solution

### Solution for Inverse Kinematic Problem
{{< math >}}
Given:
$$
^{0}T_N = \begin{bmatrix}
    n_x & o_x & a_x & p_x \\
    n_y & o_y & a_y & p_y \\
    n_z & o_z & a_z & p_z \\
    0 & 0 & 0 & 1
\end{bmatrix}

A_i = \begin{bmatrix}
    c\theta_i & -c \alpha_i s \theta_i & s \alpha_i s \theta_i & d_i c \theta_i \\
    s\theta_i & c \alpha_i c \theta_i & -s \alpha_i c \theta_i & d_i s \theta_i \\
    0 & s \alpha_i & c \alpha_i & r_i \\
    0 & 0 & 0 & 1
\end{bmatrix}
$$
Find: $\mathbf{q} = q_1, q_2, ..., q_N$

We know that: $^{0}T_N = A_1A_2...A_N$
and $LHS(i,j) = RHS(i,j)$
{{< /math >}}

#### Approach 1: General Solution
{{< math >}}
$$
A_1^{-1} {}^0T_N = A_2A_3...A_N = {}^1T_N
$$

And examine the LHS and RHS, to look for constant elements in $^1T_N$. And $q_1$ can be solved.
{{< /math >}}
And we can do this recursively to solve for all $q_i$.

*Note that there is no algorithmic approach that is 100% effective. And we need **geometric intuition.***


#### Special Cases: DECOUPLED ROBOT GEOMETRIES
1. Robots with any 3 joints are TRANSLATIONAL
2. Robots with any 3 rotational joints axes co-intersecting at a common point. i.e. their *Z*-axis intersect at a common point.

These can reduce system to a lower order subsystem (i.e. 3rd order) for which closed form solutions are guaranteed.


**Example Case 1**: Cartesian Robot

{{< math >}}
As the first three joints are translational, we can write:
$^0R_6 = f(q_4, q_5, q_6)$
{{< /math >}}
{{< math >}}
then we can solve for $q_4, q_5, q_6$
{{< /math >}}
{{< math >}}
Then we can solve for $q_1, q_2, q_3$ using $^0P_6 = f(q_1, q_2, q_3) (known: q_4, q_5, q_6)$
{{< /math >}}
So, we decoupled the problem into two subsystems, with orientaion decoupled.


**Example Case 2**: PUMA Robot
{{< math >}}
The last three rotaional joints have co-intersecting axes, which means when rotating them, the $^0P_{cointersection} = f(q_1, q_2, q_3)$.

Given $^0P_6$, $^0P_{co} = {}^0P_6 - r_6 {}^0z_6$, where $r_6$ is the distance between co to $O_6$

So, we solve $^0R_4 = f(q_1, q_2, q_3)$ first and then $^0R_6 = f(q_1, q_2, q_3, q_4, q_5, q_6)$

We decoupled position this time.
{{< /math >}}

#### Some useful closed form solutions are listed in the slides
1. 
{{< math >}}
$$
\left.
\begin{array}{lr}
    sin(\theta) = a, a \in [-1, 1]\\
    cos(\theta) = b, b \in [-1, 1]
\end{array}
\right.
\Rightarrow
\theta = atan2(a, b)
$$
{{< /math >}}

2. 
{{< math >}}
$$
\left.
\begin{array}{lr}
    sin(\theta) = a, a \in [-1, 1]\\
    cos(\theta) = \pm\sqrt{1 - a^2}
\end{array}
\right.
\Rightarrow
\theta_0 = atan2(a, \pm\sqrt{1 - a^2})
\Rightarrow
\theta = \theta_0\ or\  180 - \theta_0
$$
Singularity will occur when $|a| = 1$, in which case $\theta_0 = \pm 90$, which leads to denegeracy of order 2.

{{< /math >}}

3. 
{{< math >}}
$$
acos(\theta) + bsin(\theta) = 0
\Rightarrow
\theta = atan2(-a, b)\ or\ atan2(a, -b)
$$
These two solutions are 180 degrees apart.

Singularity when a = b = 0, which leads to infinite order degenracy.
{{< /math >}}

4. 
{{< math >}}
$$
\begin{align}
acos(\theta) + bsin(\theta) = c &\Rightarrow\\
& \theta = atan2(b, 1) + atan2(\pm\sqrt{a^2 + b^2 - c^2}, c)\\
& a^2 + b^2 - c^2  < 0 \Rightarrow our\ of\ workspace \\
& a^2 + b^2 - c^2  = 0 \Rightarrow singularity (one\ solution)\\
& degeneracy\ order = 2
\end{align}
$$
{{< /math >}}