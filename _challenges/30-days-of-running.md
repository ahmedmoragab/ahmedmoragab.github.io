---
layout: page
title: 30 Days of Running
description: Running at least 5 km every day for 30 days.
challenge_id: running30
target: 30
permalink: /challenges/30-days-of-running/
nav: false
---

My goal is to run at least 5 km every day for 30 consecutive days.

## Daily Running Journal

{% assign days = site.posts | where: "challenge", page.challenge_id | sort: "day" %}

{% for day in days %}
### [Day {{ day.day }} — {{ day.distance_km }} km]({{ day.url | relative_url }})

**Date:** {{ day.date | date: "%B %d, %Y" }}

{% if day.completed %}
**Status:** Completed
{% else %}
**Status:** In progress
{% endif %}

{% if day.photo %}
[![Day {{ day.day }}]({{ day.photo | relative_url }})]({{ day.url | relative_url }})
{% endif %}

{{ day.excerpt | strip_html | truncatewords: 25 }}

[Read day {{ day.day }} →]({{ day.url | relative_url }})

---

{% endfor %}
