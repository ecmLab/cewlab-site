---
layout: page
permalink: /research/
title: research
description: Reactive mechanics of solid-state materials for energy, microelectronics, and the environment.
nav: true
nav_order: 1
redirect_from:
  - /research-energy-storage
  - /reverse-osmosis-membrane
  - /vision-proposal
  - /copy-of-reverse-osmosis-membrane
---

Our work is on **solid-state materials for sustainable energy and environment**. In ionic ceramics,
electrodes, and ion-gated microelectronics, microstructure and properties evolve while the device
operates — so the processing–structure–property relation never closes.

We ask two questions. **What does stress do to a material reaction** when the constitutive response
is itself a state variable? And **how does the competition between mechanics and electrochemistry
decide performance?** We pursue both by modeling and by experiment.

That question defines a field we call **reactive mechanics** (Thrust I), which we then apply in
**energy storage** (II), **microelectronics** (III), and **environmental separation** (IV).

---

## Thrust I — Reactive mechanics and the mesoscale structure–property relation

Chemo-mechanical modeling of material reactions is well developed at the continuum level, and stress
from phase transformation is routinely included. But how fast an ion inserts, a metal deposits, or a
phase forms depends on **local stress**, and almost no model lets stress feed back into that rate.

A pressed or sintered pellet is also not a continuum. It carries load through the few contact points
where particles actually touch, and those contacts slide, rotate, and flatten during consolidation —
behavior the standard constitutive library does not describe. Grains rearrange and pores close during
densification; afterwards ions move through that microstructure and slowly take it apart. Reactive
mechanics aims to describe this mechano-electrochemical process with **one constitutive law**.

<figure class="cew-figure">
  <img src="{{ '/assets/img/thrusts/t1-reactive-mechanics.png' | relative_url }}" alt="Three scales of reactive mechanics: nano- and micro-mechanical testing, granular dynamics, and the TECM framework with an AI surrogate." loading="lazy">
  <figcaption><strong>Three scales of reactive mechanics.</strong> (A) Nano- and micro-mechanical tests isolate a single crystal or a fully charged agglomerate and return modulus, hardness, and fracture strength at a chosen state of charge. (B) Granular dynamics resolves composite-cathode behavior — viscoplastic deformation and electro-chemo-mechanical cycling. (C) The TECM framework trains an AI surrogate on simulated data and closes the loop against collaborative experiments.</figcaption>
</figure>

**Multiscale coupling with first-principles calculations.** What is a contact or interface made of
under reaction, across temperature? A contact is two surfaces in adhesive touch, and whether it bonds
or cracks is set by surface energy and by how easily ions and electrons cross it. We measure these
properties by nano- and micro-mechanics, isolating a single crystal or agglomerate and returning its
modulus, hardness, and fracture strength at a chosen state of charge. First-principles calculations
supply adhesion energies, the stability of interphases that grow between two solids, and the defect
chemistry that decides where electrons are available. The goal is a **map of properties against state
of charge** — stiffness, adhesion, and fracture strength set against first-principles prediction.

**Granular-to-continuum constitutive relation.** During densification, grains slide past one another
and rotate, their contacts flatten, and the material yields near full density. This deformation is
viscoplastic: how far a contact flattens depends on how fast local particles move — **granular creep**.
During cycling, active particles swell and shrink as ions enter and leave, and ionic diffusion shifts
as contacts open and close. We developed an electrochemically coupled granular-dynamics method in
which the electrochemical and mechanical problems are solved on the **same contact network**. Soil
mechanics predicts how a material deforms but knows nothing of reaction; a law carrying both would let
a material's whole history be computed in one framework.

**TECM and the AI-augmented digital twin.** We build the modeling platform — **TECM**,
thermo-electro-chemo-mechanics — that integrates first-principles results, mesoscale simulation, and
experimental data through machine learning. At material scale, models trained on first-principles
datasets accelerate calculations of ion transport and reaction. At cell scale, reduced surrogates open
the design space. At system scale, physics-informed models couple to experimental data for real-time
simulation. Conventional performance prediction uses cycling data alone; our digital twin takes
**fabrication data too**, carrying a material's whole history from synthesis to performance.

