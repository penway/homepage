---
title: Robotics Kinematics Lesson 1
subtitle: Notes for ME5421

# Summary for listings and search engines
summary: Robotics Kinematics

# Link this post with a project
projects: [ME5421]

# Date published
date: '2023-08-13T00:00:00Z'

# Date updated
lastmod: '2023-08-14T00:00:00Z'

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: 'Image credit: [**Unsplash**](./featured.jpg)'
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- penway

tags:
- 

categories:
- Course Notes

gallery_item:
- album: 
  image:
  caption:

share: false
---

**This Blog will continue to be updated as the course progresses. Notes, code and ideas will be added as I go along. Check out the course notes at the top ↑ ;)**

{{< toc >}}

## Introduction
Introduction, Spatial Descriptions and Transformations, Manipulator Forward and Inverse Kinematics, Mechanics of Robot Motion, Static Forces and Torques

Lecturer: [Prof Marcelo H. Ang Jr](https://cde.nus.edu.sg/me/staff/ang-jr-marcelo-h/)

## Contents
### 1. Introduction, Spatial Descriptions and Transformations
Robot definition. Robot classification. Robotics system components. Notations. Position definitions. Coordinate frames. Different orientation descriptions. Free vectors. Translations, rotations and relative motion. Homogeneous transformations.

### 2. Manipulator Forward and Inverse Kinematics
Link coordinate frames. Denavit-Hartenberg convention. Joint and end-effector Cartesian space. Forward kinematics transformations of position. Inverse kinematics of position. Solvability. Trigonometric equations. Closed-Form Solutions. Workspace.

### 3. Mechanics of Robot Motion
Translational and rotational velocities. Velocity Transformations. The Manipulator Jacobian. Forward and inverse kinematics of velocity. Singularities of robot motion.

### 4. Static Forces and Compliance
Transformations of static forces and moments. Joint and End-Effector force/torque transformations.


## Start of Lesson 1

Overview:

Advice: understand all the time, ask questions at real-time!
understand + pratice problem solving
try sample questions3
contact TA for research

Robotics need knowledge from: [ME, EE, CS] + Social Science (Understand Humanity) + Business (Commercial) + Ethics

Robots do things that
1. too intelligent to do
  - dangerous
  - dull
  - dirty
  - degrading
  - demeaning
2. Human cannot do as well as machine
  - precision

Autonomous Driving is both!

A Typical Robot System: Sensing+Understanding, Planning, Exceuting, Learning

## Basic Kinematics

some manipulater:
  - hand: end-effecter
  - embrace: whole body manipulation

Base(Link0) - Joint1 - Link1 - Joint2 - Link2
Joints: Sliding-Translational, Rotating-Rotational

### Workspace
The space reachable by last link is called the workspace(sometimes, arm workspace)

Arm (primarily resposible for corase positioning) link 123(Cartesian Robot) + Wrist (fine positioning) link 456

Orientation worksapce: set of all possible orientations reachable

### Cartesian， Cylinrical， Spherical Robot
T: translation joint; R: rotation joint

**Cartesian Robot**: TTT RRR

**Cylinrical Robot**: RTT RRR

**Spherical Robot**: RRT RRR

So when we are talking about spherical or cylindrical or cartesian robot, we are talking about the first 3 links, i.e. arm workspace
( sometimes changing size of link will be same in kinematics, but not in dynamics )

### SCARA: Selective Compliant Assembly Robot Arm: RRT RRR; ISO 8373:2012

**accerleration**: m + b + k + G
(mass: overcome inertia, damping: overcome friction (air, water, etc.), stiffness: if there is a spring in the system, gravity)

SCARA can be fast because the first two links do not need to overcome gravity
GearBox(theta_N to theta_1): more torque, less speed, (most of the motor has gearbox, which are not back-drivable, or else it will be back-drivable)
Advantage for back-drivable: motor-generator; human-robot interaction; hitting will turned into voltage change, providing compliance
So SCARA is seletivly comliant, the first two links are back-drivable
Back-drivable with gearbox: add a sensor (put is a the end of the pole)


### Articulated Robot Arm: RRR RRR

Rotational joint can change orientation and position at the same time while prismatic joint can only change position

Human is fully articulated (waist, shoulder, elbow, wrist, fingers)

When using a joint, one should consider: joint style and joint range motion, because some joint have limited range of motion

6 joints because 6 DOF, 6 independent variables -> 6 DOF

sphereal joint = 3 DOF! because 3 independent variables (human shoulder, wrist)

if you have more joints that 6, you can have redundant motion, like stay your hand put but moving elbow, which is great
- increase dexterity
- increase robustness
- increase flexibility


### Parallel Robot
robot that has more than one end-effector, like with two arms

increase payload, increase stiffness

### Service Robot
### Collaborative Robot (Co-X, CoBot)
ISO: robot will stop when hit something
universal robot will sense the current to stop, but not very accurate, and it is not back-drivable
impedance control: if you have force torque sensors in joints, you can control the dynamics that is not physical
appearant mass, appearant stiffness, appearant damping


## Chapter 1: Introduction, Spatial Descriptions and Transformations

Position of point O in frame A
{{< math >}}
$$
^AP_O = \begin{bmatrix} ^AP_{OX} \\ ^AP_{OY} \\ ^AP_{OZ} \end{bmatrix} \in \mathbb{R}^3
$$
{{< /math >}}

#### Rotataion Matrix
If object B is in frame A and the frame B attached to B is {{< math >}} $ ^Ai_B, ^Aj_B, ^Ak_B $ {{< /math >}}, then
{{< math >}}
$$
^AR_B = \begin{bmatrix}
^Ai_{Bx} & ^Aj_{Bx} & ^Ak_{Bx} \\
^Ai_{By} & ^Aj_{By} & ^Ak_{By} \\
^Ai_{Bz} & ^Aj_{Bz} & ^Ak_{Bz}
\end{bmatrix} \in \mathbb{R}^{3 \times 3}
$$
$$ det(^AR_B) = +1 $$
R is a Proper Orthogonal Matrix
$$
^AR_B^{-1} = {^AR_B^T} = {^BR_A} \\
{^AR_B} {^AR_B^T} = {^BR_A} {^AR_B} = I
$$
{{< /math >}}
But only three parameters are needed to describe the rotation matrix, so we can use Euler Angles, Axis-Angle, Quaternions, etc.

