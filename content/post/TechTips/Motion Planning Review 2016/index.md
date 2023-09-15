---
title: Paper Reading - A Review of Motion Planning Techniques for Automated Vehicles
subtitle: Motion Planning

summary: 
projects: [Paper Reading]

date: '2023-08-17T00:00:00Z'
lastmod: '2023-08-17T00:00:00Z'

draft: false
featured: false

authors:
- penway

categories:
- Paper_Reading
---

This note is only a fast review and understanding of the paper, which is more well organized than my note. This note skip every detail of any algorithm, and only focus on the big picture. (As we are doing deep learning, these algorithms are not that important, but the big picture is.)

## Planners

### 1. Graph Based Planners

**State Space Representation**
- Gird State Space. The graph is constructed by connecting the neighboring cells.
- State Lattice. It uses a set of predefined paths reffered as *state lattice*, which is used to discretize the state space. And graph search algorithm such as A* is used.

**Graph Search Algorithm**
- Dijkstra's [some thing good on YouTube](https://www.youtube.com/watch?v=EFg3u_E6eHU)
- A* [video I found useful](https://www.youtube.com/watch?v=71CEj4gKDnE) [beautifully explained](https://www.youtube.com/watch?v=A60q6dcoCjw)tab

### 2. Sampling Based Planners

These methods take samples in the state space, and looking for a path connecting the start and goal state. The path is constructed by connecting the samples. The path is not optimal, but it is fast.

- Probabilistic Roadmap (PRM)
- Rapidly-exploring Random Tree (RRT)

### 3. Interpolating Curve Planners