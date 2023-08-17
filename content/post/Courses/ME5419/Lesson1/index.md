---
title: Basic Probability and Statistics
subtitle: Probabilistic Robotics Lecture 1

summary: Probabilistic Robotics
projects: [ME5419]

date: '2023-08-15T00:00:00Z'
lastmod: '2023-08-15T00:00:00Z'

draft: false
featured: false

authors:
- penway

categories:
- Course Notes
---

{{< math >}}
Given independent variables $X$ and $Y$, what is the mean and variance of $X+Y$?

$$
\begin{aligned}
\mu_{X+Y} &= \Sigma_{z \in Z} z P_{X+Y}(z) \\
&= \Sigma_{z \in Z} z \Sigma_{\xi \in X} P_X(\xi) P_Y(z - \xi) \\
&let\ w=z-\xi \\
&= \Sigma_{w \in W} \Sigma_{\xi \in X} (\xi + w) P_X(\xi) P_Y(w) \\
&= \Sigma_{w \in W} w P_Y(w) + \Sigma_{\xi \in X} \xi P_X(\xi) (independent) \\
&= \mu_Y + \mu_X \\
\end{aligned}
$$

{{< /math >}}
