---
layout: page
title: Run My First Half Marathon
description: Run my first half marathon, covering 21.1 km in a single event.
start_date: 2026-10-16
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

{% if page.completed %}
## Status

Completed on {{ page.completed_date | date: "%B %d, %Y" }} — **{{ page.completed_distance_km }} km in {{ page.moving_time }}** at an average pace of **{{ page.average_pace }} min/km**.

This is my first completed half-marathon distance. I am keeping the result separate from a sub-2:30 claim because the full activity time was 2:30:48 and the exact 21.1 km time is not directly recorded.
{% else %}
## Status

In progress — I'll mark this challenge complete after I finish my first half marathon.
{% endif %}

[← Back to all challenges]({{ '/challenges/' | relative_url }})
