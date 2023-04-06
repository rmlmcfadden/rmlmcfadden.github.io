---
layout: default
title: About
description: About me.
nav_order: 1
---

# About

<img src="/assets/images/rmlm2.jpg" title="{{ rmlm.name }}" width="100%">

{% assign rmlm = site.data.rmlm.info %}

<dl>
    <dt>Name <i class="fas fa-user"></i></dt>
    <dd>{{ rmlm.name }}</dd>
    <dt>Location <i class="fas fa-map-marked"></i></dt>
    <dd><a href="{{ rmlm.location | prepend: "https://www.google.com/maps/place/" }}">{{ rmlm.location }}</a></dd>
    <dt>ORCID <i class="ai ai-orcid"></i></dt>
    <dd><a href="{{ rmlm.orcid | prepend: "https://orcid.org/" }}">{{ rmlm.orcid }}</a></dd>
    <dt>Google Scholar <i class="ai ai-google-scholar"></i></dt>
    <dd><a href="{{ rmlm.googlescholar | prepend: "https://scholar.google.ca/citations?hl=en&user=" }}">{{ rmlm.googlescholar }}</a></dd>
    <dt>arXiv <i class="ai ai-arxiv"></i></dt>
    <dd><a href="{{ rmlm.arxiv | prepend: "https://arxiv.org/a/" }}">{{ rmlm.arxiv }}</a></dd>
    <dt>GitHub <i class="fab fa-github"></i></dt>
    <dd><a href="{{ rmlm.github_username | prepend: "https://github.com/" }}">{{ rmlm.github_username }}</a></dd>
    <dt>Bitbucket <i class="fab fa-bitbucket"></i></dt>
    <dd><a href="{{ rmlm.bitbucket_username | prepend: "https://bitbucket.org/" }}">{{ rmlm.bitbucket_username }}</a></dd>
    <dt>GitLab <i class="fab fa-gitlab"></i></dt>
    <dd><a href="{{ rmlm.gitlab_username | prepend: "https://gitlab.com/" }}">{{ rmlm.gitlab_username }}</a></dd>
</dl>

I'm a Ph.D. scientist with 10+ years of research experience and 45+
peer-reviewed publications in journals run by reputable academic societies.
A list of my scholarly works can be found through
my
<a href="{{ rmlm.orcid | prepend: "https://orcid.org/" }}">Open Researcher and Contributor ID (ORCID)</a>;
or
my
<a href="{{ rmlm.googlescholar | prepend: "https://scholar.google.ca/citations?hl=en&user=" }}">Google Scholar profile</a>.
I have expertise in data analysis,
including the handling of large datasets and the use of advanced analytic
techniques
(e.g., mathematical modelling, non-linear regression, machine learning, etc.)
to extract quantitative insights.
I'm an avid computer programmer,
with over a decade of experience using, for example, [Python] and [C++]
to solve complex analysis workflows,
including the use software tools common to the domain of data science
(e.g., [NumPy], [SciPy], [pandas], [matplotlib], [TensorFlow], [Git], etc.).
I relish in the challenge of complex, interdisciplinary projects that require
both innovation and continuous learning.

Besides these "professional" interests, some of my hobbies include:
cycling, running, skateboarding, cooking, and consuming craft beer.

[T. Junginger]: https://www.triumf.ca/profiles/5656
[M. Stachura]: https://www.triumf.ca/profiles/5570
[TRIUMF]: https://www.triumf.ca/
[C++]: https://isocpp.org/
[Python]: https://www.python.org/
[Rust]: https://www.rust-lang.org/
[SciPy]: https://www.scipy.org/
[NumPy]: http://numpy.org/
[pandas]: http://pandas.pydata.org/
[matplotlib]: https://matplotlib.org/
[TensorFlow]: https://www.tensorflow.org/
[Git]: https://git-scm.com/
