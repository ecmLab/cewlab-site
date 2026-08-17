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

That coupling — **reactive mechanics**, the behavior of solids that deform while they react — is
what we study, and it is the barrier standing between solid-state batteries and the manufacturing
scale-up the field is now attempting. The same physics governs ion transport through a membrane
under load, so our program spans two application domains that share a mechanism: **electrochemical
energy storage**, and **separation and recovery of critical materials**.

Both are pursued the same way — first-principles and machine-learned simulation to establish
mechanism, continuum modeling to reach device scale, and in-house electrochemistry to test the
prediction.

{% assign s = site.data.scholar %}
<div class="cew-stats">
  <div class="cew-stats__inner">
    <div><span class="cew-stats__n">{{ s.citations_display }}</span><span class="cew-stats__l">Citations</span></div>
    <div><span class="cew-stats__n">{{ s.h_index }}</span><span class="cew-stats__l">h-index</span></div>
    <div><span class="cew-stats__n">{{ s.publications }}</span><span class="cew-stats__l">Publications</span></div>
    <div><span class="cew-stats__n">2021</span><span class="cew-stats__l">Lab founded</span></div>
  </div>
  <div class="cew-stats__note">
    Citations and h-index from
    <a href="https://scholar.google.com/citations?user={{ s.scholar_id }}&amp;hl=en">Google Scholar</a>,
    updated {{ s.updated_display }}.
  </div>
</div>

## Research thrusts

<ul class="cew-cards">
  <li class="cew-card">
    <img src="{{ '/assets/img/cards/energy.jpg' | relative_url }}" alt="Solid-state battery research" loading="lazy">
    <div class="cew-card__body">
      <h3 class="cew-card__title">Solid-state batteries</h3>
      <p class="cew-card__text">
        Dendrite growth through the solid electrolyte, composite-cathode degradation, anode-free
        architectures, and the granular creep that governs how electrolytes densify.
      </p>
      <a class="cew-card__link" href="{{ '/research/' | relative_url }}">Read more →</a>
    </div>
  </li>
  <li class="cew-card">
    <img src="{{ '/assets/img/cards/water.jpg' | relative_url }}" alt="Water purification research" loading="lazy">
    <div class="cew-card__body">
      <h3 class="cew-card__title">Water &amp; critical materials</h3>
      <p class="cew-card__text">
        Capacitive deionization for desalination and heavy-metal removal, lithium recovery from
        brine, and ion transport through membranes under confinement.
      </p>
      <a class="cew-card__link" href="{{ '/research/' | relative_url }}">Read more →</a>
    </div>
  </li>
  <li class="cew-card">
    <img src="{{ '/assets/img/cards/framework.jpg' | relative_url }}" alt="Electro-chemo-mechanics framework" loading="lazy">
    <div class="cew-card__body">
      <h3 class="cew-card__title">Electro-chemo-mechanics</h3>
      <p class="cew-card__text">
        One framework beneath both: DFT, molecular dynamics, phase field, and finite element
        modeling coupled with AI-accelerated multiscale methods.
      </p>
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
