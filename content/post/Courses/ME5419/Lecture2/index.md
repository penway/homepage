---
title: Probability and Statistics in n-D
subtitle: Probabilistic Robotics Lecture 2

summary: Probabilistic Robotics
projects: [ME5419]

date: '2023-09-29T00:00:00Z'
lastmod: '2023-09-29T00:00:00Z'

draft: false
featureSigma_d: false

authors:
- penway

categories:
- Course Notes
---

## Basics
{{<math>}}
$$
\begin{aligned}
f(\vec{x}) & \\
\int_{\mathbb{R}^n} f(\vec{x})d\vec{x} &= 1 \\
\vec\mu &= \int_{\mathbb{R}^n} \vec x\ \rho (\vec x)\ d \vec x \\
\Sigma &= \int_{\mathbb{R}^n} (\vec x - \vec \mu)(\vec x - \vec \mu)^T\ \rho (\vec x)\ d \vec x \\
\end{aligned}
$$
{{</math>}}

### Expectation
{{<math>}}
$$
\begin{aligned}
\mu &= E[x] = \int_{\mathbb{R}^n} x\ \rho(x)\ dx \\
\sigma^2 &= E[(x - \mu)^2] = \int_{\mathbb{R}^n} (x - \mu)^2\ \rho(x)\ dx \\
E[f(x)] &= \int_{-\inf}^{\inf} f(x)\ \rho(x)\ dx \\
E[f(\vec x)] &= \int_{D \subset \mathbb{R}^n} f(\vec x)\rho(\vec x)\ d\vec x \\
\end{aligned}
$$
{{</math>}}

## Multivariate Gaussian
{{<math>}}
$$
\begin{aligned}
\rho(x;\mu,\Sigma) &\dot= \frac{1}{(2\pi)^{\frac{n}{2}}|det\Sigma|^{\frac{1}{2}}}exp\{-\frac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)\} \\
\int_{\mathbb{R}^n}& \rho(x; \mu, \Sigma)\ dx = 1 \\
\int_{\mathbb{R}^n}& x\ \rho(x; \mu, \Sigma)\ dx = \mu \\
\int_{\mathbb{R}^n}& (x - \mu)\ \rho(x; \mu, \Sigma)\ dx = \Sigma \\
\end{aligned}
$$
{{</math>}}

## Crazy Math Tools
As Covariance matrix is symmetric matrix, it can be diagonalized by orthogonal matrix $Q$.
{{<math>}}
$$
\begin{aligned}
\Sigma &= Q\Lambda Q^T \\
det|\Sigma| &= det|Q\Lambda Q^T| = det|Q|\ det|\lambda|\ det|Q^T| = det|QQ^T|\ det|\lambda| = det|\Lambda| \\
\end{aligned}
$$
{{</math>}}

## Eigenvactors and Eigenvalues'
{{<math>}}
$$
\begin{aligned}
A\ \vec v &= \lambda\ \vec v \\
\end{aligned}
$$
{{</math>}}
