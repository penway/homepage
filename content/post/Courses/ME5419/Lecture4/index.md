---
title: More Gaussian, State Estimation, ProbMAN 4
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
- Probabilistic Robotics
---

## Useful Gaussian Identities and other math

Closed under convolution, product and conditional. While Product and Conditional need extra normalization factor, but the result is still a Gaussian.

{{<math>}}
$$
\begin{aligned}
\text{Convolution: } &\ \mu = \mu_1 + \mu_2,\ \Sigma = \Sigma_1 + \Sigma_2 \\
\text{Product: } &\ \Sigma^{-1} = \Sigma_1^{-1} + \Sigma_2^{-1},\ \mu = \Sigma(\Sigma_1^{-1}\mu_1 + \Sigma_2^{-1}\mu_2) \\
\text{Conditional: } &\ \mu = \mu_1 + \Sigma_{12}\Sigma_{22}^{-1}(x_2-\mu_2),\ \Sigma = \Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21} \\ \\
\text{Inversion Lemma: } &\ (R+PQP^T)^{-1} = R^{-1} - R^{-1}P(Q^{-1}+P^TR^{-1}P)^{-1}P^TR^{-1} \\ \\
\end{aligned}
$$
{{</math>}}

## Belief Propagation in Mobile Robot

Definition:
1. Belief of state of time t
2. Propagation Model: State at time t, depend on where you are at previous time and current control
3. Measurement Model: Measurement at time t, solely depend on what you are measuring now
{{<math>}}
$$
\begin{aligned}
bel(x_t) &\dot= p(x_t) \\
prop(x_t|x_{t-1},u_t) &\dot= p(x_t|x_{t-1},u_t) \\
meas(z_t|x_t) &\dot= p(z_t|x_t) \\ \\
\end{aligned}
$$

Prediction: Integrating over x_{t-1} combining propagation model and belief of previous state, i.e. propagating the prior belief to current time
$$
pred(x_t) \dot= \int_{x_t-1} prop(x_t|x_{t-1},u_t) bel(x_{t-1}) dx_{t-1}
$$
Often, $prop(x_t|x_{t-1}, u_t) = prop(x_t-x_{t-1}|0, u_t)$, when written like this, the calculation of pred becomes a convolution.


New belief: fusing the prediction and measurement model
$$
bel(x_t) = \eta\ meas(z_t|x_t) pred(x_t)
$$
{{</math>}}

## Information Fusion
{{<math>}}
$$
\begin{aligned}
h \cdot f(\vec{x_1}) \cdot f(\vec{x_2})
&= \eta\ exp\{-\frac{1}{2} x^T (\Sigma_1^{-1} + \Sigma_2^{-1}) x\},\ where\ \mu \text{ is omitted} \\

Under\ Fusion &:\ \rightarrow (\Sigma_1^{-1} + \Sigma_2^{-1})^{-1}, \text{cov smaller} \\
Under\ Convolution &:\ \rightarrow \Sigma_1 + \Sigma_2, \text{cov larger} \\ \\

Product\ of\ N\ Gaussians\ &with\ normalization : \\
\Sigma^{-1} &= \sum^N_{k=1} \Sigma_k^{-1} \\
\Sigma^{-1}\mu &= \sum^N_{k=1} \Sigma_k^{-1}\mu_k \\
In\ terms\ of\ Information\ &Matrix : \\
I &= \sum^N_{k=1} I_k \\
v &= \sum^N_{k=1} I_k v_k \\
\end{aligned}
$$
{{</math>}}

## Filters
### Bayes Filter
{{<math>}}
$$
\begin{aligned}
&for\ t=1:T\\
&\quad\quad Start\ with\ prior\ bel(x_{t-1}) \\
&\quad\quad pred(x_t) = \int_{x_t-1} prop(x_t | x_{t-1}, u_t)\  bel(x_{t-1})\ dx_{t-1} \\
&\quad\quad bel(x_t) = h\ meas(z_t|x_t)\ pred(x_t) \\
&end
\end{aligned}
$$
{{</math>}}

### Kalman Filters
Kalman Filter is basically Bayes Filter + (meas, prop, bel) are Gaussian, where conv, prod and cond are all closed.

So, we can only propagate(calculate) the mean and covariance.

**Kalman Filter Family**:
1. "Kalman Filter": Discrete Time, Linear Model

    {{<math>}}$x_t=Ax_{t-1}+Bu_t+Cdw_1${{</math>}}, 
    
    {{<math>}}$z_t=Dx_t+Edw_2${{</math>}}

    w are noises

