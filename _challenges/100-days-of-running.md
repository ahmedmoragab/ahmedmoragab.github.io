---
layout: page
title: 100 Days of Running
description: Running at least 5 km every day for 100 days, building on my completed 50-day challenge.
challenge_id: running-100-days
start_date: 2026-11-02
consistency_start_date: 2026-09-13
consistency_end_date: 2026-11-03
carry_over_from: running-50-days
additional_carry_over_from: running-30-days
target: 100
goal_km: 5
completed: false
permalink: /challenges/100-days-of-running/
nav: false
---

{% assign current_days = site.posts | where: "challenge", page.challenge_id %}
{% assign carried_days = site.posts | where: "challenge", page.carry_over_from %}
{% assign additional_carried_days = site.posts | where: "challenge", page.additional_carry_over_from %}
{% assign days = current_days | concat: carried_days | concat: additional_carried_days | where_exp: "day", "day.day <= page.target" | sort: "day" | reverse %}
{% assign completed = days | where: "completed", true | size %}
{% assign achievement = completed | times: 100.0 | divided_by: page.target | round: 2 %}
{% assign first_run = page.consistency_start_date | default: page.start_date %}
{% assign latest_run = page.consistency_end_date | default: days.first.date %}
{% assign first_seconds = first_run | date: "%s" %}
{% assign latest_seconds = latest_run | date: "%s" %}
{% assign elapsed_seconds = latest_seconds | minus: first_seconds %}
{% assign elapsed_days = elapsed_seconds | divided_by: 86400 | plus: 1 %}
{% assign consistency = completed | times: 100.0 | divided_by: elapsed_days | round: 2 %}
{% assign goal_days = 0 %}
{% assign total_distance = 0 %}
{% for day in days %}
{% if day.completed %}
{% assign total_distance = total_distance | plus: day.distance_km %}
{% if day.distance_km >= page.goal_km %}
{% assign goal_days = goal_days | plus: 1 %}
{% endif %}
{% endif %}
{% endfor %}

## Progress So Far

**Achievement:** {{ completed }} of {{ page.target }} planned runs ({{ achievement }}%)

**Consistency:** {{ completed }} of {{ elapsed_days }} elapsed days ({{ consistency }}%)

**Total distance:** {{ total_distance | round: 2 }} km · **{{ page.goal_km }} km goal met:** {{ goal_days }} of {{ completed }} completed runs.

Achievement measures progress toward the target; consistency measures how regularly I showed up over time. The 50 completed runs from my previous challenge count toward this one.

**Status:** In progress · **Day 51:** Recovery day on November 2, followed by Run 51 on November 3.

<div role="progressbar" aria-label="{{ page.title | escape }} achievement" aria-valuenow="{{ achievement | at_most: 100 }}" aria-valuemin="0" aria-valuemax="100" aria-valuetext="{{ completed }} of {{ page.target }} planned runs completed" style="width: 100%; height: 20px; background: #e2e8f0; border-radius: 10px; overflow: hidden;">
  <div style="width: {{ achievement | at_most: 100 }}%; height: 100%; background: #0969da;"></div>
</div>

## The New Goal

The first 50 runs are already part of this journey. I am extending the challenge to **100 days of running at least 5 km**, while allowing recovery days when my body needs them. One missed day changes the consistency score, but it does not erase the work already completed.

## Choose a Day

{% for day in days %}
[Day {{ day.day }}]({{ day.url | relative_url }}){% unless forloop.last %} · {% endunless %}
{% endfor %}

## Daily Running Journal

{% for day in days %}

### [Day {{ day.day }} — {{ day.distance_km }} km]({{ day.url | relative_url }})

**Date:** {{ day.date | date: "%B %d, %Y" }}

{% if day.completed %}
**Status:** Run logged · {% if day.distance_km >= page.goal_km %}{{ page.goal_km }} km goal met{% else %}Below the {{ page.goal_km }} km goal{% endif %}
{% endif %}

{% if day.photo %}
<a href="{{ day.url | relative_url }}"><img src="{{ day.photo | relative_url }}" alt="Day {{ day.day }} running activity summary" loading="lazy" style="max-width:100%;height:auto;"></a>
{% endif %}

{{ day.excerpt | strip_html | truncatewords: 25 }}

[Read day {{ day.day }} →]({{ day.url | relative_url }})

---

{% endfor %}

[← Back to all challenges]({{ '/challenges/' | relative_url }})
