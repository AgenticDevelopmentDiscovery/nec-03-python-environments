# Content

## How it works

Four things are easy to confuse: the **interpreter**, the **package set**,
the **spec**, and the **lockfile**.

![Spec: loose, resolved each time. Lockfile: exact, replayed each time.](figures/env-mental-model.svg){#fig:mental-model width=88%}

A spec is a range, resolved each install. A lockfile is one exact build,
replayed — so it can't drift.

## `venv`: create and activate

The built-in path: create, activate, install from the spec with `pip` —
then freeze what actually got installed into a lockfile of your own.

![`venv`: create, activate, install, freeze.](figures/venv-create.svg){#fig:venv-create width=90%}

It pins every version, but not hashes or platform — rerun it by hand after
any change.

## `uv`: fast installs and lockfiles

`uv` does the same three jobs faster, and treats the lockfile as a
first-class output.

![`uv`: create, install, lock.](figures/uv-lockfile.svg){#fig:uv-lockfile width=88%}

`conda` covers dependencies `uv`/`pip` can't build themselves — compiled
C/Fortran libraries, GPU toolkits — at the cost of a slower resolver; reach
for it when a dependency needs more than pure Python and wheels.

## Pinning vs. lockfiles

Pinning a direct dependency (`numpy==2.1.3`) fixes *that* package — not the
dozens it pulls in transitively.

![Pinning fixes one node; a lockfile pins the whole tree.](figures/pin-vs-lock-tree.svg){#fig:pin-vs-lock width=88%}

A lockfile pins all of them. Treat the spec as *intent* and the lockfile as
*fact*: commit both, reproduce from the lockfile.

## Demo: prove it with the symbolic-regression substrate

Build the same environment two ways — `venv`+`pip`, and separately `uv` —
and confirm both run the linear-regression baseline identically. Generate a
lockfile, **delete the environment entirely**, rebuild it from the lock
alone, and rerun: the fitness score matches to the last digit. Then bump one
dependency without pinning it and rerun — watch the score shift with no code
change, the exact failure `02-motivation` described, now reproduced on
purpose.

## Pitfalls

- **Pinning direct dependencies and calling it done.** Leaves every
  transitive dependency unpinned — only a lockfile closes that gap.
- **Never committing the lockfile.** One that lives on a single machine
  reproduces nothing.
- **Locking the environment and forgetting the random seed.** Environment
  locking and seeding are independent — fixing one doesn't fix the other.
