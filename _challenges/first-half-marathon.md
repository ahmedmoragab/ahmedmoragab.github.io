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

<table>
  <thead>
    <tr>
      <th>Date</th>
      <th>Run</th>
      <th>Distance</th>
      <th>Moving time</th>
      <th>Avg pace</th>
      <th>Elevation</th>
      <th>Max elevation</th>
      <th>Steps</th>
      <th>Calories</th>
      <th>Avg heart rate</th>
      <th>Longest so far</th>
      <th>Note</th>
    </tr>
  </thead>
  <tbody>
    {% assign longest_so_far = 0 %}
    {% for run in runs %}
    {% assign previous_longest = longest_so_far %}
    {% if run.distance_km > longest_so_far %}
    {% assign longest_so_far = run.distance_km %}
    {% endif %}
    {% assign share = longest_so_far | times: 100.0 | divided_by: page.goal_distance_km | round: 1 %}
    <tr>
      <td>{{ run.date | date: "%b %d, %Y" }} · {{ run.time }}</td>
      <td>{% if run.url %}<a href="{{ run.url | relative_url }}">{{ run.title }}</a>{% else %}{{ run.title }}{% endif %}</td>
      <td>{{ run.distance_km }} km</td>
      <td>{{ run.moving_time }}</td>
      <td>{{ run.average_pace }} /km</td>
      <td>{{ run.elevation_gain_m }} m</td>
      <td>{% if run.max_elevation_m %}{{ run.max_elevation_m }} m{% else %}—{% endif %}</td>
      <td>{% if run.steps %}{{ run.steps }}{% else %}—{% endif %}</td>
      <td>{% if run.calories %}{{ run.calories }} Cal{% else %}—{% endif %}</td>
      <td>{% if run.average_heart_rate_bpm %}{{ run.average_heart_rate_bpm }} bpm{% else %}—{% endif %}</td>
      <td>{{ longest_so_far }} km ({{ share | at_most: 100 }}%)</td>
      <td>{% if run.distance_km > previous_longest %}New longest.{% endif %} {{ run.note }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

The same build continues toward [my first full marathon]({{ '/challenges/first-full-marathon/' | relative_url }}).

[← Back to all challenges]({{ '/challenges/' | relative_url }})
