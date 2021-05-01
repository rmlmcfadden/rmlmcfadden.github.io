---
layout: default
title: Theses
description: μSR theses.
parent: μSR
---

# Theses

{% assign theses = site.data.musr.publications.theses | sort: "published" | reverse %}

Here I compile a (short) list of theses based around the μSR technique.
Nowadays, the use μSR is widespread enough that a comprehensive compilation is
impractical.
Instead, this list mainly reflects works that I've read (or at least skimmed).

So far, this collection contains {{ theses.size }} theses.

<hr>

{% for pub in theses %}
<dl>
    {% if pub.title %}
        <dt>Title</dt>
        <dd>{{ pub.title }}</dd>
    {% endif %}

    {% if pub.author %}
        <dt>Author</dt>
        <dd>
        {% for author in pub.author  %}
            {% if author != pub.author.last %}
                {{ author | append: ", " }}
            {% else %}
                {{ author }}
            {% endif %}
        {% endfor %}
        </dd>
    {% endif %}
    
    {% if pub.degree %}
        <dt>Degree</dt>
        <dd>{{ pub.degree }}</dd>
    {% endif %}
    
    {% if pub.school %}
        <dt>School</dt>
        <dd>{{ pub.school }}</dd>
    {% endif %}
    
    {% if pub.address %}
        <dt>Address</dt>
        <dd>{{ pub.address }}</dd>
    {% endif %}
    
    {% if pub.year %}
        <dt>Year</dt>
        <dd>{{ pub.year }}</dd>
    {% endif %}
    
    {% if pub.abstract %}
        <dt>Abstract</dt>
        <dd>
            <details>
                <summary></summary>
                {{ pub.abstract }}
            </details>
        </dd>
    {% endif %}
    
    {% if pub.doi %}
        <dt><i class="ai ai-doi"></i></dt>
        <dd><a href="https://doi.org/{{ pub.doi }}">{{ pub.doi }}</a></dd>
    {% endif %}
    
    {% if pub.arxiv %}
        <dt><i class="ai ai-arxiv"></i></dt>
        <dd>
        <a href="https://arxiv.org/abs/{{ pub.arxiv.id }}">arXiv:{{ pub.arxiv.id }} [{{ pub.arxiv.cat }}]</a>
        </dd>
    {% endif %}
    
    {% if pub.url %}
        <dt><i class="fas fa-external-link-alt"></i></dt>
        <dd><a href="{{ pub.url }}">{{ pub.url }}</a></dd>
    {% endif %}
</dl>
<hr>
{% endfor %}
