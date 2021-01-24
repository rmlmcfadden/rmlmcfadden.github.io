---
layout: default
title: RustBCA
description: Rust Binary Collision Approximation
parent: Ion Implantation
---

# `RustBCA`

`RustBCA` is a new codebase for simulating ion-material interactions using the
binary collision approximation ([BCA]). The source code is written in the modern
programming language [Rust], meaning is produces highly performant machine code,
but without the pitfalls associated with the languages traditionally used in
scientific computing.

A key feature of the project is <i>flexibility</i>, including the ability script
each calculation using a sensible input format ([TOML]), as well as define which
atomic potential(s) should be used. Though it is not nearly as mature as its
alternatives, I think in time it will be their successor.

The GitHub page for the project can be found here:

<https://github.com/lcpp-org/RustBCA>

[BCA]: https://en.wikipedia.org/wiki/Binary_collision_approximation
[Rust]: https://www.rust-lang.org/
[TOML]: https://en.wikipedia.org/wiki/TOML
