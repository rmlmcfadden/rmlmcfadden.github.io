---
layout: default
title: Publications
description: β-NMR publications.
permalink: /triumf/bnmr/publications
parent: β-NMR
grand_parent: TRIUMF
---

# Publications
{: .no_toc }

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Electronic Preprints

{% assign preprints = site.data.bnmr.publications.preprints | sort: "published" | reverse %}

<ol reversed>
{% for pub in preprints %}
   <li>
   {% if pub.author %}
      <p>
      {% for author in pub.author  %}
         {% if pub.author.size > 2 and author != pub.author.last %}
            {{ author | append: ", " }}
         {% elsif pub.author.size > 1 and author == pub.author.last %}
            {{ author | prepend: "and " | append: "." }}
         {% else %}
            {{ author | append: "." }}
         {% endif %}
      {% endfor %}
      </p>
   {% endif %}
   {% if pub.title %}
      <p>
      <i>{{ pub.title }}.</i>
      </p>
   {% endif %}
   {% if pub.journal and pub.volume and pub.pages and pub.year %}
      <p>
      {{ pub.journal }} <b>{{ pub.volume }}</b>, {{ pub.pages }} ({{ pub.year }}).
      </p>
   {% endif %}
   {% if pub.abstract %}
      <details>
         <summary>Abstract</summary>
         <p>{{ pub.abstract }}</p>
      </details>
   {% endif %}
   {% if pub.doi or pub.arxiv or pub.url %}
      <p>
      {% if pub.doi %}
         <i class="ai ai-doi"></i>
         <a href="https://doi.org/{{ pub.doi }}">{{ pub.doi }}</a>
      {% endif %}
      {% if pub.arxiv %}
         <i class="ai ai-arxiv"></i>
         <a href="https://arxiv.org/abs/{{ pub.arxiv.id }}">arXiv:{{ pub.arxiv.id }} [{{ pub.arxiv.cat }}]</a>
      {% endif %}
      {% if pub.url %}
         <i class="fa fa-link"></i>
         <a href="{{ pub.url }}">{{ pub.url }}</a>
      {% endif %}
      </p>
   {% endif %}
   </li>
{% endfor %}
</ol>

## Journal Articles

{% assign articles = site.data.bnmr.publications.articles | sort: "published" | reverse %}

<ol reversed>
{% for pub in articles %}
   <li>
   {% if pub.author %}
      <p>
      {% for author in pub.author  %}
         {% if pub.author.size > 2 and author != pub.author.last %}
            {{ author | append: ", " }}
         {% elsif pub.author.size > 1 and author == pub.author.last %}
            {{ author | prepend: "and " | append: "." }}
         {% else %}
            {{ author | append: "." }}
         {% endif %}
      {% endfor %}
      </p>
   {% endif %}
   {% if pub.title %}
      <p>
      <i>{{ pub.title }}.</i>
      </p>
   {% endif %}
   {% if pub.journal and pub.volume and pub.pages and pub.year %}
      <p>
      {{ pub.journal }} <b>{{ pub.volume }}</b>, {{ pub.pages }} ({{ pub.year }}).
      </p>
   {% endif %}
   {% if pub.abstract %}
      <details>
         <summary>Abstract</summary>
         <p>{{ pub.abstract }}</p>
      </details>
   {% endif %}
   {% if pub.doi or pub.arxiv or pub.url %}
      <p>
      {% if pub.doi %}
         <i class="ai ai-doi"></i>
         <a href="https://doi.org/{{ pub.doi }}">{{ pub.doi }}</a>
      {% endif %}
      {% if pub.arxiv %}
         <i class="ai ai-arxiv"></i>
         <a href="https://arxiv.org/abs/{{ pub.arxiv.id }}">arXiv:{{ pub.arxiv.id }} [{{ pub.arxiv.cat }}]</a>
      {% endif %}
      {% if pub.url %}
         <i class="fa fa-link"></i>
         <a href="{{ pub.url }}">{{ pub.url }}</a>
      {% endif %}
      </p>
   {% endif %}
   </li>
{% endfor %}
</ol>

