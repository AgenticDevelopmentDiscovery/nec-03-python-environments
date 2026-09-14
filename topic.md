# Topic

## In one sentence

Python environments and lockfiles turn "works on my machine" into a
recreatable, auditable fact instead of a shrug.

## What it is

A Python environment is an isolated set of installed packages tied to a
specific interpreter, so one project's dependencies cannot collide with
another's. `venv` is the built-in per-project sandbox; `conda` extends the same
idea to non-Python and binary dependencies; `uv` is a fast modern
resolver/installer that builds environments and lockfiles in seconds.
Reproducibility on top of that comes from pinning — a loose requirement like
`numpy` means "whatever is newest today," a pinned one like `numpy==2.1.3`
means exactly that build — and, more completely, from a lockfile
(`uv.lock`, `poetry.lock`, `conda-lock`, or a fully-pinned `requirements.txt`)
that records the entire resolved dependency tree, transitive packages
included, so anyone on any machine can reconstruct the identical environment.

## Why it belongs in this course

Agent runs are experiments, and an experiment you cannot rerun is not
evidence. When an agent fits a baseline or scores against the eval harness,
the result only means something if the environment underneath it is fixed —
a silent version bump in a library the harness depends on can change outputs
or break it outright. Without pinning, a reported regression could be real or
could be a dependency that drifted; there is no way to tell them apart. This
is specific to agentic development, not programming generally: an agent
proposes and evaluates artifacts unattended, over many iterations, with no
human in the loop to notice that the ground shifted between runs.

## What the reader will be able to do

- Create an isolated environment with `venv` and with `uv`, and explain when
  each (or `conda`) is the right choice.
- Generate a lockfile and use it to reconstruct a byte-identical environment
  on a different machine or after deleting the original.
- Explain the difference between pinning a direct dependency and locking the
  full resolved tree, and why only the latter survives "works on my machine."
- Recognize an unpinned-dependency drift as the cause of a changed result,
  rather than mistaking it for a real regression.

## Scope

**In scope**

- `venv` and `uv` as the two hands-on tools; `conda` covered by description,
  not walked through, as the answer for non-Python/binary dependencies.
- Pinning vs. lockfiles, and `requirements.txt`/`pyproject.toml` (human-edited
  spec) vs. the lockfile (machine truth).
- Seeding randomness (`PYTHONHASHSEED`, library seeds) as the second axis of
  reproducibility, distinct from environment locking.
- Committing the lockfile as a repo artifact.

**Out of scope**

- Packaging and publishing a package to PyPI — a different problem
  (distribution, not reproducibility).
- Container-level reproducibility (Docker) — one layer below the interpreter;
  worth a pointer in "where to go next," not a section of its own.
- `poetry` and `pipenv` as hands-on tools — `venv` and `uv` make the
  pinning/lockfile point without a tool survey.

## Shape

- `03-content` carries the weight: the `venv` vs. `uv` walkthrough, the
  pinning-vs-lockfile distinction, and the destroy-and-rebuild demo that
  proves a lockfile actually reproduces the environment.
- The worked example in `03-content` is the course's own symbolic-regression
  substrate: build the environment two ways, lock it, delete it, rebuild from
  the lock, and rerun the linear-regression baseline to show identical
  fitness. The bonus (bump one dependency unpinned, watch the result shift)
  is the pitfall that motivates committing the lockfile.
- `02-motivation`'s failure case is a silent version bump in a library the
  eval harness depends on (e.g. SciPy or NumPy) changing fitted output —
  concrete and drawn from the same substrate as the demo, not a generic
  "a dependency updated."
- `04-conclusion` folds in how the capability is used downstream — C1's
  reproducible-repo challenge, C2's comparable leaderboard, C4's
  generate→evaluate→select loop — as concrete "what you can do now," since the
  shipped arc has no separate connections section.

## Open questions

- How much `conda`/binary-dependency framing does `01-context` need, given the
  audience already runs binary-heavy scientific packages?
- Does the destroy-and-rebuild demo need a figure (environment/lockfile
  relationship diagram), or does the CLI transcript carry it on its own?
- `uv`'s lockfile format is still young — how much to hedge that in
  `04-conclusion`'s open edges versus just teaching current practice?
