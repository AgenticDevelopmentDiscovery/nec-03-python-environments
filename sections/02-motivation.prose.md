# Motivation

## Why it matters for agentic development

An agent run is an experiment, not a one-off script: it fits a baseline or
scores against an eval harness, and the result only means something if the
environment that produced it is fixed. An agent iterates unattended, often
across many runs and machines, with nobody watching a library quietly change
underneath it. Pinned environments and lockfiles are what let you reproduce a
leaderboard result, hand it to a collaborator, and trust that a regression is
real — not a dependency that drifted. The environment is part of the
artifact; without it, the result isn't auditable.

## What goes wrong without it

An agent reports a fitness score; a rerun a week later gives a different
number, with no code change.

![An unpinned dependency drifts, the score moves, and it reads as a code regression instead of environment drift.](figures/drift-chain.svg){#fig:drift width=92%}

The natural read is that the harness is unreliable. The real fault is an
unpinned dependency — and without a lockfile, nothing tells the two apart.

## When to reach for it

Lock the environment for anything you'll compare, share, or trust later — a
leaderboard entry, a baseline others build on, an experiment you'll revisit.
A throwaway exploration you're about to discard doesn't need it: the
overhead only pays off once a result has to outlive the session that made
it.
