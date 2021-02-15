---
layout: default
title: Publications
description: β-NMR publications.
parent: β-NMR
---

# Publications
{: .no_toc }

This is my (unoffical) curated list of β-NMR (and related) publications coming
out of [TRIUMF]. Most of the literature is related to materials science, but
results from nuclear physics experiments are also included for completeness.

For a glimpse at some of the ongoing research using the technique,
have a look at the [β-NMR / Experiments]({% link bnmr/experiments.md %}) page.

## Table of contents
{: .no_toc .text-delta}

1. TOC
{:toc}


{% assign preprints = site.data.bnmr.publications.preprints | sort: "published" | reverse %}

## Electronic Preprints ({{ preprints.size }})

{% include_relative publications_preprints.md %}



{% assign articles = site.data.bnmr.publications.articles | sort: "published" | reverse %}

## Journal Articles ({{ articles.size }})

{% include_relative publications_articles.md %}



{% assign reviews = site.data.bnmr.publications.reviews | sort: "published" | reverse %}

## Reviews ({{ reviews.size }})

{% include_relative publications_reviews.md %}



{% assign proceedings = site.data.bnmr.publications.proceedings | sort: "published" | reverse %}

## Conference Proceedings ({{ proceedings.size }})

{% include_relative publications_proceedings.md %}



{% assign theses = site.data.bnmr.publications.theses | sort: "published" | reverse %}

## Theses ({{ theses.size }})

{% include_relative publications_theses.md %}



[TRIUMF]: https://www.triumf.ca/
