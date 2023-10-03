---
title: Motion, Random Walk, and SDE, ProbMAN 3
subtitle: Probabilistic Robotics Lecture 3

summary: Probabilistic Robotics
projects: [ME5419]

date: '2023-10-03T00:00:00Z'
lastmod: '2023-10-03T00:00:00Z'

draft: false
featureSigma_d: false

authors:
- penway

categories:
- Course Notes
- Probabilistic Robotics
---

## Linearization of E.O.M.

E.O.M means Equation of Motion.

For a physical system, the E.O.M. is usually nonlinear, with the form of
{{<math>}}
$$
\begin{aligned}
Let\ \vec \theta = \begin{pmatrix} \theta_1 & \theta_2 \end{pmatrix}^T \\
M(\theta)\ddot{\vec \theta} + C(\theta, \dot{\vec \theta})\dot{\vec \theta} + G(\theta) &= 0 \\
\end{aligned}
$$
{{</math>}}
Where
- M is the mass matrix
- C is the Coriolis matrix
- G is the gravity matrix

**The general form can be written as**
{{<math>}}
$$
M(q)\ddot{q} + C(q, \dot{q})\dot{q} + G(q) = 0
$$
{{</math>}}

Whenever we choose generalized coordinates measured from equilibrium points, we can linearize the E.O.M. by assumptions:
- Small angle, ||q|| << 1
- Small velocity, ||q'|| << 1

We can throw away higher order term q', but keep q and q".
And also change cos(q) to 1, sin(q) to q.

{{<math>}}

## System subject to noice level 0: Random Walk
### 1. Discrete time and space
**Setting**: Particle in 1D. At each time step, the particle moves either left or right with step 1 with equal probability.

{{<math>}}
$$
\begin{aligned}
\Delta p (\Delta k, n) &\dot= \frac{1}{2}(\delta_{\Delta k,1}+\delta_{\Delta k, -1}) \\
p(k, n+1) &= (p * \Delta p)(k, n)
\end{aligned}
$$
{{</math>}}

Simply speaking, the probability distribution become more and more like a Gaussian distribution and wider and wider.

### 2. Continuous time and space
To write in SDE form,
{{<math>}}
$$
\begin{aligned}
dx &= dw \\
\end{aligned}
$$
{{</math>}}

## Level 1: Ornstein-Uhlenbeck Process
This is a forced machanical system consisting of a spring, mass and damper.
{{<math>}}
$$
\begin{aligned}
m\ddot{x} + c\dot{x} + kx &= f(t) \\
\end{aligned}
$$

m is mass, c is damping constant, k is spring stiffness, f is external force. This second order scalar equation can be written as two first order equations. We can define x1 = x, x2 = x'. Then

$$
\begin{aligned}
\begin{pmatrix} dx_1 \\ dx_2 \end{pmatrix}
=
-\begin{pmatrix} 0 & -1 \\ k/m & c/m \end{pmatrix}
\begin{pmatrix} x_1 \\ x_2 \end{pmatrix}
dt
+
\begin{pmatrix} 0 \\ 1/m \end{pmatrix}
dw
\end{aligned}
$$
This is essential saying that
$$
\begin{aligned}
\frac{dx}{dt} &= \dot x \\
m \frac{d\dot x}{dt} &= -c\dot x - kx + dw \\
\end{aligned}
$$
{{</math>}}

## How to get Fokker-Planck Equation from SDE
### 