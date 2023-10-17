---
title: Sensors
subtitle: ME5410 Lesson 7

summary: Material, Sensors, Actuators and Frabrication
projects: [ME5410]

date: '2023-08-15T00:00:00Z'
lastmod: '2023-08-15T00:00:00Z'

draft: false
featured: false

authors:
- penway

categories:
- Course Notes
- ME5410

share: false
---

Transducer: A device that converts one form of energy to another. Can be used as a sensor or actuator.

Sensor: sense a physical quantity and convert it to an measurable (usually electrical) signal. One or more transducers.

## Classification
1. By Measured: Temperature, Position, Pressure, Force, Flow, Level, Gas(Chemical)
2. By Tech: Electrical, Optical, Magnetic, Mechanical
3. contact vs non-contact; passive vs active; analog vs digital

## Sensor Characteristics
1. **Transfer Function**
2. **Range**: min and max values
3. **Saturation**: max-out
4. **Deadband**: range where no output, usually around zero
5. **Hyteresis**: difference between up and down
6. **Linearity**: deviation from line
7. **SNR**
8. **Error**: systematic(bias), precision(random)
9. **Accuracy**: how close to true value
10. **Precision**(Repeatibility): how close each measurement
11. **Resolution**: smallest change that can be reliably detected
12. **Stability**: keep characteristics over time
13. **Zero Offset**: output when input is zero
14. **Zero Drift**: Zero Offset changes over time
15. **Response Time**
16. **Operating Temperature**

X. **Calibration**: determine transfer function
X. **Calibration Cycle**: up and down (for hysteresis)

## Sensor in Robotics
1. Extroception vs Proprioception: external vs internal
2. Position and Proximity Sensors
    - potentiometer: 电位器
    - capacitive proximity sensor: 电容接近传感器，可用于非金属测量距离
    - hall effect sensor: 霍尔传感器
    - ultrasonic sensor
3. Touch Sensors
    - Contact sensor
    - Tactile sensor: pizeoresistive, capacitive, 
    - Force sensor
4. Vision Sensors
    - CCD and CMOS
    - Infrared 红外
    - ToF: time of flight, 通过测量光的往返时间来测量距离, 但是精度不高，但是便宜
    - LiDAR: light detection and ranging, 通过测量光的往返时间来测量距离, 精度高，但是贵
    - Radar: radio detection and ranging