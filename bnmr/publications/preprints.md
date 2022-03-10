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
They are listed below in reverse chronological order.

<!-- create an empty array -->
{% assign years = "" | split: ',' %}
<!-- push content directly into it -->
{% for preprint in preprints %}
	{% assign years = years | push: preprint.year %}
{% endfor %}
<!-- extract the unique values -->
{% assign unique_years = years | uniq %}

{% for year in unique_years %}
<details>
<summary>{{ year }}</summary>
<hr>
{% for pub in preprints %}
{% if year == pub.year %}
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
{% endif %}
{% endfor %}
</details>
{% endfor %}
