---
layout: default
title: Electronic Preprints
description: β-NMR electronic preprints.
parent: Publications
grand_parent: β-NMR
---

# Electronic Preprints

{% assign preprints = site.data.bnmr.publications.preprints | sort: "published" | reverse %}

There are currently {{ preprints.size }} electronic preprints awaiting publication.

<hr>

{% for pub in preprints %}
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
    
    {% if pub.abstract %}
        <dt>Abstract</dt>
        <dd>{{ pub.abstract }}</dd>
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
