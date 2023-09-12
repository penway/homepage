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
> $$
\begin{align}
{}^B_AP_C &= {}^AR_B \cdot {}^B_BP_C \\
{}^AP_C &= {}^AP_B + {}^AR_C \cdot {}^BP_C
\end{align}
> $$
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

Given: $\begin{matrix} {}^Au_B & ^Bu_C \\ {}^A\omega_B & {}^B\omega_C \end{matrix}$

Find: ${}^Au_C, {}^A\omega_C$
{{< /math >}}