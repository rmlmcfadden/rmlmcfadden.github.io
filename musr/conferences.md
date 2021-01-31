---
layout: default
title: Conferences
description: International Conferences on Muon Spin Rotation, Relaxation and Resonance (μSR).
parent: μSR
---

# Conferences
{: .no_toc }

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

{% assign conferences = site.data.musr.conferences | sort: "year" | reverse %}

{% for conference in conferences %}
    <h2>{{ conference.year | prepend: "μSR" }}</h2>
    
    <dl>
    
    <dt>Location</dt>
    <dd>{{ conference.location }}</dd>
    
    <dt>Website</dt>
    <dd>
    {% if conference.website %}
        <a href="{{ conference.website }}">{{ conference.website }}</a>
    {% endif %}
    </dd>
    
    <dt>Proceedings</dt>
    <dd>
    {% for p in conference.proceedings %}
        <p>
        <a href="{{ p.url }}">
        {{ p.journal }} <b>{{ p.volume }}</b> (<i>{{ p.issue }}</i>)
        </a>
        </p>
    {% endfor %}
    </dd>
    
    </dl>
{% endfor %}
