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
