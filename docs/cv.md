---
layout: default
title: CV
description: My curriculum vitae.
nav_order: 2
permalink: /cv
---

# CV
{: .no_toc }

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}

## Education

<table id="experiments">
   <thead>
      <th>Year</th>
      <th>Degree</th>
      <th>Institute</th>
      <th>Location</th>
   </thead>
   <tbody>
      <tr>
         <td>2020</td>
         <td>Ph.D.</td>
         <td><a href="https://www.ubc.ca/">University of British Columbia</a></td>
         <td><a href="https://vancouver.ca/">Vancouver, BC</a></td>
      </tr>
      <tr>
         <td>2013</td>
         <td>B.Sc. (Hons.)</td>
         <td><a href="https://www.mta.ca/">Mount Allison University</a></td>
         <td><a href="https://sackville.com/">Sackville, NB</a></td>
      </tr>
   </tbody>
</table>

## Awards & Honours

## Service & Membership

<table>
   <thead>
      <th>Year</th>
      <th>Position</th>
      <th>Event/Organization</th>
   </thead>
   <tbody>
      <tr>
         <td>2014-2020</td>
         <td>Student Representative</td>
         <td><a href="http://www.isosim.ubc.ca/">IsoSiM</a> Program Committee</td>
      </tr>
      <tr>
         <td>2018</td>
         <td>Canadian Representative</td>
         <td><a href="https://www.iaea.org/">IAEA</a> Technical Meeting <a href="https://www.iaea.org/events/iaea-technical-meeting-on-novel-multidisciplinary-applications-with-unstable-ion-beams-and-complementary-techniques">EVT1703385</a></td>
      </tr>
      <tr>
         <td>2016-2017</td>
         <td>Science Ambassador</td>
         <td><a href="https://www.triumf.ca/">TRIUMF</a></td>
      </tr>
      <tr>
         <td>2015</td>
         <td>Member</td>
         <td><a href="http://www.isosim.ubc.ca/">IsoSiM</a> Summer School Organizing Committee</td>
      </tr>
      <tr>
         <td>2014</td>
         <td>Member</td>
         <td><a href="https://www.cheminst.ca/about/about-csc/">Canadian Society for Chemistry</a></td>
      </tr>
      <tr>
         <td>2007-2012</td>
         <td>Member</td>
         <td><a href="https://www.mta.ca">MtA</a> Chemistry & Biochemistry Society</td>
      </tr>
   </tbody>
</table>

## Publications

### Electronic Preprints

{% assign preprints = site.data.rmlm.publications.preprints | sort: "published" | reverse %}

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

### Journal Articles

{% assign articles = site.data.rmlm.publications.articles | sort: "published" | reverse %}

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

### Conference Proceedings

{% assign proceedings = site.data.rmlm.publications.proceedings | sort: "published" | reverse %}

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

### Theses

{% assign theses = site.data.rmlm.publications.theses | sort: "published" | reverse %}

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
