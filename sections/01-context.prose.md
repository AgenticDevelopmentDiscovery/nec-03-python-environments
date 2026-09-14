# Context

## What this is

A Python environment is an isolated set of installed packages tied to one
interpreter, so one project's dependencies can't collide with another's.
`venv` is the built-in version: a per-project folder with its own `python`
and `site-packages`. `conda` extends this to non-Python and binary
dependencies; `uv` is a fast modern resolver that builds environments and
lockfiles in seconds. Whatever the tool, a **lockfile** is what makes it
reproducible — it records the full resolved dependency tree, every
transitive package pinned, so anyone can reconstruct the identical
environment.

## Where it came from

Before `venv` — standard since Python 3.3 — every project on a machine shared
one global `site-packages` — two projects needing different versions of the
same library simply couldn't coexist.

![Before `venv`, two projects collide over one shared site-packages. After, each gets its own.](figures/isolation-before-after.svg){#fig:isolation width=92%}

`conda` grew out of the scientific Python community, for packages wrapping
compiled C/Fortran code `pip` can't build. `uv` is newer still: the same
jobs, an order of magnitude faster, with the lockfile built in rather than
bolted on.

## What this tutorial covers

This tutorial covers creating environments with `venv` and `uv`, when to
reach for `conda` instead, and the difference between pinning a dependency
and locking the full resolved tree — what actually makes a run reproducible.
The hands-on demo builds an environment two ways, locks it, deletes it, and
rebuilds it from the lock to prove the point. It does not cover PyPI
packaging or container-level reproducibility (Docker). By the end, you'll be
able to create, lock, and reconstruct a Python environment — and explain why
a lockfile, not a pinned `requirements.txt`, is what makes a result
reproducible.
