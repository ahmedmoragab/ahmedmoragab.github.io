---
layout: page
title: Topics
permalink: /blog/topics/
nav: false
---

{% assign entries = site.posts | concat: site.news | where_exp: "entry", "entry.published != false" | sort: "date" | reverse %}
{% assign tags = entries | map: "tags" | join: "," | split: "," %}
{% assign categories = entries | map: "categories" | join: "," | split: "," %}
{% assign news_topics = entries | map: "topics" | join: "," | split: "," %}
{% assign topics = tags | concat: categories | concat: news_topics | uniq | sort %}

{% for topic in topics %}
{% unless topic == empty %}
<h2 id="{{ topic | slugify }}">{{ topic | replace: '-', ' ' | capitalize | replace: "Phd", "PhD" | escape }}</h2>
<ul>
{% for entry in entries %}
{% if entry.tags contains topic or entry.categories contains topic or entry.topics contains topic %}
  <li><a href="{{ entry.url | relative_url }}">{{ entry.title | escape }}</a> — {{ entry.date | date: "%b %d, %Y" }}</li>
{% endif %}
{% endfor %}
</ul>
{% endunless %}
{% endfor %}
