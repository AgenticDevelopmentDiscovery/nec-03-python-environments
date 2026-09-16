# Content

## How it works: spec to lockfile

Four things are easy to confuse: the **interpreter**, the **package set**,
the **spec**, and the **lockfile**.

![Spec: loose, written by hand. Handed to the interpreter, it resolves into a lockfile.](figures/env-mental-model.svg){#fig:mental-model width=88%}

A spec is loose, written by hand — `requirements.txt` is one. Hand it to
the interpreter and it resolves into a lockfile: one exact build, generated
once, not written by hand.

## How it works: lockfile to environment

The lockfile isn't a second spec — it's data the interpreter replays
instead of resolving.

![Lockfile handed to the interpreter installs the exact package set — together, the environment.](figures/env-mental-model-2.svg){#fig:mental-model-2 width=88%}

Hand it to the interpreter and it installs that exact package set, every
time — no re-resolving, so it can't drift. The next two sections write one:
`venv`'s manual freeze, and `uv`'s built-in `uv lock`.

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

Pinning a dependency in the spec (`numpy==2.1.3`) fixes *that* package —
not the dozens it pulls in transitively.

![Pinning fixes one node; a lockfile pins the whole tree.](figures/pin-vs-lock-tree.svg){#fig:pin-vs-lock width=88%}

A lockfile pins all of them. Treat the spec as *intent* and the lockfile as
*fact*: commit both, reproduce from the lockfile.

## Demo: prove it with the bike-sharing example

- Build an environment using `uv`
- Generate a lockfile, **delete the environment entirely**, rebuild it from the lock
alone, and rerun: the fitness score matches to the last digit.
- Then bump one dependency without pinning it and rerun — watch the score shift with no code
change.

## Pitfalls

- **Pinning direct dependencies and calling it done.** Leaves every
  transitive dependency unpinned — only a lockfile closes that gap.
- **Never committing the lockfile.** One that lives on a single machine
  reproduces nothing.
- **Locking the environment and forgetting the random seed.** *Seeding*
  fixes the RNG's starting state (`random.seed(42)`) so a stochastic run
  repeats; it's independent of environment locking — fixing one doesn't
  fix the other.
