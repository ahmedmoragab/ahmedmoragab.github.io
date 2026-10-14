---
layout: page
title: 30 Days of Running
description: Running at least 5 km every day for 30 days.
challenge_id: running-30-days
target: 30
goal_km: 5
permalink: /challenges/30-days-of-running/
nav: false
---

My goal is to run at least 5 km every day for 30 consecutive days.

## Why I'm Doing This

I want to build consistency and discipline, and challenge myself to stay committed to a long-term goal.

The first 30 days are complete! I'm continuing toward [50 Days of Running]({{ '/challenges/50-days-of-running/' | relative_url }}), with these runs counting toward the new goal.

{% assign days = site.posts | where: "challenge", page.challenge_id | sort: "day" | reverse %}
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

<div role="progressbar" aria-label="{{ page.title | escape }} progress" aria-valuenow="{{ percent | at_most: 100 }}" aria-valuemin="0" aria-valuemax="100" aria-valuetext="{{ completed }} of {{ page.target }} days completed" style="width: 100%; height: 20px; background: #e2e8f0; border-radius: 10px; overflow: hidden;">
  <div style="width: {{ percent | at_most: 100 }}%; height: 100%; background: #0969da;"></div>
</div>

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