2. "Kalman-Bucy Filter": Continuous Time, Linear Model

    "This is Kalman filter with differential equations"

3. "Extended Kalman Filter": Nonlinear Model, Discrete or Continuous Time version
    {{<math>}}$x_t=f(x_{t-1}, u)+Cdw_1${{</math>}}, 
    {{<math>}}$z_t=g(x_{t-1})+Edw_2${{</math>}}
> I don't expect you to know all, but you should know there are different versions of Kalman Filter, and they are all based on Bayes Filter.

### Information Filter
> I am sure this is not included. I copied from Thrun's book, while in Prof's notation. And find it too specific to be included in the exam.

{{<math>}}
$$
\begin{aligned}
log\ \rho(x) &= const. + \frac{1}{2} x^T I x - x^T \vec{v} \\ \\

Given\ v_{t-1}, &I_{t-1}, u_t, z_t: \\
\bar{I_t} &= (A_t I_{t-1}^{-1}A_t^T + R_t) ^ {-1} \\
\bar{v_t} &= \bar{I_t} (A_t I_{t-1}^{-1}v_{t-1} + B_t u_t) \\
I_t &= \bar{I_t} + C_t^T Q_t^{-1} C_t \\
v_t &= \bar{v_t} + C_t^T Q_t^{-1} z_t \\ \\
\end{aligned}
$$
{{</math>}}

For my unstanding, these filters are just secific implementations of Bayes Filter, adding upon different assumptions or mathematical properties.

### Other methods
- EKF(Extended Kalman Filter)
- Unscented Kalman Filter
- Particle Filter
- Rao-Blackwell Filter

### Stocastic Control
Modify the control input u to take the uncentainty in measeurement into account. (also not important)

## Parameter Estimation

We want to answer the question: "What is the best estimate of the parameter vector {{<math>}}$\theta${{</math>}} given the data D?" or "What is the convariance of the estimated(sampled) theta from the true one {{<math>}}$\Psi(\theta)${{</math>}}?"

**Cramer-Rao Lower Bound for PDFs**

> This part contains too many information and I don't think it is important. I will skip it. 


## 1. Inverse of Block Matrix Sigma
    
{{< math >}}
$$
\begin{aligned}
&\begin{bmatrix}
\Sigma_{12}   & \Sigma_{12} \\
\Sigma_{12}^T & \Sigma_{22}
\end{bmatrix}^{-1} =
\begin{bmatrix}
I_{11} & I_{12} \\
I_{12}^T & I_{22}
\end{bmatrix} \\
I_{11} &= \Sigma_{11}^{-1} + \Sigma_{11}^{-1} \Sigma_{12} (\Sigma_{22} - \Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12})^{-1}\Sigma_{12}^T\Sigma_{11}^{-1} \\
&= (\Sigma_{11} + \Sigma_{12}\Sigma_{22}\Sigma_{12}^T)^{-1} \\
I_{12} &= -\Sigma_{11}^{-1} \Sigma_{12} (\Sigma_{22} - \Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12})^{-1} \\
I_{12}^T &= -(\Sigma_{22} - \Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12})^{-1}\Sigma_{12}^T\Sigma_{11}^{-1} \\
I_{22} &= (\Sigma_{22} - \Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12})^{-1}
\end{aligned}
$$
The I is called Information Matrix, as is defined in the class.
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
\rho(x;\mu_1,&\Sigma_1) = n_1 exp\{\frac{1}{2}(x-\mu_1)^T\Sigma_1^{-1}(x-\mu_1)\} \\
\rho(x;\mu_2,&\Sigma_2) = n_2 exp\{\frac{1}{2}(x-\mu_2)^T\Sigma_2^{-1}(x-\mu_2)\} \\

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


## 4. Inversion Lemma: Inversion of {{< math >}}$R + PQP^T${{< /math >}}
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


## 5. Conditional Gaussian

{{< math >}}
$$
\begin{aligned}
Derive\ the\ following\ & equation: \\
\frac{\rho([x_1^T, x_2^T]^T;\mu,\Sigma)}{\rho(x_2;\mu_2,\Sigma_2)} &= 
\rho(x_1;\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(x_2-\mu_2),\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}) \\ \\

