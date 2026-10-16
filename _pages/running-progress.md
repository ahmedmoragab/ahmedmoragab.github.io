---
layout: page
title: Running Progress
description: A live summary of my runs across the 30-day and 50-day running challenges.
permalink: /challenges/running-progress/
nav: false
---

{% assign first_challenge_runs = site.posts | where: "challenge", "running-30-days" %}
{% assign second_challenge_runs = site.posts | where: "challenge", "running-50-days" %}
{% assign runs = first_challenge_runs | concat: second_challenge_runs | where: "completed", true | sort: "day" %}
{% assign pace_runs = runs | where_exp: "run", "run.recorded_distance_km == nil" | where_exp: "run", "run.moving_time != nil" | where_exp: "run", "run.distance_km > 0" %}
{% assign total_distance = 0 %}
{% assign goal_days = 0 %}
{% for run in runs %}
{% assign total_distance = total_distance | plus: run.distance_km %}
{% if run.distance_km >= 5 %}
{% assign goal_days = goal_days | plus: 1 %}
{% endif %}
{% endfor %}

## Progress So Far

Since **{{ runs.first.date | date: "%B %d, %Y" }}**, I've logged **{{ runs.size }} runs** covering **{{ total_distance | round: 2 }} km**. I met my 5 km daily goal on **{{ goal_days }} of {{ runs.size }} runs**.

{% assign fastest_pace = 999999 %}
{% assign slowest_pace = 0 %}
{% for run in pace_runs %}
{% assign time_parts = run.moving_time | split: ":" %}
{% if time_parts.size == 3 %}
{% assign hours = time_parts[0] | plus: 0 %}
{% assign minutes = time_parts[1] | plus: 0 %}
{% assign seconds = time_parts[2] | plus: 0 %}
{% assign duration = hours | times: 3600 | plus: minutes | times: 60 | plus: seconds %}
{% else %}
{% assign minutes = time_parts[0] | plus: 0 %}
{% assign seconds = time_parts[1] | plus: 0 %}
{% assign duration = minutes | times: 60 | plus: seconds %}
{% endif %}
{% assign run_pace = duration | divided_by: run.distance_km | round %}
{% if run_pace < fastest_pace %}
{% assign fastest_pace = run_pace %}
{% endif %}
{% if run_pace > slowest_pace %}
{% assign slowest_pace = run_pace %}
{% endif %}
{% endfor %}
{% assign pace_range = slowest_pace | minus: fastest_pace %}
{% assign last_day = runs.last.day | minus: 1 %}
{% if last_day < 1 %}
{% assign last_day = 1 %}
{% endif %}
{% assign fastest_minutes = fastest_pace | divided_by: 60 %}
{% assign fastest_seconds = fastest_pace | modulo: 60 | prepend: "0" | slice: -2, 2 %}
{% assign slowest_minutes = slowest_pace | divided_by: 60 %}
{% assign slowest_seconds = slowest_pace | modulo: 60 | prepend: "0" | slice: -2, 2 %}

