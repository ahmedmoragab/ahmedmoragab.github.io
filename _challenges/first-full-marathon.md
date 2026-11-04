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
      <td>{{ longest_so_far }} km ({{ share }}%)</td>
      <td>{% if run.distance_km > previous_longest %}New longest.{% endif %} {{ run.note }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

[← Back to all challenges]({{ '/challenges/' | relative_url }})
