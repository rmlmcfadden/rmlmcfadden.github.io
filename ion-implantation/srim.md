---
layout: default
title: SRIM
description: Stopping and range of ions in matter.
parent: Ion Implantation
---

# `SRIM`

The Stopping and Range of Ions in Matter (`SRIM`) is a collection of software
for calculations/simulations dealing with ion transport in matter.
This includes:

- ion stopping and range in targets,
- ion implantation,
- sputtering,
- ion transmisstion,
- and ion beam therapy.

Further details can be found at the `SRIM` homepage (<http://www.srim.org/>),
as well as the textbook sharing the same name:

---

<dl>
    <dt>Title</dt>
        <dd>SRIM - The Stopping and Range of Ions in Matter</dd>
    <dt>Author</dt>
        <dd>J. F. Ziegler, J. P. Biersack, M. D. Ziegler</dd>
    <dt>Edition</dt>
        <dd>7</dd>
    <dt>Publisher</dt>
        <dd>SRIM Co.</dd>
    <dt>Address</dt>
        <dd>Chester, MD</dd>
    <dt>Year</dt>
        <dd>2008>/dd>
    <dt>Cover</dt>
        <dd><img src="/assets/images/srim_textbook_cover.jpg" alt="SRIM textbook" width="25%"></dd>
</dl>

---

Papers dealing with specific versions of `SRIM` also exist:

- [SRIM 2010](https://doi.org/10.1016/j.nimb.2010.02.091)
- [SRIM 2003](https://doi.org/10.1016/j.nimb.2004.01.208)

Though the software is free, it is [closed source] and writtin in
(the now defunct language) [Visual Basic].
Niether of these traits are particularly appealing
(or sensible) by modern standards.
Nevertheless,
it offers a user friendly interface for a number of
complicated tasks that are useful for many branches of science
(e.g., the stopping profile of an implanted ion).

For those who prefer to work with scripts over `SRIM`'s [GUI],
check out [pysrim]({% link ion-implantation/pysrim.md %}),
which provides a nice [Python] interface to the application.

[closed source]: https://en.wikipedia.org/wiki/Proprietary_software
[Visual Basic]: https://en.wikipedia.org/wiki/Visual_Basic
[GUI]: https://en.wikipedia.org/wiki/Graphical_user_interface
[Python]: https://www.python.org/
