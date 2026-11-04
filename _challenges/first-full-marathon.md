---
layout: page
title: Run My First Full Marathon
description: Run my first full marathon, covering 42.195 km in a single event.
start_date: 2026-05-16
goal_distance_km: 42.195
completed: false
permalink: /challenges/first-full-marathon/
nav: false
---

My goal is to run my first full marathon: **42.195 km in a single event**.

{% assign runs = site.data.long_runs | sort: "date" %}
{% assign longest = 0 %}
{% for run in runs %}
{% if run.distance_km > longest %}
{% assign longest = run.distance_km %}
{% endif %}
{% endfor %}
{% assign percent = longest | times: 100.0 | divided_by: page.goal_distance_km | round: 1 %}

## Status

In progress. The longest single run so far is **{{ longest }} km** on November 3, 2026 — the [first half marathon]({{ '/challenges/first-half-marathon/' | relative_url }}). That is **{{ percent }}%** of 42.195 km. The marathon is still a single event, so this page tracks how far that one-run distance has climbed.

<div role="progressbar" aria-label="Full marathon distance built so far" aria-valuenow="{{ percent | at_most: 100 }}" aria-valuemin="0" aria-valuemax="100" aria-valuetext="{{ longest }} km of {{ page.goal_distance_km }} km" style="width: 100%; height: 20px; background: #e2e8f0; border-radius: 10px; overflow: hidden; margin: 1rem 0;">
  <div style="width: {{ percent | at_most: 100 }}%; height: 100%; background: #0969da;"></div>
</div>

## How the distance was built

These are the same long runs, in chronological order. Each row keeps the distance reached so far, including the runs that did not set a new longest. The half-marathon result is one point on this line, not the whole story.

<p>Each point is one recorded run. Hover or focus a point for its date, distance, pace, and title.</p>
<svg viewBox="0 0 900 390" role="img" aria-labelledby="full-distance-title full-distance-description" style="width: 100%; height: auto;">
  <title id="full-distance-title">Long-run distance by date</title>
  <desc id="full-distance-description">Chronological recorded run distances from {{ runs.first.date | date: "%B %d, %Y" }} through {{ runs.last.date | date: "%B %d, %Y" }}.</desc>
  <line x1="70" y1="35" x2="70" y2="320" stroke="#9aa8b5" />
  <line x1="70" y1="320" x2="860" y2="320" stroke="#9aa8b5" />
  <text x="62" y="325" text-anchor="end" fill="#596b7e" font-size="13">0 km</text>
  <text x="62" y="42" text-anchor="end" fill="#596b7e" font-size="13">{{ page.goal_distance_km }} km</text>
  {% assign point_count = runs.size | minus: 1 %}
  {% capture distance_points %}{% for run in runs %}{% assign x = forloop.index0 | times: 790.0 | divided_by: point_count | plus: 70 %}{% assign y_offset = run.distance_km | times: 285.0 | divided_by: page.goal_distance_km %}{% assign y = 320 | minus: y_offset %}{{ x | round: 1 }},{{ y | round: 1 }}{% unless forloop.last %} {% endunless %}{% endfor %}{% endcapture %}
  <polyline points="{{ distance_points | strip }}" fill="none" stroke="#175b96" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" />
  {% for run in runs %}
  {% assign x = forloop.index0 | times: 790.0 | divided_by: point_count | plus: 70 %}{% assign y_offset = run.distance_km | times: 285.0 | divided_by: page.goal_distance_km %}{% assign y = 320 | minus: y_offset %}
  <circle cx="{{ x | round: 1 }}" cy="{{ y | round: 1 }}" r="6" fill="#175b96" tabindex="0"><title>{{ run.date | date: "%b %d, %Y" }}: {{ run.distance_km }} km · {{ run.average_pace }} /km · {{ run.title }}</title></circle>
  {% endfor %}
  <text x="70" y="350" fill="#596b7e" font-size="13">{{ runs.first.date | date: "%b %d, %Y" }}</text>
  <text x="860" y="350" text-anchor="end" fill="#596b7e" font-size="13">{{ runs.last.date | date: "%b %d, %Y" }}</text>
  <text x="465" y="380" text-anchor="middle" fill="#596b7e" font-size="13">Date</text>
  <text x="16" y="180" text-anchor="middle" fill="#596b7e" font-size="13" transform="rotate(-90 16 180)">Distance (km)</text>
</svg>

[← Back to all challenges]({{ '/challenges/' | relative_url }})
