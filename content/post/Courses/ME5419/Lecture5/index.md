---
title: Trajectory for Manipulation, ProbMAN 5
subtitle: Probabilistic Robotics Lecture 

summary: Probabilistic Robotics
projects: [ME5419]

date: '2023-09-28T00:00:00Z'
lastmod: '2023-09-28T00:00:00Z'

draft: false
featureSigma_d: false

authors:
- penway

categories:
- Course Notes
- Probabilistic Robotics
---

## Precursor
What is manipulation? 
- Prehensile manipulation: grasp and move, We have manipulator arm, we have screws (Mostly talked)
- Nonprehensile manipulation: move without grasp, We have assembly line, there are passive fences to guide the object (Less talked)

## Geometry of Manipulation

### Curves (Path and Trajectory), and parameterization
- Path is a continuous function from some variable to the space. This variable is called parameter. It can be time, arc length, etc.
- Trajectory is a path, plus a velocity for each point on the path.

#### Arc Length Parameterization
{{<math>}}
$$
\begin{aligned}
s(t_2) - s(t_1) &= \int_{t1}^{t2}(x'(t), x'(t))^{1/2}dt \\
u(t) &\dot{=} \frac{1}{||x'(t)||}x'(t) \\
\end{aligned}
$$
When $t=s$, i.e. parameter is arc length,
$$
u(s) = \frac{dx}{ds}
$$
Since $u(s)$ is a unit vector, we can write
$$
\frac{d}{ds}(u\cdot u) = 0 \Rightarrow u \cdot \frac{du}{ds} = 0
$$
{{</math>}}

#### Curvature
{{<math>}}
$$
\begin{aligned}
\kappa(s) &= (\frac{du}{ds} \cdot \frac{du}{ds})^{1/2} = (\frac{d^2x}{ds^2} \cdot \frac{d^2x}{ds^2})^{1/2} \\
n_1(s) &\dot{=} \frac{1}{\kappa(s)}\frac{du}{ds} \\
\kappa(s) &= 
\end{aligned}
$$
{{</math>}}