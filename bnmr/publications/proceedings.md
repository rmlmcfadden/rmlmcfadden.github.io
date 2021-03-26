---
layout: default
title: Conference Proceedings
description: β-NMR conference proceedings.
parent: Publications
grand_parent: β-NMR
---

# Conference Proceedings

{% assign proceedings = site.data.bnmr.publications.proceedings | sort: "published" | reverse %}

To date, {{ proceedings.size }} articles have been published in conference proceedings.

<hr>

{% for pub in proceedings %}
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
    
    {% if pub.journal %}
        <dt>Journal</dt>
        <dd>{{ pub.journal }}</dd>
    {% endif %}
    
    {% if pub.volume %}
        <dt>Volume</dt>
        <dd>{{ pub.volume }}</dd>
    {% endif %}
    
    {% if pub.issue %}
        <dt>Issue</dt>
        <dd>{{ pub.issue }}</dd>
    {% endif %}
    
    {% if pub.pages %}
        <dt>Pages</dt>
        <dd>{{ pub.pages }}</dd>
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
