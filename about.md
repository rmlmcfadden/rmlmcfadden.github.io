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
    <dt>GitLab <i class="fab fa-gitlab"></i></dt>
    <dd><a href="{{ rmlm.gitlab_username | prepend: "https://gitlab.com/" }}">{{ rmlm.gitlab_username }}</a></dd>
    <dt>Bitbucket <i class="fab fa-bitbucket"></i></dt>
    <dd><a href="{{ rmlm.bitbucket_username | prepend: "https://bitbucket.org/" }}">{{ rmlm.bitbucket_username }}</a></dd>
</dl>

I'm currently a Postdoctoral Researcher at [TRIUMF] - Canada's particle
accelerator centre - where I share affiliation with both Accelerator and Life
Sciences Divisions though my supervisors ([T. Junginger] and [M. Stachura]).
My research focuses on the use of radioactive beams as tools for studying the
chemistry and physics of materials, primarily though the
[β-NMR]({% link bnmr.md %}) and [μSR]({% link musr.md %}) techniques.
A list of my scholarly works can be found through my Open Researcher and
Contributor ID (ORCID):
<a href="{{ rmlm.orcid | prepend: "https://orcid.org/" }}">{{ rmlm.orcid }}</a>.

I'm also an avid, self-taught programmer, and have written hundreds of short
scripts (mostly in [Python]) and larger codebases (mainly in [C++]) in my
day-to-day work over the last decade. This has mostly been for the purpose of
completing my own academic projects, but I do try to follow language
developments out of personal interest. For instance, I'm (slowly) learning
[Rust] in my spare time.

Besides these "professional" interests, some of my hobbies include:
cycling, running, skateboarding, cooking, and consuming craft beer.

[T. Junginger]: https://www.triumf.ca/profiles/5656
[M. Stachura]: https://www.triumf.ca/profiles/5570
[TRIUMF]: https://www.triumf.ca/
[C++]: https://isocpp.org/
[Python]: https://www.python.org/
[Rust]: https://www.rust-lang.org/
