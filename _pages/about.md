---
layout: about
title: about
permalink: /
subtitle: >
  <strong>Clean Energy and Water Laboratory</strong> · Department of Mechanical Engineering ·
  <a href="https://www.rit.edu/engineering/">Kate Gleason College of Engineering</a> ·
  Rochester Institute of Technology

# The hero carries the lab's identity, so the theme's profile sidebar is disabled —
# it would repeat the logo and push the opening paragraph into a narrow column.

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true
  limit: 3
---

<div class="cew-hero" style="--cew-hero-img: url('{{ '/assets/img/hero/lab-team.jpg' | relative_url }}');">
  <div class="cew-hero__inner">
    <img class="cew-hero__logo" src="{{ '/assets/img/brand/logo-white.png' | relative_url }}" alt="CEW Lab">
    <h1 class="cew-hero__title">Materials set what a cell could store. Mechanics decides how long it survives storing it.</h1>
    <p class="cew-hero__sub">
      The Clean Energy and Water Laboratory studies how solids deform while they react — the
      coupling that limits solid-state batteries and separation membranes — at RIT's Kate Gleason
      College of Engineering.
    </p>
    <div class="cew-hero__cta">
      <a class="cew-btn cew-btn--primary" href="{{ '/research/' | relative_url }}">Our research</a>
      <a class="cew-btn cew-btn--ghost" href="{{ '/joinus/' | relative_url }}">Join the lab</a>
    </div>
  </div>
</div>

A battery is a structure that changes shape while it works. Lithium plates into a ceramic that
cannot accommodate it, cathode particles swell and crack away from their conductive network, and a
separator that was mechanically sound at assembly is fractured after fifty cycles.

In ionic ceramics, electrodes, and ion-gated microelectronics, microstructure and properties evolve
while the device operates — so the processing–structure–property relation never closes. We ask what
**stress does to a material reaction** when the constitutive response is itself a state variable, and
how the competition between mechanics and electrochemistry decides performance.

We call that question **reactive mechanics**, and we pursue it by modeling and by experiment — then
apply it across **energy storage**, **chip-scale microelectronics**, and **environmental separation
and critical-element recovery**.

<div class="cew-stats">
  <div class="cew-stats__inner">
    <div><span class="cew-stats__n">{{ site.data.scholar.citations_display }}</span><span class="cew-stats__l">Citations</span></div>
    <div><span class="cew-stats__n">{{ site.data.scholar.h_index }}</span><span class="cew-stats__l">h-index</span></div>
    <div><span class="cew-stats__n">{{ site.data.scholar.publications }}</span><span class="cew-stats__l">Publications</span></div>
    <div><span class="cew-stats__n">2021</span><span class="cew-stats__l">Lab founded</span></div>
  </div>
  <div class="cew-stats__note">
    Citations and h-index from
    <a href="https://scholar.google.com/citations?user={{ site.data.scholar.scholar_id }}&amp;hl=en">Google Scholar</a>,
    updated {{ site.data.scholar.updated_display }}.
  </div>
</div>

## Research thrusts

<ul class="cew-cards">
  <li class="cew-card">
    <img src="{{ '/assets/img/thrusts/t1-reactive-mechanics.png' | relative_url }}" alt="Reactive mechanics research" loading="lazy">
    <div class="cew-card__body">
      <h3 class="cew-card__title">Reactive mechanics</h3>
      <p class="cew-card__text">One constitutive law for a reacting solid: stress feeding back into reaction rate, granular creep during densification, and a thermo-electro-chemo-mechanical framework with an AI surrogate.</p>
      <a class="cew-card__link" href="{{ '/research/' | relative_url }}">Read more →</a>
    </div>
  </li>
  <li class="cew-card">
    <img src="{{ '/assets/img/thrusts/t2-energy-storage.png' | relative_url }}" alt="Energy storage research" loading="lazy">
    <div class="cew-card__body">
      <h3 class="cew-card__title">Energy storage</h3>
      <p class="cew-card__text">Solid-state cells fail mechanically before they fail electrochemically. Dendrite fracture, composite-cathode accommodation, and dry-processed scale-up.</p>
      <a class="cew-card__link" href="{{ '/research/' | relative_url }}">Read more →</a>
    </div>
  </li>
  <li class="cew-card">
    <img src="{{ '/assets/img/thrusts/t3-microelectronics.png' | relative_url }}" alt="Microelectronics research" loading="lazy">
    <div class="cew-card__body">
      <h3 class="cew-card__title">Microelectronics</h3>
      <p class="cew-card__text">Electrochemistry on the chip: ECRAM for neuromorphic computing, single-particle measurement at picoamp-hour resolution, and lithographically defined micro-batteries.</p>
      <a class="cew-card__link" href="{{ '/research/' | relative_url }}">Read more →</a>
    </div>
  </li>
  <li class="cew-card">
    <img src="{{ '/assets/img/thrusts/t4-separation.png' | relative_url }}" alt="Separation &amp; recovery research" loading="lazy">
    <div class="cew-card__body">
      <h3 class="cew-card__title">Separation &amp; recovery</h3>
      <p class="cew-card__text">Electro-reactive deionization for industrial wastewater, membrane-free separation with aqueous ion traps, and closed-loop recovery of rare earths.</p>
      <a class="cew-card__link" href="{{ '/research/' | relative_url }}">Read more →</a>
    </div>
  </li>
</ul>

<div class="cew-band">
  <div class="cew-band__inner">
    <h2>We are hiring</h2>
    <p>
      The CEW Lab has openings for <strong>MS and PhD students and postdoctoral researchers</strong>
      in both research directions. Experience with electrochemistry is welcome but not required to
      start — we look for a background in solid or fluid mechanics and in continuum or atomic-scale
      modeling.
    </p>
    <a class="cew-btn cew-btn--primary" href="{{ '/joinus/' | relative_url }}">See openings</a>
  </div>
</div>