## Conference Proceedings

{% assign proceedings = site.data.bnmr.publications.proceedings | sort: "published" | reverse %}

<ol reversed>
{% for pub in proceedings %}
   <li>
   {% if pub.author %}
      <p>
      {% for author in pub.author  %}
         {% if pub.author.size > 2 and author != pub.author.last %}
            {{ author | append: ", " }}
         {% elsif pub.author.size > 1 and author == pub.author.last %}
            {{ author | prepend: "and " | append: "." }}
         {% else %}
            {{ author | append: "." }}
         {% endif %}
      {% endfor %}
      </p>
   {% endif %}
   {% if pub.title %}
      <p>
      <i>{{ pub.title }}.</i>
      </p>
   {% endif %}
   {% if pub.journal and pub.volume and pub.pages and pub.year %}
      <p>
      {{ pub.journal }} <b>{{ pub.volume }}</b>, {{ pub.pages }} ({{ pub.year }}).
      </p>
   {% endif %}
   {% if pub.abstract %}
      <details>
         <summary>Abstract</summary>
         <p>{{ pub.abstract }}</p>
      </details>
   {% endif %}
   {% if pub.doi or pub.arxiv or pub.url %}
      <p>
      {% if pub.doi %}
         <i class="ai ai-doi"></i>
         <a href="https://doi.org/{{ pub.doi }}">{{ pub.doi }}</a>
      {% endif %}
      {% if pub.arxiv %}
         <i class="ai ai-arxiv"></i>
         <a href="https://arxiv.org/abs/{{ pub.arxiv.id }}">arXiv:{{ pub.arxiv.id }} [{{ pub.arxiv.cat }}]</a>
      {% endif %}
      {% if pub.url %}
         <i class="fa fa-link"></i>
         <a href="{{ pub.url }}">{{ pub.url }}</a>
      {% endif %}
      </p>
   {% endif %}
   </li>
{% endfor %}
</ol>

## Theses

{% assign theses = site.data.bnmr.publications.theses | sort: "published" | reverse %}

<ol reversed>
{% for pub in theses %}
   <li>
   {% if pub.author %}
      <p>
      {% for author in pub.author  %}
         {% if pub.author.size > 2 and author != pub.author.last %}
            {{ author | append: ", " }}
         {% elsif pub.author.size > 1 and author == pub.author.last %}
            {{ author | prepend: "and " | append: "." }}
         {% else %}
            {{ author | append: "." }}
         {% endif %}
      {% endfor %}
      </p>
   {% endif %}
   {% if pub.title %}
      <p>
      <i>{{ pub.title }}.</i>
      </p>
   {% endif %}
   {% if pub.degree and pub.school and pub.address and pub.year %}
      <p>
      {{ pub.degree }} Thesis ({{ pub.school }}, {{ pub.address }}, {{ pub.year }}).
      </p>
   {% endif %}
   {% if pub.abstract %}
      <details>
         <summary>Abstract</summary>
         <p>{{ pub.abstract }}</p>
      </details>
   {% endif %}
   {% if pub.doi or pub.arxiv or pub.url %}
      <p>
      {% if pub.doi %}
         <i class="ai ai-doi"></i>
         <a href="https://doi.org/{{ pub.doi }}">{{ pub.doi }}</a>
      {% endif %}
      {% if pub.arxiv %}
         <i class="ai ai-arxiv"></i>
         <a href="https://arxiv.org/abs/{{ pub.arxiv.id }}">arXiv:{{ pub.arxiv.id }} [{{ pub.arxiv.cat }}]</a>
      {% endif %}
      {% if pub.url %}
         <i class="fa fa-link"></i>
         <a href="{{ pub.url }}">{{ pub.url }}</a>
      {% endif %}
      </p>
   {% endif %}
   </li>
{% endfor %}
</ol>