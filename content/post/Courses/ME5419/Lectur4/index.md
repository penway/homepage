---
title: Homework of Lecture 4
subtitle: Probabilistic Robotics

summary: Probabilistic Robotics
projects: [ME5419]

date: '2023-09-27T00:00:00Z'
lastmod: '2023-09-27T00:00:00Z'

draft: false
featureSigma_d: false

authors:
- penway

categories:
- Course Notes
---

## 1. Inverse of Block Matrix Sigma
    
{{< math >}}
$$
\begin{aligned}
&\begin{bmatrix}
\Sigma_{12}   & \Sigma_{12} \\
\Sigma_{12}^T & \Sigma_{22}
\end{bmatrix}^{-1} =
\begin{bmatrix}
W & X \\
Y & Z
\end{bmatrix} \\
&W = \Sigma_{11}^{-1} + \Sigma_{11}^{-1} \Sigma_{12} (\Sigma_{22} - \Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12})^{-1}\Sigma_{12}^T\Sigma_{11}^{-1} \\
&X = -\Sigma_{11}^{-1} \Sigma_{12} (\Sigma_{22} - \Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12})^{-1} \\
&Y = -(\Sigma_{22} - \Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12})^{-1}\Sigma_{12}^T\Sigma_{11}^{-1} \\
&Z = (\Sigma_{22} - \Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12})^{-1}
\end{aligned}
$$
{{< /math >}}

## 2. Product of Gaussian Distribution

{{< math >}}
$$
Given\ h f_1(x) f_2(x) = f_3(x), \text{where all f are Gaussian distribution, h is normalizing factor} \\
Find\ \mu_3\ and\ \Sigma_3 \\ \\
\text{As we have h, all the normalizing factors} \\
\text{in X and Y will be absorbed into } h \\ \\
$$
$$
\begin{aligned}
\rho(x;\mu_1,Sigma_1) &= n_1 exp\{\frac{1}{2}(x-\mu_1)^T\Sigma_1^{-1}(x-\mu_1)\} \\
\rho(x;\mu_2,Sigma_2) &= n_2 exp\{\frac{1}{2}(x-\mu_2)^T\Sigma_2^{-1}(x-\mu_2)\} \\
\rho(x;\mu_3,Sigma_3) &= n_3 exp\{\frac{1}{2}(x-\mu_3)^T\Sigma_3^{-1}(x-\mu_3)\} \\

h f_1 f_2 &= h\ n_1\ n_2\ exp\{\frac{1}{2}(x-\mu_1)^T\Sigma_1^{-1}(x-\mu_1)\}\ exp\{\frac{1}{2}(x-\mu_2)^T\Sigma_2^{-1}(x-\mu_2)\} \\

&= h\ exp\{\frac{1}{2}[(x-\mu_1)^T\Sigma_1^{-1}(x-\mu_1) + (x-\mu_2)^T\Sigma_2^{-1}(x-\mu_2)]\} \\

&= h\ exp\{\frac{1}{2} (x^T\Sigma_1^{-1}x - 2x^T\Sigma_1^{-1}\mu_1 + \mu_1^T\Sigma_1^{-1}\mu_1 \\
&\quad \quad \quad + x^T\Sigma_2^{-1}x - 2x^T\Sigma_2^{-1}\mu_2 + \mu_2^T\Sigma_2^{-1}\mu_2)\} \\

&= h\ exp\{\frac{1}{2} x^T(\Sigma_1^{-1} + \Sigma_2^{-1})x - 2x^T(\Sigma_1^{-1}\mu_1 + \Sigma_2^{-1}\mu_2)\\
&\quad \quad \quad + \mu_1^T\Sigma_1^{-1}\mu_1 + \mu_2^T\Sigma_2^{-1}\mu_2\}\\

f_3 &= n_3\ exp\{\frac{1}{2} x^T\Sigma_3^{-1}x - 2x^T\Sigma_3^{-1}\mu_3 + \mu_3^T\Sigma_3^{-1}\mu_3\} \\

\therefore \Sigma_3^{-1} &= \Sigma_1^{-1} + \Sigma_2^{-1} \\
\mu_3^T\Sigma_3^{-1} &= \Sigma_1^{-1}\mu_1 + \Sigma_2^{-1}\mu_2 \\
\mu_3 &= \Sigma_3(\Sigma_1^{-1}\mu_1 + \Sigma_2^{-1}\mu_2) \\
\end{aligned}
$$
{{< /math >}}