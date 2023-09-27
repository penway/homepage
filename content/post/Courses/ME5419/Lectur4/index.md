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
W &= \Sigma_{11}^{-1} + \Sigma_{11}^{-1} \Sigma_{12} (\Sigma_{22} - \Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12})^{-1}\Sigma_{12}^T\Sigma_{11}^{-1} \\
&= (\Sigma_{11} + \Sigma_{12}\Sigma_{22}\Sigma_{12}^T)^{-1} \\
X &= -\Sigma_{11}^{-1} \Sigma_{12} (\Sigma_{22} - \Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12})^{-1} \\
Y &= -(\Sigma_{22} - \Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12})^{-1}\Sigma_{12}^T\Sigma_{11}^{-1} \\
Z &= (\Sigma_{22} - \Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12})^{-1}
\end{aligned}
$$
{{< /math >}}

## 2. Product of Gaussian Distribution

{{< math >}}
$$
\begin{aligned}
&Given\ h f_1(x) f_2(x) = f_3(x), \text{where all f are Gaussian distribution, h is normalizing factor} \\
&Find\ \mu_3\ and\ \Sigma_3 \\ \\
&\text{As we have h, all the normalizing factors in X and Y will be absorbed into } h \\
\end{aligned}
$$
$$
\begin{aligned}
\rho(x;\mu_1,&Sigma_1) = n_1 exp\{\frac{1}{2}(x-\mu_1)^T\Sigma_1^{-1}(x-\mu_1)\} \\
\rho(x;\mu_2,&Sigma_2) = n_2 exp\{\frac{1}{2}(x-\mu_2)^T\Sigma_2^{-1}(x-\mu_2)\} \\
\rho(x;\mu_3,&Sigma_3) = n_3 exp\{\frac{1}{2}(x-\mu_3)^T\Sigma_3^{-1}(x-\mu_3)\} \\

h f_1 f_2 &= h\ n_1\ n_2\ exp\{\frac{1}{2}(x-\mu_1)^T\Sigma_1^{-1}(x-\mu_1)\}\ exp\{\frac{1}{2}(x-\mu_2)^T\Sigma_2^{-1}(x-\mu_2)\} \\

&= h\ exp\{-\frac{1}{2}[(x-\mu_1)^T\Sigma_1^{-1}(x-\mu_1) + (x-\mu_2)^T\Sigma_2^{-1}(x-\mu_2)]\} \\

&= h\ exp\{-\frac{1}{2} (x^T\Sigma_1^{-1}x - 2x^T\Sigma_1^{-1}\mu_1 + \mu_1^T\Sigma_1^{-1}\mu_1 \\
&\quad \quad \quad + x^T\Sigma_2^{-1}x - 2x^T\Sigma_2^{-1}\mu_2 + \mu_2^T\Sigma_2^{-1}\mu_2)\} \\

&= h\ exp\{-\frac{1}{2} x^T(\Sigma_1^{-1} + \Sigma_2^{-1})x - 2x^T(\Sigma_1^{-1}\mu_1 + \Sigma_2^{-1}\mu_2)\\
&\quad \quad \quad + \mu_1^T\Sigma_1^{-1}\mu_1 + \mu_2^T\Sigma_2^{-1}\mu_2\}\\

f_3 &= n_3\ exp\{-\frac{1}{2} x^T\Sigma_3^{-1}x - 2x^T\Sigma_3^{-1}\mu_3 + \mu_3^T\Sigma_3^{-1}\mu_3\} \\

\therefore \Sigma_3^{-1} &= \Sigma_1^{-1} + \Sigma_2^{-1} \\
\mu_3^T\Sigma_3^{-1} &= \Sigma_1^{-1}\mu_1 + \Sigma_2^{-1}\mu_2 \\
\mu_3 &= \Sigma_3(\Sigma_1^{-1}\mu_1 + \Sigma_2^{-1}\mu_2) \\
\end{aligned}
$$
{{< /math >}}

## 3. Marginalization of Gaussian Distribution

I cannot solve this one.
{{< math >}}
$$
\begin{aligned}
&Given\ f(x) = \rho(\begin{pmatrix} x_1 \\ x_2\end{pmatrix};\ \begin{pmatrix} \mu_1 \\ \mu_2\end{pmatrix},\begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22}\end{pmatrix}) \\
& Prove \int f(x_1,x_2) dx_1 = \rho(x_2;\mu_2,\Sigma_{22}),\text{use brute force integration} \\ \\

\int f(x_1,x_2) dx_1
&= \int N\ exp\{-\frac{1}{2} (x - \mu)^T \Sigma^{-1} (x - \mu)\} dx_1 \\
&= \int N\ exp\{-\frac{1}{2} [x^T\Sigma^{-1}x - 2\mu^T\Sigma^{-1}x + \mu^T\Sigma^{-1}\mu]\} dx_1 \\
&= N\ exp\{\mu^T\Sigma^{-1}\mu\}\ \int exp\{-\frac{1}{2}x^T\Sigma^{-1}x \}dx_1 \int exp\{-\frac{1}{2} \mu^T\Sigma^{-1}x\}dx_1 \\

x^T\Sigma^{-1} x &= \begin{pmatrix} x_1 & x_2\end{pmatrix} \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{12}^T & \Sigma_{22}\end{pmatrix}^{-1} \begin{pmatrix} x_1 \\ x_2\end{pmatrix} \\

&= \begin{pmatrix} x_1^T & x_2^T \end{pmatrix} \begin{pmatrix} W & X \\ Y & Z \end{pmatrix} \begin{pmatrix} x_1 \\ x_2\end{pmatrix} \\

&= x_1^T W x_1 + x_1^T X x_2 + x_2^T Y x_1 + x_2^T Z x_2 \\

&= x_1^T W x_1 + x_1^T (X + Y^T) x_2 + x_2^T Z x_2 \\
\end{aligned}
$$
{{< /math >}}
I cannot solve this one.


## 4. Inversion of R + PQPT
{{< math >}}
$$
\begin{aligned}
& (R+PQP^T)^{-1} = R^{-1} - R^{-1}P(Q^{-1}+P^TR^{-1}P)^{-1}P^TR^{-1} \\ \\
& (R+PQP^T)^{-1} [R^{-1} - R^{-1}P(Q^{-1}+P^TR^{-1}P)^{-1}P^TR^{-1}] \\
&= I + PQP^TR^{-1} - P(Q^{-1}+P^TR^{-1}P)^{-1}P^TR^{-1}
\\&\quad\quad\quad - PQP^TR^{-1}P(Q^{-1}+P^TR^{-1}P)^{-1}P^TR^{-1} \\
&= I + PQP^TR^{-1} - (P + PQP^TR^{-1}P)(Q^{-1}+P^TR^{-1}P)^{-1}P^TR^{-1} \\
&= I + PQP^TR^{-1} - PQ(Q^{-1} + P^TR^{-1}P)(Q^{-1}+P^TR^{-1}P)^{-1}P^TR^{-1} \\
&= I + PQP^TR^{-1} - PQP^TR^{-1} \\
&= I

\end{aligned}
$$
{{< /math >}}