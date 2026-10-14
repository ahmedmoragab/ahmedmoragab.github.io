---
layout: page
title: Challenges
description: My personal challenges and progress.
permalink: /challenges/
nav: true
nav_order: 5
---

A living record of the goals I set, the things
I learn, and my personal growth.

{% for challenge in site.challenges %}

{% assign entries = site.posts | where: "challenge", challenge.challenge_id %}
{% if challenge.carry_over_from %}
{% assign previous_entries = site.posts | where: "challenge", challenge.carry_over_from %}
{% assign entries = entries | concat: previous_entries %}
{% endif %}
{% assign entries = entries | where_exp: "entry", "entry.day <= challenge.target" %}
{% assign completed = entries | where: "completed", true | size %}
{% assign percent = completed | times: 100.0 | divided_by: challenge.target | round %}

## [{{ challenge.title }}]({{ challenge.url | relative_url }})

{{ challenge.description }}

**Days logged: {{ completed }} / {{ challenge.target }} ({{ percent }}%)**

<div role="progressbar" aria-label="{{ challenge.title | escape }} progress" aria-valuenow="{{ percent | at_most: 100 }}" aria-valuemin="0" aria-valuemax="100" aria-valuetext="{{ completed }} of {{ challenge.target }} days completed" style="width: 100%; height: 20px; background: #e2e8f0; border-radius: 10px; overflow: hidden;">
  <div style="width: {{ percent | at_most: 100 }}%; height: 100%; background: #0969da;"></div>
</div>

[View challenge and daily entries →]({{ challenge.url | relative_url }})

{% else %}

No challenges have been added yet.

{% endfor %}
