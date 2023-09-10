---
title: Basic Probability and Statistics
subtitle: Probabilistic Robotics Lecture 1

summary: Probabilistic Robotics
projects: [ME5419]

date: '2023-08-15T00:00:00Z'
lastmod: '2023-08-15T00:00:00Z'

draft: false
featureSigma_d: false

authors:
- penway

categories:
- Course Notes
---

{{< math >}}
Given independent variables $X$ and $Y$, what is the mean and variance of $X+Y$?

$$
\begin{aligned}
\mu_{X+Y} &= \sum_{z \in Z} z P_{X+Y}(z) \\
&= \sum_{z \in Z} z \sum_{\xi \in X} P_X(\xi) P_Y(z - \xi) \\
&let\ w=z-\xi \\
&= \sum_{w \in W} \sum_{\xi \in X} (\xi + w) P_X(\xi) P_Y(w) \\
&= \sum_{w \in W} w P_Y(w) + \sum_{\xi \in X} \xi P_X(\xi) \\
&= \mu_Y + \mu_X \\
\end{aligned}
$$

(I know there are nonsence involved in the below derivation, but I just want to show the process of how I get the result)
$$
\begin{aligned}
\sigma_{X+Y}^2 &= \sum_{z \in Z} (z - \mu_{X+Y})^2 P_{X+Y}(z) \\
&= \sum_{z \in Z} (z - \mu_{X+Y})^2 \sum_{\xi \in X} P_X(\xi) P_Y(z - \xi) \\
&let\ w=z-\xi \\
&= \sum_{w \in W} \sum_{\xi \in X} (w + \xi - \mu_{X+Y})^2 P_X(\xi) P_Y(w) \\
&= \sum_{w \in W} \sum_{\xi \in X} [(\xi - \mu_X) + (w - \mu_Y)]^2 P_X(\xi) P_Y(w) \\
&= \sum_{w \in W} \sum_{\xi \in X} [(\xi - \mu_X)^2 + (w - \mu_Y)^2 + 2(\xi - \mu_X)(w - \mu_Y)] P_X(\xi) P_Y(w) \\
&= \sum_{w \in W} \sum_{\xi \in X} (\xi - \mu_X)^2 P_X(\xi) P_Y(w) + \sum_{w \in W} \sum_{\xi \in X} (w - \mu_Y)^2 P_X(\xi) P_Y(w) + \sum_{w \in W} \sum_{\xi \in X} 2(\xi - \mu_X)(w - \mu_Y) P_X(\xi) P_Y(w) \\
&= \sum_{w \in W}P_Y(w)\sigma_X^2 + \sum_{\xi \in X}P_X(\xi)\sigma_Y^2 + 2 \sum_{w \in W} \sum_{\xi \in X} (\xi - \mu_X)(w - \mu_Y) P_X(\xi) P_Y(w) \\
&= \sigma_X^2 + \sigma_Y^2 + 2 \sum_{w \in W} \sum_{\xi \in X} (\xi - \mu_X)(w - \mu_Y) P_X(\xi) P_Y(w) \\
&= \sigma_X^2 + \sigma_Y^2 + 2 \sum_{w \in W} (w - \mu_Y) P_Y(w) \sum_{\xi \in X} (\xi - \mu_X) P_X(\xi) \\
&= \sigma_X^2 + \sigma_Y^2 + 2 \sum_{w \in W} (w - \mu_Y) P_Y(w) (\mu_X - \mu_X) \\
&= \sigma_X^2 + \sigma_Y^2 \\
\end{aligned}
$$
{{< /math >}}