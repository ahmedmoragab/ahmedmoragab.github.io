
---
layout: page
title: "Run 5 km Every Day for 30 Days"
description: "A personal challenge to build consistency."
challenge_id: running-30-days
target: 30
---

# My 30-Day Running Challenge

**Goal:** Run 5 km every day for 30 days.

## Why I'm Doing This

I want to develop consistency, improve
my physical fitness, and learn to stay
committed to a long-term goal.

## My Progress

{% assign entries = site.posts | where: "challenge", page.challenge_id %}
{% assign completed = entries | where: "completed", true | size %}
{% assign percent = completed | times: 100 | divided_by: page.target %}

**Completed: {{ completed }} / {{ page.target }} days**

**Progress: {{ percent }}%**

<progress value="{{ completed }}" max="{{ page.target }}" style="width:100%;"></progress>

## Daily Journal

{% assign sorted_entries = entries | sort: "date" %}

{% for entry in sorted_entries %}

- [{{ entry.title }}]({{ entry.url | relative_url }})
  {% if entry.completed %}✓ Completed{% else %}Not completed{% endif %}

{% endfor %}
