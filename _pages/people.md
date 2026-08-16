---
layout: page
permalink: /people/
title: people
description: The CEW Lab team — faculty, postdocs, and students.
nav: true
nav_order: 2
redirect_from:
  - /team
---

{% assign ph = '/assets/img/team/_placeholder.jpg' %}

{% for group in site.data.team.groups %}
{% if group.members.size > 0 %}
<h2 class="team-heading" id="{{ group.id }}">{{ group.name }}</h2>
<ul class="team-grid">
  {% for m in group.members %}
  <li class="team-card">
    {% if m.photo %}
      {% assign src = m.photo | prepend: '/assets/img/team/' %}
    {% else %}
      {% assign src = ph %}
    {% endif %}
    <img src="{{ src | relative_url }}" alt="{{ m.name }}" loading="lazy" width="220" height="220">
    <div class="team-name">{{ m.name }}</div>
    {% if m.role %}<div class="team-role">{{ m.role }}</div>{% endif %}
    {% if m.topic %}<div class="team-topic">{{ m.topic }}</div>{% endif %}
    {% if m.email or m.links %}
    <div class="team-links">
      {% if m.email %}<a href="mailto:{{ m.email }}" title="Email">email</a>{% endif %}
      {% if m.links.scholar %}<a href="{{ m.links.scholar }}" title="Google Scholar">scholar</a>{% endif %}
      {% if m.links.researchgate %}<a href="{{ m.links.researchgate }}" title="ResearchGate">RG</a>{% endif %}
      {% if m.links.linkedin %}<a href="{{ m.links.linkedin }}" title="LinkedIn">linkedin</a>{% endif %}
    </div>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% endif %}
{% endfor %}

{% if site.data.team.alumni.size > 0 %}
<h2 class="team-heading" id="alumni">Alumni &amp; Former Visitors</h2>
<p class="team-alumni">
  {% for a in site.data.team.alumni %}<span>{{ a.name }}</span>{% unless forloop.last %} · {% endunless %}{% endfor %}
</p>
{% endif %}