---

## Thrust II — Processing and degradation of ion-conducting ceramics and oxides

The global transition to clean energy needs storage that is dense, safe, and durable, from abundant
materials. Solid-state systems promise all of this — but they **fail mechanically before they fail
electrochemically**. A cell is consolidated from powder into a structure in seconds, then asked to
survive years of reaction.

<figure class="cew-figure">
  <img src="{{ '/assets/img/thrusts/t2-energy-storage.png' | relative_url }}" alt="Mechanics across the life of a solid-state electrochemical cell: dendrite issues, X-ray tomography of a cycling composite cathode, in-situ TEM of a solid-solid interphase, and a dry-processed electrode." loading="lazy">
  <figcaption><strong>Mechanics across the life of a solid-state electrochemical cell.</strong> (A) Dendrite failure recurs across many electrochemical systems. (B) X-ray tomography of a composite cathode during cycling; in-situ TEM applies a controlled force to a real solid–solid interphase. (C) A dry-processed electrode laminated onto Al foil.</figcaption>
</figure>

**Dendrite fracture and safety.** Dendrites find the pores and grain boundaries where electrons are
available, deposit there, and push outward against a brittle ceramic. Whether the ceramic **flows or
fractures** is set by how fast metal is forced in compared with how fast it creeps away — which is why
one ionic current is harmless to one cell and destroys another. The same competition appears in fuel
cells and electrolyzers. We model the stress-dependent charge transfer at the anode interface and test
the predictions with controlled fabrication and operation.

**Composite cathodes and interfaces.** Active materials breathe every cycle, and the catholyte is the
only phase that can absorb that motion — so catholyte selection is the design decision that matters.
We model and characterize the properties that govern accommodation: deformability, viscoplasticity,
and granular creep under sustained constraint. What decides contact retention is **how fast the
catholyte can flow during cycling, not how soft it is at an instant.** The aim is a rapid
material-discovery design principle for catholytes.

**Scale-up and dry manufacturing.** Dry processing removes the solvent and the drying oven, and leaves
mechanics in charge of the outcome. Mixing, calendering, and lamination have each been studied alone,
and little is known about how they couple; the first obstacle is simply a homogeneous distribution of
active material, carbon, and binder. We build predictive models for anode-free cells and
pouch-format manufacturing, and are working toward a dry-electrode design principle with a **predicted
processing window** — mixing energy, calendering and lamination pressure and temperature — that reaches
high capacity without losing adhesion.

---

## Thrust III — Chip-scale electrochemical microelectronics

Electrochemistry is moving onto the chip, and that does two things. It makes new **devices** — from a
memory element whose weight is an ion population, to a cell powering a MEMS device of a few mm². And
it makes **experiments that cannot be done in a larger cell**, because lithography controls the
architecture: electrode, electrolyte, and contact are all patterned. This thrust builds devices for
real applications and platforms that serve as clean instruments for calibrating the predictions of
Thrust I — here materials are clamped and patterned rather than packed with uncertainty.

<figure class="cew-figure">
  <img src="{{ '/assets/img/thrusts/t3-microelectronics.png' | relative_url }}" alt="On-chip electrochemical platforms: a side-gated ECRAM transistor, a microelectrode array carrying individual NMC particles, and a lateral micro-battery cell." loading="lazy">
  <figcaption><strong>On-chip electrochemical platforms.</strong> (A) A side-gated ECRAM transistor in which an electrolyte gates a 2D semiconducting channel, with ions redistributing under bias. (B) A microelectrode array carrying individual secondary NMC particles, each isolated on its own gold electrode, with voltage–capacity curves measured one particle at a time. (C) A lateral micro-battery cell, with cathode, electrolyte, and anode defined lithographically between Ti/Au contacts.</figcaption>
</figure>

**Electrochemical memory for neuromorphic computing.** Training a neural network costs energy largely
because weights travel between memory and processor; computing inside the memory removes that traffic.
**ECRAM** moves ions into a channel instead of switching a filament, giving hundreds of distinguishable
states that filamentary devices cannot supply. But write voltage, retention, and endurance are all set
at an interface governed by ion transport and strain. We modeled the electrical double layer between
an electrolyte-gated transistor and 2D channels, and found that the voltage needed to write a
non-volatile state depends strongly on **pulse frequency**. We are now after an atomistic understanding
of the double layer between two solids — how charge transfers, and how interphase formation affects
carrier transport.

