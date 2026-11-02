---
layout: page
title: Challenges
permalink: /challenges/
nav: true
nav_order: 5
---

Here I share the challenges I'm taking on to build new skills, stay consistent, and grow as a person and a leader—one day at a time.

{% assign challenges = site.challenges | sort: "start_date" | reverse %}
{% for challenge in challenges %}

{% if challenge.goal_distance_km %}

## [{{ challenge.title }}]({{ challenge.url | relative_url }})

**Goal:** Run your first race of {{ challenge.goal_distance_km }} km · **Status:** {% if challenge.completed %}Completed{% else %}In progress{% endif %}

{% else %}

{% assign entries = site.posts | where: "challenge", challenge.challenge_id %}
{% if challenge.carry_over_from %}
{% assign previous_entries = site.posts | where: "challenge", challenge.carry_over_from %}
{% assign entries = entries | concat: previous_entries %}
{% endif %}
{% assign entries = entries | where_exp: "entry", "entry.day <= challenge.target" %}
{% assign entries = entries | sort: "date" | reverse %}
{% assign completed = entries | where: "completed", true | size %}
{% assign percent = completed | times: 100.0 | divided_by: challenge.target | round %}
{% assign first_entry = challenge.consistency_start_date | default: challenge.start_date %}
{% assign latest_entry = entries.first.date %}
{% assign first_seconds = first_entry | date: "%s" %}
{% assign latest_seconds = latest_entry | date: "%s" %}
{% assign elapsed_seconds = latest_seconds | minus: first_seconds %}
{% assign elapsed_days = elapsed_seconds | divided_by: 86400 | plus: 1 %}
{% assign consistency = completed | times: 100.0 | divided_by: elapsed_days | round: 2 %}

## [{{ challenge.title }}]({{ challenge.url | relative_url }})

**Achievement:** {{ percent }}% · {{ completed }} / {{ challenge.target }} planned runs · **Consistency:** {{ consistency }}% · {{ completed }} / {{ elapsed_days }} elapsed days · **Status:** {% if challenge.completed %}Done!{% else %}In progress{% endif %}

Achievement tracks progress toward the target; consistency tracks how regularly the work happened over time.

<div role="progressbar" aria-label="{{ challenge.title | escape }} progress" aria-valuenow="{{ percent | at_most: 100 }}" aria-valuemin="0" aria-valuemax="100" aria-valuetext="{{ completed }} of {{ challenge.target }} days completed" style="width: 100%; height: 20px; background: #e2e8f0; border-radius: 10px; overflow: hidden;">
  <div style="width: {{ percent | at_most: 100 }}%; height: 100%; background: #0969da;"></div>
</div>

{% endif %}

{% else %}

No challenges have been added yet.

{% endfor %}
