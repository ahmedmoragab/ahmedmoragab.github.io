---
layout: page
title: 50 Days of Running
description: Running at least 5 km every day for 50 days, building on my first 30 days.
challenge_id: running-50-days
carry_over_from: running-30-days
target: 50
goal_km: 5
permalink: /challenges/50-days-of-running/
nav: false
---

After completing [30 Days of Running]({{ '/challenges/30-days-of-running/' | relative_url }}), I'm extending the challenge to **50 consecutive days of running at least 5 km**.

The first 30 days count toward this goal. Day 31 continues the same running streak, and the journal below brings both parts together.

{% assign current_days = site.posts | where: "challenge", page.challenge_id %}
{% assign previous_days = site.posts | where: "challenge", page.carry_over_from %}
{% assign days = current_days | concat: previous_days | where_exp: "day", "day.day <= page.target" | sort: "day" %}
{% assign completed = days | where: "completed", true | size %}
{% assign percent = completed | times: 100.0 | divided_by: page.target | round %}
{% assign goal_days = 0 %}
{% assign total_distance = 0 %}
{% for day in days %}
{% assign total_distance = total_distance | plus: day.distance_km %}
{% if day.distance_km >= page.goal_km %}
    {% assign goal_days = goal_days | plus: 1 %}
{% endif %}
{% endfor %}

## My Progress

**{{ completed }} of {{ page.target }} days logged — {{ percent }}%**

**Total distance:** {{ total_distance | round: 2 }} km · **{{ page.goal_km }} km goal met:** {{ goal_days }} of {{ days.size }} recorded days.

<progress value="{{ completed }}" max="{{ page.target }}" aria-label="Running days logged" style="width:100%;"></progress>

## Choose a Day

{% for day in days %}
[Day {{ day.day }}]({{ day.url | relative_url }}){% unless forloop.last %} · {% endunless %}
{% endfor %}

## Daily Running Journal

{% for day in days %}

### [Day {{ day.day }} — {{ day.distance_km }} km]({{ day.url | relative_url }})

**Date:** {{ day.date | date: "%B %d, %Y" }}

{% if day.recorded_distance_km %}
**Recording note:** {{ day.distance_km }} km run; {{ day.recorded_distance_km }} km captured by the app.
{% endif %}

{% if day.completed %}
**Status:** Run logged · {% if day.distance_km >= page.goal_km %}{{ page.goal_km }} km goal met{% else %}Below the {{ page.goal_km }} km goal{% endif %}
{% else %}
**Status:** In progress
{% endif %}

{% if day.photo %}
<a href="{{ day.url | relative_url }}"><img src="{{ day.photo | relative_url }}" alt="Day {{ day.day }} running activity summary" loading="lazy" style="max-width:100%;height:auto;"></a>
{% endif %}

{{ day.excerpt | strip_html | truncatewords: 25 }}

[Read day {{ day.day }} →]({{ day.url | relative_url }})

---

{% else %}

Daily entries will appear here as I add them.

{% endfor %}

[← Back to all challenges]({{ '/challenges/' | relative_url }})
