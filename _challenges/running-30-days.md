---
layout: page
title: "30 Days of Running"
description: "Run at least 5 km every day for 30 days."
challenge_id: running-30-days
target: 30
---

# 30 Days of Running

My goal is to run at least 5 km every day
for 30 consecutive days.

## Why I'm Doing This

I want to build consistency and discipline,
and challenge myself to stay committed to
a long-term goal.

## My Progress

{% assign entries = site.posts | where: "challenge", page.challenge_id %}
{% assign completed = entries | where: "completed", true | size %}
{% assign percent = completed | times: 100.0 | divided_by: page.target | round %}

**{{ completed }} of {{ page.target }} days completed — {{ percent }}%**

<progress value="{{ completed }}" max="{{ page.target }}" style="width:100%;"></progress>

## My Running Journal

{% assign sorted_entries = entries | sort: "date" %}

{% for entry in sorted_entries %}
- [Day {{ entry.day }} — {{ entry.title }}]({{ entry.url | relative_url }}) — {{ entry.distance_km }} km
{% endfor %}
