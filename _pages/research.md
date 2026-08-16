---
layout: page
permalink: /research/
title: research
description: Electro-chemo-mechanics of solid-state batteries and capacitive deionization.
nav: true
nav_order: 1
redirect_from:
  - /research-energy-storage
  - /reverse-osmosis-membrane
  - /vision-proposal
  - /copy-of-reverse-osmosis-membrane
---

The CEW Lab studies how **mechanics, chemistry, and transport couple** in electrochemical systems.
One framework — electro-chemo-mechanics — underpins two application areas: **energy storage** and
**water purification**. Below, each thrust lists the active projects and the papers that ground them.

---

## Solid-state batteries for energy storage

All-solid-state batteries (SSBs) are a promising next-generation technology, offering improved safety
and energy density over liquid-electrolyte cells. Limited cycle life is what still blocks practical
deployment. Degradation during cycling has several coupled causes — dendrites growing from the anode
through the solid electrolyte, and microstructural degradation of the composite cathode. Theoretical
methods that capture these mechanisms are what let us design materials and structures instead of
screening them by trial and error.

<figure class="cew-figure">
  <img src="{{ '/assets/img/cards/energy.jpg' | relative_url }}" alt="Composite-cathode and solid-electrolyte microstructure — the length scale where chemo-mechanical degradation sets cycle life." loading="lazy">
  <figcaption>Composite-cathode and solid-electrolyte microstructure — the length scale where chemo-mechanical degradation sets cycle life.</figcaption>
</figure>

**Project 1 — Dendrite growth at the Li-metal anode / solid-electrolyte interface.**
Electrodeposition and mechanical stability at the interface during plating; the role of creep and
plastic flow of the metal; how mixed ionic–electronic conduction drives metal propagation into the
electrolyte; and dendrite suppression by detouring Li transport in a mechanically anisotropic
electrolyte.

**Project 2 — Microstructure optimization of the composite cathode.**
Growth and in-situ compression of primary and secondary NMC particles; clustering and volume
expansion of secondary particles; particle-size optimization for high active-material loading; and
intergranular degradation of secondary NMC in liquid versus solid-state environments. Two US patent
applications cover the resulting cathode designs.

**Project 3 — Solid-electrolyte degradation and processing.**
Degradation of the solid electrolyte over cycling, granular creep and its role in optimizing
electrolyte fabrication, minimizing volume change and stack pressure, anode-free architectures,
operando monitoring of cathode microstructure with wireless sensors, and closed-loop recycling of
sulfide solid electrolytes from spent sodium cells.

---

## Capacitive deionization for water purification

Freshwater scarcity and rising demand are already critical across arid regions. Capacitive
deionization (CDI) desalinates water using charged electrodes and is energy-efficient,
cost-effective, and environmentally benign. Better membrane and electrode materials are what set its
ceiling, and computational investigation is how we get there faster than synthesis alone allows.

<figure class="cew-figure">
  <img src="{{ '/assets/img/cards/water.jpg' | relative_url }}" alt="Ion and water transport through nanoconfined channels, resolved by molecular dynamics." loading="lazy">
  <figcaption>Ion and water transport through nanoconfined channels, resolved by molecular dynamics.</figcaption>
</figure>

**Project 1 — Transport in membranes and CDI channels.**
Ion and water transport mechanisms in CDI channels and ion-exchange membranes; interlayer spacing
and separation capability of graphene-oxide membranes in organic solvents; swelling of GO membranes
in aqueous solution; and the effect of osmotic pressure on the permeability of carbon-based 2D
materials.

**Project 2 — Selective ion capture and heavy-metal removal.**
Harvesting lithium from brine and seawater with flow-CDI; Li⁺ separation from divalent cations
across crown-ether-functionalized GO membranes; selective lead adsorption and filtration with MoS₂
nanosheets and membranes; and the aqueous stability of those membranes.

**Project 3 — Novel desalination architectures.**
Rotating carbon-nanotube membrane filters, scale-up nanoporous membrane centrifuges for
fouling-free reverse osmosis, and molecular-dynamics study of rotational nanofluids for desalination.

---

## Electro-chemo-mechanics as a general framework

Underneath both application areas is a single modeling framework that couples solid mechanics, ion
and electron conduction, electrodeposition, and fracture — Butler–Volmer reaction kinetics, diffusion
and migration in the active material, phase segregation, electronic conduction, and fracture
criteria, solved across steady-state, time-dependent, and fully coupled formulations.

<figure class="cew-figure">
  <img src="{{ '/assets/img/cards/framework.jpg' | relative_url }}" alt="Microstructure of the composite cathode, from electron microscopy through to the discrete-element representation used in simulation." loading="lazy">
  <figcaption>Microstructure of the composite cathode, from electron microscopy through to the discrete-element representation used in simulation.</figcaption>
</figure>

Building that framework is a research thrust in its own right, and spans density functional theory,
molecular dynamics, the finite element method, phase-field modeling, and discrete-element and CFD
treatments of microstructure. Two further directions extend it: **data-driven microstructural
optimization** of composite structures, and **AI-based decision-making** for automated synthesis.

This thrust also carries the lab's earlier and continuing work in computational mechanics —
updated Lagrangian particle hydrodynamics (ULPH) for Newtonian fluids, interphase models for
nanoparticle–polymer and concrete composites, high-temperature nanoindentation, and crosslinked
polymer networks.

---

## Where the thrusts meet

Energy storage and water purification are not separate programs here. A patented **hybrid
CDI–solid-state-battery device** combines the two: energy generation together with lithium capture,
using a composite cathode, solid electrolyte, and ion-exchange membrane in one stack.

---

A complete, continuously updated list of the lab's papers is on the
[publications page]({{ '/publications/' | relative_url }}).
