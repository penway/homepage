---
title: Actuators
subtitle: ME5410 Lesson 8

summary: Material, Sensors, Actuators and Frabrication
projects: [ME5410]

date: '2023-10-23T00:00:00Z'
lastmod: '2023-10-23T00:00:00Z'

draft: false
featured: false

authors:
- penway

categories:
- Course Notes
- ME5410

share: false
---

Actuator: accept control command, produce a change in the physical system by generating {force, heat, flow, etc}
Energy -> Motion, etc

Actuator = Trannsducer(Must) + Energy Source(Optional) + Motion Converter(Optional)

Rotary vs Linear
Tethered (external power, control sys) vs Untethered (onboard power and control sys)
Hard vs Soft

## Classification on Actuation Mechanisms
1. Electrical
    - two state: on/off, like electrically operated switch

2. Electromechanical
    - DC, AC, Stepper Motor
    - Linear/rotary, Hard, Tethered
3. Electromagnetic
    - DC/AC solenoid (Linear)
    - Linear/rotary, Hard, Tethered
4. Hydraulic(液压) and 5. Pneumatic(气动)
    - Hy: pressurized oil, Pn: pressurized gas
    - Rotary: low speed high torque
    - Linear piston
    - Control valve
** The above are all Linear/rotary, Hard, Tethered **
X. Smart Materials

## Elastic Actuator
Linear/rotary, Hard, Tethered, hard but elastic

Electric motor: Encoder + Reducer (Gearbox) + Power Amplifier + Motor + Control Unit

## [Can be important] Actuator Selectioin Criteria
- Couninuous Power Output
- Range of Motion
- Resolution
- Accuracy
- Peak force/torque
- Heat dissipation
- Speed characteristics: Force(torque) - speed curve
- No load speed
- Frequency response
- Power requirement

## Soft Actuation (almost =) Artificial Muscle
- Pneumatic 一些有趣的，气球，
    - McKibben Artificial Muscle
    - Micro McKibben，模拟肌肉纤维
    - 大象鼻子
- phase transition
    - shape memory alloy
    - shape memory polymer: temp, humidity, light, driven
- combustion
- electrostatic force   