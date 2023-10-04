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

### Unsigned Curvature
Kappa is the unsigned curvature. N1 is the (principal) normal vector.
{{<math>}}
$$
\begin{aligned}
\kappa(s) &= (\frac{du}{ds} \cdot \frac{du}{ds})^{1/2} = (\frac{d^2x}{ds^2} \cdot \frac{d^2x}{ds^2})^{1/2} = ||u'(s)|| \\
n_1(s) &\dot{=} \frac{1}{\kappa(s)}\frac{du}{ds} \\
\end{aligned}
$$
{{</math>}}


**Example: Circle**
{{<math>}}
$$
\begin{aligned}
x_1(s) &= r\cos(\frac{s}{r}) \\
x_2(s) &= r\sin(\frac{s}{r}) \\
\end{aligned}
$$
Actually this needs experience to know this perfect parameterization. $$ $$
The second part is the calculate the unit tangent vector. Only this derivative is naturally unit. (by good parameterization)
$$
\begin{aligned}
& u_1(s) = x_1'(s) = -\sin(\frac{s}{r}) \\
& u_2(s) = x_2'(s) = \cos(\frac{s}{r}) \\
& u_1^2(s) + u_2^2(s) = 1 \\
& u_1'(s) = -\frac{1}{r}\cos(\frac{s}{r}) \\
& u_2'(s) = -\frac{1}{r}\sin(\frac{s}{r}) \\
\end{aligned}
$$
And we can see that
$$
u'(s) = \frac{1}{r}\begin{pmatrix} -c \\ -s \end{pmatrix} \\
\therefore \kappa(s) = ||u'(s)|| = \frac{1}{r}
$$
{{</math>}}

### Signed Curvature
{{<math>}}
$$
\begin{aligned}
k(s) = \sigma(s)\kappa(s)
\end{aligned}
$$
{{</math>}}

**Example:  curve**
{{<math>}}
$$
\begin{aligned}
y &= x^3 \\
x(t) &= t \\
y(t) &= t^3 \\
x'(t) &= 1 \\
y'(t) &= 3t^2 \\
\kappa(t) &= \sqrt{x'^2(t) + y'^2(t)} = \sqrt{1 + 9t^4} \\
\sigma(t) &= \frac{y''(t)x'''(t) - x''(t)y'''(t)}{\kappa^3(t)} = \frac{6t^2}{\kappa^3(t)} \\
\end{aligned}
$$
{{</math>}}