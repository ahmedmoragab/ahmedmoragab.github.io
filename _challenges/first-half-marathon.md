---
layout: page
title: Run My First Half Marathon
description: Run my first half marathon, covering 21.1 km in a single event.
start_date: 2026-05-16
goal_distance_km: 21.1
completed: true
completed_date: 2026-11-03
completed_distance_km: 21.36
moving_time: "2:30:48"
average_pace: "7:04"
photo: /assets/img/challenges/running/day-51.jpg
permalink: /challenges/first-half-marathon/
nav: false
---

My goal is to run my first half marathon: **21.1 km in a single event**.

{% assign runs = site.data.long_runs | sort: "date" %}
{% assign longest = 0 %}
{% for run in runs %}
{% if run.distance_km > longest %}
{% assign longest = run.distance_km %}
{% endif %}
{% endfor %}
{% assign percent = longest | times: 100.0 | divided_by: page.goal_distance_km | round: 1 %}

{% if page.completed %}
## Status

Completed on {{ page.completed_date | date: "%B %d, %Y" }} — **{{ page.completed_distance_km }} km in {{ page.moving_time }}** at an average pace of **{{ page.average_pace }} min/km**.

This is my first completed half-marathon distance. I am keeping the result separate from a sub-2:30 claim because the full activity time was 2:30:48 and the exact 21.1 km time is not directly recorded.
{% else %}
## Status

In progress — I'll mark this challenge complete after I finish my first half marathon.
{% endif %}

## How the distance was built

The 21.1 km finish was the last step in a longer build, not a one-day jump. From May 16 to November 3, 2026, these long runs in Xiangshan District raised my longest single run from **8.92 km** to **21.36 km**.

<div role="progressbar" aria-label="Half marathon distance built so far" aria-valuenow="{{ percent | at_most: 100 }}" aria-valuemin="0" aria-valuemax="100" aria-valuetext="{{ longest }} km of {{ page.goal_distance_km }} km" style="width: 100%; height: 20px; background: #e2e8f0; border-radius: 10px; overflow: hidden; margin: 1rem 0;">
  <div style="width: {{ percent | at_most: 100 }}%; height: 100%; background: #0969da;"></div>
</div>

**Longest single run:** {{ longest }} km · **{{ percent | at_most: 100 }}%** of the {{ page.goal_distance_km }} km goal.

<p>Each point is one recorded run. Hover or focus a point for its date, distance, pace, and title.</p>
<svg viewBox="0 0 900 390" role="img" aria-labelledby="half-distance-title half-distance-description" style="width: 100%; height: auto;">
  <title id="half-distance-title">Long-run distance by date</title>
  <desc id="half-distance-description">Chronological recorded run distances from {{ runs.first.date | date: "%B %d, %Y" }} through {{ runs.last.date | date: "%B %d, %Y" }}.</desc>
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

The same build continues toward [my first full marathon]({{ '/challenges/first-full-marathon/' | relative_url }}).

[← Back to all challenges]({{ '/challenges/' | relative_url }})