{% assign comparison_window = pace_runs.size | divided_by: 2 | at_most: 7 %}
{% if comparison_window > 0 %}
{% assign first_window = pace_runs | slice: 0, comparison_window %}
{% assign latest_window = pace_runs | reverse | slice: 0, comparison_window %}
{% assign first_time = 0 %}
{% assign first_distance = 0 %}
{% for run in first_window %}
{% assign time_parts = run.moving_time | split: ":" %}
{% if time_parts.size == 3 %}
{% assign hours = time_parts[0] | plus: 0 %}
{% assign minutes = time_parts[1] | plus: 0 %}
{% assign seconds = time_parts[2] | plus: 0 %}
{% assign duration = hours | times: 3600 | plus: minutes | times: 60 | plus: seconds %}
{% else %}
{% assign minutes = time_parts[0] | plus: 0 %}
{% assign seconds = time_parts[1] | plus: 0 %}
{% assign duration = minutes | times: 60 | plus: seconds %}
{% endif %}
{% assign first_time = first_time | plus: duration %}
{% assign first_distance = first_distance | plus: run.distance_km %}
{% endfor %}
{% assign latest_time = 0 %}
{% assign latest_distance = 0 %}
{% for run in latest_window %}
{% assign time_parts = run.moving_time | split: ":" %}
{% if time_parts.size == 3 %}
{% assign hours = time_parts[0] | plus: 0 %}
{% assign minutes = time_parts[1] | plus: 0 %}
{% assign seconds = time_parts[2] | plus: 0 %}
{% assign duration = hours | times: 3600 | plus: minutes | times: 60 | plus: seconds %}
{% else %}
{% assign minutes = time_parts[0] | plus: 0 %}
{% assign seconds = time_parts[1] | plus: 0 %}
{% assign duration = minutes | times: 60 | plus: seconds %}
{% endif %}
{% assign latest_time = latest_time | plus: duration %}
{% assign latest_distance = latest_distance | plus: run.distance_km %}
{% endfor %}
{% assign first_pace = first_time | divided_by: first_distance | round %}
{% assign latest_pace = latest_time | divided_by: latest_distance | round %}
{% assign first_pace_minutes = first_pace | divided_by: 60 %}
{% assign first_pace_seconds = first_pace | modulo: 60 | prepend: "0" | slice: -2, 2 %}
{% assign latest_pace_minutes = latest_pace | divided_by: 60 %}
{% assign latest_pace_seconds = latest_pace | modulo: 60 | prepend: "0" | slice: -2, 2 %}
{% assign pace_difference = first_pace | minus: latest_pace %}
{% assign pace_difference_abs = pace_difference | abs %}
{% assign pace_change_percent = pace_difference_abs | times: 100.0 | divided_by: first_pace | round: 1 %}

Across my first and latest **{{ comparison_window }} comparable runs**, average pace changed from **{{ first_pace_minutes }}:{{ first_pace_seconds }} to {{ latest_pace_minutes }}:{{ latest_pace_seconds }} min/km**. That's a **{{ pace_change_percent }}% {% if pace_difference > 0 %}faster{% elsif pace_difference < 0 %}slower{% else %}unchanged{% endif %}** average pace in the latest group. This is a comparison of recorded workouts, not a controlled fitness test; distance, effort, terrain, traffic, and weather can vary.

{% else %}

Pace comparisons will appear after at least two complete runs with recorded moving times.

{% endif %}

## Pace by Run

Lower pace means faster. The chart includes complete recordings with a moving time; partially recorded activities are left out of the pace analysis.

