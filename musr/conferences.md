---
layout: default
title: Conferences
description: International Conferences on Muon Spin Rotation, Relaxation and Resonance (μSR).
parent: μSR
---

# Conferences
{: .no_toc }

Here I compile a list of all past and future
<i>International Conferences on Muon Spin Rotation, Relaxation and Resonance (μSR)</i>,
which are held every few years.

A link to each conference website and published proceedings are included,
if available.

<table>
    <thead>
        <th>Date</th>
        <th>Location</th>
        <th>Website</th>
        <th>Proceedings</th>
    </thead>
    <tbody>
    {% assign conferences = site.data.musr.conferences | sort: "year" | reverse %}
    {% for conf in conferences %}
    <tr>
        <td>{{ conf.date }}</td>
        <td>
            <a href="{{ conf.location | prepend: "https://www.google.com/maps/place/" }}">{{ conf.location }}</a>
        </td>
        <td>
            {% if conf.website %}
                <a href="{{ conf.website }}">{{ conf.website }}</a>
            {% endif %}
        </td>
        <td>
            {% for proc in conf.proceedings %}
                <p>
                <a href="{{ proc.url }}">
                {{ proc.journal }} <b>{{ proc.volume }}</b> {% if proc.issue %}(<i>{{ proc.issue }}</i>){% endif %}
                </a>
                </p>
            {% endfor %}
        </td>
    </tr>
    {% endfor %}
    </tbody>
</table>
