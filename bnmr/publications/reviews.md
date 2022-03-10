---
layout: default
title: Reviews
description: β-NMR review articles.
parent: Publications
grand_parent: β-NMR
---

# Reviews

{% assign reviews = site.data.bnmr.publications.reviews | sort: "published" | reverse %}

To date, {{ reviews.size }} review articles have been published.
They are listed below in reverse chronological order.

<!-- create an empty array -->
{% assign years = "" | split: ',' %}
<!-- push content directly into it -->
{% for review in reviews %}
	{% assign years = years | push: review.year %}
{% endfor %}
<!-- extract the unique values -->
{% assign unique_years = years | uniq %}

{% for year in unique_years %}
<details>
<summary>{{ year }}</summary>
<hr>
{% for pub in reviews %}
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
{% endif %}
{% endfor %}
</details>
{% endfor %}
