---
layout: default
title: About
description: About me.
nav_order: 1
---

# About
{: .no_toc }

{% assign rmlm = site.data.rmlm.info %}

<dl>
   <dt>Github</dt>
   <dd><a href="{{ rmlm.github_username | prepend: "https://github.com/" }}">{{ rmlm.github_username }}</a></dd>
</dl>

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Education

{% assign education = rmlm.education | sort: "year" | reverse %}

<ul>
{% for e in education %}
   <li>
      <p>{{ e.degree }}, <a href="{{ e.url }}">{{ e.school }}</a>, {{ e.address }} ({{ e.year }}).</p>
      <dl>
         <dt>Supervisor</dt>
         <dd>{{ e.supervisor }}</dd>
         <dt>Thesis</dt>
         <dd>{{ e.thesis }}</dd>
      </dl>
   </li>
{% endfor %}
</ul>

## Publications

{% assign preprints = site.data.rmlm.publications.preprints | sort: "published" | reverse %}

### Electronic Preprints ({{ preprints.size }})

<ol>
{% for pub in preprints %}
   <li value="{{ forloop.length | minus: forloop.index0 }}">
   {% if pub.author %}
      <p>
      {% for author in pub.author  %}
         {% if pub.author.size > 2 and author != pub.author.last %}
            {{ author | replace: "R. M. L. McFadden", "<u>R. M. L. McFadden</u>" | replace: "R. M. L. Mcfadden", "<u>R. M. L. Mcfadden</u>" | append: ", " }}
         {% elsif pub.author.size > 1 and author == pub.author.last %}
            {{ author | replace: "R. M. L. McFadden", "<u>R. M. L. McFadden</u>" | replace: "R. M. L. Mcfadden", "<u>R. M. L. Mcfadden</u>" | prepend: "and " | append: "." }}
         {% else %}
            {{ author | replace: "R. M. L. McFadden", "<u>R. M. L. McFadden</u>" | replace: "R. M. L. Mcfadden", "<u>R. M. L. Mcfadden</u>" | append: "." }}
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
   <hr>
{% endfor %}
</ol>

{% assign articles = site.data.rmlm.publications.articles | sort: "published" | reverse %}

### Journal Articles ({{ articles.size }})

<ol>
{% for pub in articles %}
   <li value="{{ forloop.length | minus: forloop.index0 }}">
   {% if pub.author %}
      <p>
      {% for author in pub.author  %}
         {% if pub.author.size > 2 and author != pub.author.last %}
            {{ author | replace: "R. M. L. McFadden", "<u>R. M. L. McFadden</u>" | replace: "R. M. L. Mcfadden", "<u>R. M. L. Mcfadden</u>" | append: ", " }}
         {% elsif pub.author.size > 1 and author == pub.author.last %}
            {{ author | replace: "R. M. L. McFadden", "<u>R. M. L. McFadden</u>" | replace: "R. M. L. Mcfadden", "<u>R. M. L. Mcfadden</u>" | prepend: "and " | append: "." }}
         {% else %}
            {{ author | replace: "R. M. L. McFadden", "<u>R. M. L. McFadden</u>" | replace: "R. M. L. Mcfadden", "<u>R. M. L. Mcfadden</u>" | append: "." }}
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
   <hr>
{% endfor %}
</ol>

{% assign proceedings = site.data.rmlm.publications.proceedings | sort: "published" | reverse %}

### Conference Proceedings ({{ proceedings.size }})

<ol>
{% for pub in proceedings %}
   <li value="{{ forloop.length | minus: forloop.index0 }}">
   {% if pub.author %}
      <p>
      {% for author in pub.author  %}
         {% if pub.author.size > 2 and author != pub.author.last %}
            {{ author | replace: "R. M. L. McFadden", "<u>R. M. L. McFadden</u>" | replace: "R. M. L. Mcfadden", "<u>R. M. L. Mcfadden</u>" | append: ", " }}
         {% elsif pub.author.size > 1 and author == pub.author.last %}
            {{ author | replace: "R. M. L. McFadden", "<u>R. M. L. McFadden</u>" | replace: "R. M. L. Mcfadden", "<u>R. M. L. Mcfadden</u>" | prepend: "and " | append: "." }}
         {% else %}
            {{ author | replace: "R. M. L. McFadden", "<u>R. M. L. McFadden</u>" | replace: "R. M. L. Mcfadden", "<u>R. M. L. Mcfadden</u>" | append: "." }}
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
   <hr>
{% endfor %}
</ol>

{% assign theses = site.data.rmlm.publications.theses | sort: "published" | reverse %}

### Theses ({{ theses.size }})

<ol>
{% for pub in theses %}
   <li value="{{ forloop.length | minus: forloop.index0 }}">
   {% if pub.author %}
      <p>
      {% for author in pub.author  %}
         {% if pub.author.size > 2 and author != pub.author.last %}
            {{ author | replace: "R. M. L. McFadden", "<u>R. M. L. McFadden</u>" | replace: "R. M. L. Mcfadden", "<u>R. M. L. Mcfadden</u>" | append: ", " }}
         {% elsif pub.author.size > 1 and author == pub.author.last %}
            {{ author | replace: "R. M. L. McFadden", "<u>R. M. L. McFadden</u>" | replace: "R. M. L. Mcfadden", "<u>R. M. L. Mcfadden</u>" | prepend: "and " | append: "." }}
         {% else %}
            {{ author | replace: "R. M. L. McFadden", "<u>R. M. L. McFadden</u>" | replace: "R. M. L. Mcfadden", "<u>R. M. L. Mcfadden</u>" | append: "." }}
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
   <hr>
{% endfor %}
</ol>
