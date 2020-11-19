---
layout: default
title: Publications
description: β-NMR publications.
parent: β-NMR
---

# Publications
{: .no_toc }

This is my (unoffical) curated list of β-NMR (and related) publications coming
out of TRIUMF. Most of the literature is related to materials science, but
results from nuclear physics experiments are also included for completeness.

For an idea of what <i>unpublished</i> experiments have previously or are
currently being done using the technique, have a look the
[Experiments page]({{ site.baseurl }}{% link /bnmr/experiments.md %}).

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

{% assign preprints = site.data.bnmr.publications.preprints | sort: "published" | reverse %}

## Electronic Preprints ({{ preprints.size }})

<ol>
{% for pub in preprints %}
   <li value="{{ forloop.length | minus: forloop.index0 }}">
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

{% assign articles = site.data.bnmr.publications.articles | sort: "published" | reverse %}

## Journal Articles ({{ articles.size }})

<ol>
{% for pub in articles %}
   <li value="{{ forloop.length | minus: forloop.index0 }}">
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

{% assign proceedings = site.data.bnmr.publications.proceedings | sort: "published" | reverse %}

## Conference Proceedings ({{ proceedings.size }})

<ol>
{% for pub in proceedings %}
   <li value="{{ forloop.length | minus: forloop.index0 }}">
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

{% assign theses = site.data.bnmr.publications.theses | sort: "published" | reverse %}

## Theses ({{ theses.size }})

<ol>
{% for pub in theses %}
   <li value="{{ forloop.length | minus: forloop.index0 }}">
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
