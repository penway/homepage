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
{{< /math >}}