<svg viewBox="0 0 900 390" role="img" aria-labelledby="pace-chart-title pace-chart-description" style="width: 100%; height: auto;">
  <title id="pace-chart-title">Average pace across {{ pace_runs.size }} complete runs</title>
  <desc id="pace-chart-description">Pace ranges from {{ fastest_minutes }} minutes {{ fastest_seconds }} seconds per kilometer at the top to {{ slowest_minutes }} minutes {{ slowest_seconds }} seconds per kilometer at the bottom. Lower is faster.</desc>
  <line x1="58" y1="45" x2="58" y2="320" stroke="#9aa8b5" />
  <line x1="58" y1="320" x2="860" y2="320" stroke="#9aa8b5" />
  <line x1="58" y1="45" x2="860" y2="45" stroke="#e2e8f0" />
  <line x1="58" y1="320" x2="860" y2="320" stroke="#e2e8f0" />
  <text x="50" y="32" text-anchor="end" fill="#596b7e" font-size="13">{{ fastest_minutes }}:{{ fastest_seconds }}</text>
  <text x="50" y="325" text-anchor="end" fill="#596b7e" font-size="13">{{ slowest_minutes }}:{{ slowest_seconds }}</text>
  <text x="58" y="355" fill="#596b7e" font-size="13">Day 1</text>
  <text x="860" y="355" text-anchor="end" fill="#596b7e" font-size="13">Day {{ runs.last.day }}</text>
  {% capture chart_points %}
  {% for run in pace_runs %}
  {% assign time_parts = run.moving_time | split: ":" %}
  {% if time_parts.size == 3 %}
  {% assign hours = time_parts[0] | plus: 0 %}
  {% assign minutes = time_parts[1] | plus: 0 %}
  {% assign seconds = time_parts[2] | plus: 0 %}
  {% assign duration = hours | times: 3600 | plus: minutes | times: 60 | plus: seconds %}
  {% else %}
  {% assign minutes = time_parts[0] | plus: 0 %}
  {% assign seconds = time_parts[1] | plus: 0 %}
  {% assign duration = minutes | times: 60 | plus: seconds %}
  {% endif %}
  {% assign run_pace = duration | divided_by: run.distance_km | round %}
  {% assign day_offset = run.day | minus: 1 %}
  {% assign x = day_offset | times: 802.0 | divided_by: last_day | plus: 58 %}
  {% if pace_range > 0 %}
  {% assign y_offset = run_pace | minus: fastest_pace | times: 275.0 | divided_by: pace_range %}
  {% else %}
  {% assign y_offset = 0 %}
  {% endif %}
  {% assign y = y_offset | plus: 45 %}
  {{ x | round: 1 }},{{ y | round: 1 }}{% unless forloop.last %} {% endunless %}
  {% endfor %}
  {% endcapture %}
  <polyline points="{{ chart_points | strip }}" fill="none" stroke="#175b96" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" />
  {% for run in pace_runs %}
  {% assign time_parts = run.moving_time | split: ":" %}
  {% if time_parts.size == 3 %}
  {% assign hours = time_parts[0] | plus: 0 %}
  {% assign minutes = time_parts[1] | plus: 0 %}
  {% assign seconds = time_parts[2] | plus: 0 %}
  {% assign duration = hours | times: 3600 | plus: minutes | times: 60 | plus: seconds %}
  {% else %}
  {% assign minutes = time_parts[0] | plus: 0 %}
  {% assign seconds = time_parts[1] | plus: 0 %}
  {% assign duration = minutes | times: 60 | plus: seconds %}
  {% endif %}
  {% assign run_pace = duration | divided_by: run.distance_km | round %}
  {% assign day_offset = run.day | minus: 1 %}
  {% assign x = day_offset | times: 802.0 | divided_by: last_day | plus: 58 %}
  {% if pace_range > 0 %}
  {% assign y_offset = run_pace | minus: fastest_pace | times: 275.0 | divided_by: pace_range %}
  {% else %}
  {% assign y_offset = 0 %}
  {% endif %}
  {% assign y = y_offset | plus: 45 %}
  <circle cx="{{ x | round: 1 }}" cy="{{ y | round: 1 }}" r="4" fill="#175b96">
    <title>Day {{ run.day }}: {{ run.average_pace }} min/km</title>
  </circle>
  {% endfor %}
</svg>

## Run Log

The table below is built directly from the run posts, so new completed runs appear here automatically when the site rebuilds.

<div style="overflow-x: auto;" tabindex="0" role="region" aria-label="Running data for all completed challenge runs">
  <table>
    <thead>
      <tr><th scope="col">Run</th><th scope="col">Date</th><th scope="col">Distance</th><th scope="col">Moving time</th><th scope="col">Average pace</th></tr>
    </thead>
    <tbody>
      {% for run in runs %}
      <tr>
        <th scope="row"><a href="{{ run.url | relative_url }}">Day {{ run.day }}</a></th>
        <td>{{ run.date | date: "%b %d, %Y" }}</td>
        <td>{{ run.distance_km }} km{% if run.recorded_distance_km %} ({{ run.recorded_distance_km }} km recorded){% endif %}</td>
        <td>{{ run.moving_time | default: "—" }}</td>
        <td>{{ run.average_pace | default: "—" }}{% if run.average_pace %} min/km{% endif %}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

[← Back to 50 Days of Running]({{ '/challenges/50-days-of-running/' | relative_url }}) · [All challenges]({{ '/challenges/' | relative_url }})