**On-chip single-particle measurement.** A silicon chip carries an array of hundreds of gold
microelectrodes, passivated so only the tips are exposed. Individual electrode and ceramic particles
(1–10 µm) are placed one per electrode with a micromanipulator, and cycled one at a time at
**picoamp-hour resolution**. The same particle is then fractured under a flat-punch indenter in SEM —
so electrochemical history and mechanical strength are measured **on one particle**. The goal is to run
this across chemistries and states of charge until single-particle strength can be predicted from
cycling history alone, which would give Thrust I its constitutive input.

**Micro-batteries on a chip.** A microsensor, implant, or lab-on-chip device needs a power supply made
in the same fab as the device it powers, and a micro-battery is the only chemistry that can be
patterned. We build the cell laterally — cathode, electrolyte, and anode defined by lithography and
contacted through Ti/Au pads. In conventional fabrication the interface is produced by laminating two
components, and its area and contact state have to be inferred. **On a chip the interface is drawn:**
its area, geometry, and degree of confinement are set by the mask, and the same cell can be cycled
while it is imaged. That makes it the cleanest system available for isolating the quantities Thrust I
otherwise has to fit — contact area, interfacial adhesion, and confinement — each varied independently
by design rather than by processing.

---

## Thrust IV — Selective separation and recovery of critical elements

Clean water, secure supply chains for critical minerals, and the recycling of economically important
elements are central to a sustainable future. We work on **membrane-based electrochemical systems**
that serve both. Through collaborative experiments we study the transport of ions — Li⁺, Na⁺, K⁺,
Mg²⁺, Ca²⁺ — in aqueous solution and across a membrane separator under electric potential, coupling
ionic transport, electrochemistry, and fluid mechanics with AI-guided design.

<figure class="cew-figure">
  <img src="{{ '/assets/img/thrusts/t4-separation.png' | relative_url }}" alt="Electro-reactive deionization performance on industrial wastewater, aqueous quadrupole ion traps separating microspheres, and AI-augmented modeling of rare-earth recovery with a functionalized GO membrane." loading="lazy">
  <figcaption><strong>Separation and recovery.</strong> (A) Performance of our electro-reactive deionization system across industrial wastewater streams. (B) Aqueous ion-trap testing for microsphere separation. (C) AI-augmented modeling of rare-earth recovery with an agent-functionalized GO polyanion membrane.</figcaption>
</figure>

**Energy-efficient industrial wastewater treatment.** We developed an **electro-reactive deionization**
device that couples capacitive behavior with a selective ion-exchange membrane and cathode material,
removing inorganic dissolved solids — heavy metals, PFAS, corrosive salts — from wastewater and other
solvents. The system reduces hazardous discharge, recycles treated water for direct reuse in industrial
processes, and lessens reliance on chemical treatment. We are extending it to transition-metal
dichalcogenides such as MoS₂ that react with hazardous ions like Cr(VI), and to the charge-transfer
reactions that govern them.

**Membrane-free ion separation with aqueous quadrupole ion traps.** We develop aqueous **quadrupole
ion traps** to study ion transport in liquid and to target separation without a membrane at all.
Proof-of-concept experiments with charged microspheres show that ion traps can reliably control
particle motion in aqueous environments, opening a path toward scalable, membrane-free, solvent-free
separation — with applications in desalination, precision contaminant removal, and biochemical
separation.

**Closed-loop recovery of ion conductors and critical elements.** We target the circularity of silicon
and critical materials — particularly rare earths such as cerium and neodymium — from mixed
photovoltaic waste. Through collaboration we develop membrane-based separation models to recover rare
earth elements, using AI-augmented modeling of ion–membrane interactions to guide scalable platforms
that operate under mild aqueous conditions.

---

A complete, continuously updated list of the lab's papers is on the
[publications page]({{ '/publications/' | relative_url }}).