\rho([x_1^T, x_2^T]^T;\mu,\Sigma) &= N_1 exp\{-\frac{1}{2}
    \begin{pmatrix} x_1^T - \mu_1^T & x_2^T - \mu_2^T \end{pmatrix}
    \begin{pmatrix}
    I_{11} & I_{12} \\
    I_{12}^T & I_{22} 
    \end{pmatrix}
    \begin{pmatrix} x_1 - \mu_1 \\ x_2 - \mu_2 \end{pmatrix}\} \\

&= N_1 exp\{ -\frac{1}{2} (
    x_1^T I_{11} x_1 - x_1^T I_{12} x_2 - x_2^T I_{21} x_1 - x_2^T I_{22} x_2 \\
    &\quad + x_1^T I_{11} \mu_1 + x_1^T I_{12} \mu_2 + x_2^T I_{21} \mu_1 + x_2^T I_{22} \mu_2
    )\} \\ \\

\rho(x_2;\mu_2,\Sigma_2) &= N_2 exp\{-\frac{1}{2} (x_2 - \mu_2)^T \Sigma_2^{-1} (x_2 - \mu_2)\} \\

&= N_2 exp\{-\frac{1}{2} (
    x_2^T \Sigma_{22}^{-1} x_2 - x_2^T \Sigma_{22}^{-1} \mu_2 - \mu_2^T \Sigma_{22}^{-1} x_2 + \mu_2^T \Sigma_{22}^{-1} \mu_2
    )\} \\ \\

\frac{\rho([x_1^T, x_2^T]^T;\mu,\Sigma)}{\rho(x_2;\mu_2,\Sigma_2)} 
&= \frac{N_1}{N_2} exp\{-\frac{1}{2} (
    x_1^T I_{11} x_1 - x_1^T I_{12} x_2 - x_2^T I_{21} x_1 - x_2^T I_{22} x_2 \\
    &\quad + x_1^T I_{11} \mu_1 + x_1^T I_{12} \mu_2 + x_2^T I_{21} \mu_1 + x_2^T I_{22} \mu_2 \\
    &\quad - x_2^T \Sigma_{22}^{-1} x_2 + x_2^T \Sigma_{22}^{-1} \mu_2 + \mu_2^T \Sigma_{22}^{-1} x_2 - \mu_2^T \Sigma_{22}^{-1} \mu_2
    )\} \\

&= \eta\ exp\{-\frac{1}{2}
    (x_1 - M)^T I_{11} (x_1 - M) + ...\} \quad(eq.F1) \\ \\

where\ M &= \mu_1 - I_{11}^{-1} I_{12} (x_2 - \mu_2) \\
    &= \mu_1 - (\Sigma_{11} + \Sigma_{12}\Sigma_{22}\Sigma_{12}^T) (-\Sigma_{11}^{-1} \Sigma_{12} (\Sigma_{22} - \Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12})^{-1}) (x_2 - \mu_2)\ \quad(eq.M2)\\
  &= \mu_1 - \Sigma_{12} \Sigma_{22}^{-1} (x_2 - \mu_2)\quad(eq.M3)\\
I_{11} &= (\Sigma_{11} + \Sigma_{12}\Sigma_{22}\Sigma_{12}^T)^{-1} \\ \\

\therefore
new\ \mu &= M \\
new\ \Sigma &= I_{11}^{-1}
\end{aligned}
$$
{{< /math >}}

For{{<math>}}$M${{</math>}}, I do not know how to derive to the final answer, it seems that only if{{<math>}}$\Sigma_{12}\Sigma_{22}\Sigma_{12}^T = 0${{</math>}} and{{<math>}}\Sigma_{12}^T\Sigma_{11}^{-1}\Sigma_{12} = 0${{</math>}}, then we can derive from eq.M2 to eq.M3.

Also, eq.F1 is not fully expanded, only the quadratic terms are expanded, the linear terms are omitted, the answer can be get, but this cannot prove that the result is a Gaussian. The target form should be{{<math>}}(x - A)^T B (x - A) + V^T (x - A)${{</math>}}

But what we can learn from this is that, the conditional Gaussian is a Gaussian, and the mean and covariance can be derived from the original mean and covariance. Similar to the convolution of two Gaussian. Gaussian is closed under both convolution and conditional.


## 6. Product of N Gaussians
I am tired, I will do this later, or never.
{{< math >}}
$$
\begin{aligned}
Answer &: \\
\Sigma^{-1} &= \sum^N_{k=1} \Sigma_k^{-1} \\
\Sigma^{-1}\mu &= \sum^N_{k=1} \Sigma_k^{-1}\mu_k \\
\end{aligned}
$$
{{< /math >}}
