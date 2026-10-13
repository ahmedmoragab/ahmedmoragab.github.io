---
layout: page
title: 30 Days of Running
description: Running at least 5 km every day for 30 days.
challenge_id: running-30-days
target: 30
permalink: /challenges/30-days-of-running/
nav: false
---

My goal is to run at least 5 km every day for 30 consecutive days.

## Why I'm Doing This

I want to build consistency and discipline, and challenge myself to stay committed to a long-term goal.

{% assign days = site.posts | where: "challenge", page.challenge_id | sort: "day" %}
{% assign completed = days | where: "completed", true | size %}
{% assign percent = completed | times: 100.0 | divided_by: page.target | round %}

## My Progress

**{{ completed }} of {{ page.target }} days completed — {{ percent }}%**

<progress value="{{ completed }}" max="{{ page.target }}" aria-label="Running challenge progress" style="width:100%;"></progress>

## Daily Running Journal

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

{% else %}

Daily entries will appear here as I add them.

{% endfor %}

[← Back to all challenges]({{ '/challenges/' | relative_url }})
