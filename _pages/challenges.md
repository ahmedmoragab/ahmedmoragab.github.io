---
layout: page
title: Challenges
description: My personal challenges and progress.
permalink: /challenges/
nav: false
nav_order: 5
---

# My Challenges

A living record of the goals I set, the things
I learn, and my personal growth.

{% for challenge in site.challenges %}

{% assign entries = site.posts | where: "challenge", challenge.challenge_id %}
{% assign completed = entries | where: "completed", true | size %}
{% assign percent = completed | times: 100.0 | divided_by: challenge.target | round %}

## [{{ challenge.title }}]({{ challenge.url | relative_url }})

{{ challenge.description }}

**Progress: {{ completed }} / {{ challenge.target }} ({{ percent }}%)**

<progress value="{{ completed }}" max="{{ challenge.target }}" style="width:100%;"></progress>

{% else %}

No challenges have been added yet.

{% endfor %}
