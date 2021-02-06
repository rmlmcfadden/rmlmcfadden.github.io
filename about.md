---
layout: default
title: About
description: About me.
nav_order: 1
---

# About

{% assign rmlm = site.data.rmlm.info %}

<dl>
    <dt>Name</dt>
    <dd>{{ rmlm.name }}</dd>
    <dt>Location</dt>
    <dd>{{ rmlm.location }}</dd>
    <dt>ORCID</dt>
    <dd><a href="{{ rmlm.orcid | prepend: "https://orcid.org/" }}">{{ rmlm.orcid }}</a></dd>
    <dt>arXiv</dt>
    <dd><a href="{{ rmlm.arxiv | prepend: "https://arxiv.org/a/" }}">{{ rmlm.arxiv }}</a></dd>
    <dt>GitHub</dt>
    <dd><a href="{{ rmlm.github_username | prepend: "https://github.com/" }}">{{ rmlm.github_username }}</a></dd>
    <dt>GitLab</dt>
    <dd><a href="{{ rmlm.gitlab_username | prepend: "https://gitlab.com/" }}">{{ rmlm.gitlab_username }}</a></dd>
</dl>

I'm currently a Postdoctoral Researcher at TRIUMF, with affiliation in both the
Accelerator (T. Junginger) and Life Sciences (M. Stachura) Divisions.
My research interests are (primarily) in the use of radioactive beams as tools
for studying the chemistry and physics of materials, especially with
[β-NMR]({% link bnmr.md %})) and [μSR]({% link musr.md %}).

I'm also an avid, self-taught programmer, having frequently written short
scripts (in [Python]) and larger codebases (in [C++]) for much of the last
decade. Most of this has been for completing my own academic projects, but I do
try to follow language developments out of personal interest. In my spare time,
I'm starting to learn [Rust].

Besides these "professional" interests, my main hobbies include skateboarding,
running, reading novels, cooking, and consuming craft beer.

<img src="/assets/rmlm.jpg" title="{{ rmlm.name }}" width="100%"/>

[C++]: https://isocpp.org/
[Python]: https://www.python.org/
[Rust]: https://www.rust-lang.org/
