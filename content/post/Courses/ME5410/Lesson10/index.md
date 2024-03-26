---
title: Conventional Fabrication
subtitle: ME5410 Lesson 10

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

## Soft robot
definition: soft machines that can actively interact with the environment and undergo large deformations relying on inherent or structural compliance

emulation from soft-bodied animals

advantages: adaptability, conformability, safety

### Soft robot tier
1. conventional + compliance passively
2. primary function achieved fully or partially by soft elements, making up significant portion of the body
3. entire soft, external hard components
4. soft, no hard components


### Elastomer
polymer with viscosity and elasticity: viscoelastic
- viscous: the ability to flow (黏性)
- elastic: the ability to return to original shape after deformation (弹性)
- low young's modulus, high failure strain
- regain original shape after large deformation

#### Thermoset ones
- glass transition temperature < room temperature
- intermolecular bond + **covalent bond**(inreversible) = crosslink
- the above two is formed during curing or crosslinking
- chemical reaction during molding at high temperature
- Advantages:
    - chemical resistance
    - thermal stability

#### Thermoplastic ones
- no crosslinking during molding
- melt-processable or reprocessable
- Advantages:
    - recyclable
    - ease of compounding
    - ease of molding

## Untethered soft robot
Definition: essential components (control, actuation, power, sensing) are fully integrated (embedded) within its own structure

Disadvantages: bulky on-board components

## Soft actuation
1. pneumatic
2. phase transition
3. combustion
4. electrostatic
5. biological actuation

## stretchable electronics
1. out-of-plane
    - buckled film (扣带膜，像波浪一样)
    - origami shaped (折纸, 把纸剪开折叠)
    - they are out of plane because they are not flat, they are 3D
2. in-plane
    - serpentine (蛇形) and fractal (分形)
    - percolating (渗透, 先生成一个网格, 然后在网格上生成电路)
    - they are in plane because they are flat, they are 2D
3. stretchable composites
    - stretchable interconnects (e.g. eHelix), components are solid but the "wires" are stretchable
    - stretchable electronics

## Self-healing
- more durable, sustainable
- single-time (extrinsic) vs repeated (intrinsic, without external healing agent)
- stimuli for healing (high temp, Hp, UV) vs automatic 
healing

## Additive manufacturing
Advantages:
- customization
- complexity
- sustainability / environmental friendly
    - less material waste
    - moldless

### Classification
1. Vat photopolymerization (光固化)
    - SLA (stereolithography, 光固化), liquid based
2. Material extrusion (材料挤出)
    - FDM (fused deposition modeling, 熔融沉积建模)
3. Powder bed fusion (粉末熔融)
    - SLS (selective laser sintering, 选择性激光烧结)
4. Binder jetting (粘结喷射)
    - powder + liquid based
5. Material jetting (材料喷射)
    - inkjet, liquid based
6. Directed energy deposition (定向能量沉积)
    - powder based
7. Sheet lamination (层压)
    - solid sheet based

### SLA
- Sterolithography apparatus (立体光刻机)
- liquid based
- material: photopolymer resin (光敏树脂)
- highly detailed parts: smooth surface, tight tolerances
- thermoset

### FDM
- Fused deposition modeling (熔融沉积建模)  
- material: thermoplastic filament (热塑性丝) ABS, PLA
- low dimensional accuracy, low surface quality
- visible layer lines
- thermoplastic

### SLS
- Selective laser sintering (选择性激光烧结)
- material: thermoplastic powder (热塑性粉末)
- slightly grainy surface
- no support structure needed
- thermoplastic

## Opportunities
### Metal 3D printing
### Electronics 3D printing

1. Inkjet printing (喷墨打印)
2. Aerosol jet printing (气溶胶喷射打印)
3. DIW (direct ink writing) (直接墨水书写)
4. E-jet / EHD (electrohydrodynamic) printing (电流体动力学打印)

Materials:
- conductive / semiconductive ink: metal np(metal nanoparticles), carbon, conductive polymer
- substrates (基板): paper, polymer, textile(纺织品), tattoo, curvy surface
- dielectric ink
- adhesive 
- electronic components