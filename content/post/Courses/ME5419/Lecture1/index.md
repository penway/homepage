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

## Random Variables and Probability Distributions
{{< math >}}
$$
\begin{aligned}
\text{Joint probability: }& P(X, Y) =^{indpendent} P(X)P(Y) \\
\text{Conditional probability: }& P(X|Y) \dot{=} \frac{P(X, Y)}{P(Y)} \\
\text{Sum or Integral: }& \sum_{x \in X} p(x) = 1;\ &\int_{x \in X} \rho(x) dx = 1 \\
& \sum_{x \in X}\sum_{y \in Y} p(x, y) = 1;\ &\int_{x \in X} \int_{y \in Y} \rho(x, y) dy dx = 1 \\
\text{Bayes Rule: }& P(X|Y) = \frac{P(Y|X)P(X)}{P(Y)} \\
\text{Marginalization: }& P(X) = \sum_{y \in Y}P(X, Y);\ &\rho(x) = \int_{y \in Y} \rho(x, y) dy \\ \\
\text{Mean: }& \mu = \sum_{x \in X} x\ p(x);\ &\mu = \int_{x \in X} x\ \rho(x)\ dx \\
\text{Variance: }& \sigma^2 = \sum_{x \in X} (x - \mu)^2 p(x);\ &\sigma^2 = \int_{x \in X} (x - \mu)^2 \rho(x)\ dx \\
\end{aligned} \\
$$
{{< /math >}}

## Convolution
We want to know the probability distribution when two random variables are added together. For example, roll two dice and add the numbers together. The probability distribution of the sum is the convolution of the two dice.
{{< math >}}
$$
\begin{aligned}
\text{Convolution: }& P_{X+Y}(Z) = \sum_{\xi \in X} P_X(\xi) P_Y(z - \xi) \\
& P_{X+Y}(Z) = \int_{\xi \in X} \rho_X(\xi) \rho_Y(z - \xi) d\xi \\
Mean: & \mu_{X+Y} = \mu_X + \mu_Y \\
Variance: & \sigma_{X+Y}^2 = \sigma_X^2 + \sigma_Y^2 \\
\end{aligned}
$$
{{< /math >}}

## Gaussian Distribution
{{< math >}}
$$
\begin{aligned}
\rho(x;\mu,\sigma^2) &= \frac{1}{\sqrt{2\pi}\sigma}e^{(x-\mu)^2/2\sigma^2} \\
Convolution: \rho(x; \mu_1, \sigma_1^2) * \rho(x; \mu_2, \sigma_2^2) &= \rho(x; \mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2) \\

\end{aligned}
$$
{{< /math >}}

## Homework 1
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
