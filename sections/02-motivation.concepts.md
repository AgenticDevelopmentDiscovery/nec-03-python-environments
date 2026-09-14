# Motivation — spine

> Note form only; never rendered. See `01-context.concepts.md` for what each
> heading is for.

## Purpose

Say WHY the topic is important for agentic development, and bound where it
applies.

## Claims

- A silent dependency bump can change an agent's fitted output with zero code
  changes — the failure is invisible until someone compares two runs.
- Without a lockfile, "my result changed" is unanswerable: no way to
  distinguish a real regression in code from an environment that drifted.
- Locking is worth the overhead only for results meant to be compared,
  shared, or revisited — not every throwaway run needs it.

## Decisions

- Made the failure case concrete (SciPy/NumPy version bump shifting a fitted
  score) using the course's own eval-harness substrate, rather than a generic
  "some library updated" — chosen because the template flags invented
  pitfalls as obviously invented to a reader who's hit the real ones.
- Scoped the value claim specifically to *unattended, iterative* agent runs
  (no human in the loop to notice drift) rather than a general reproducible-
  research argument, so the case doesn't read the same for any programming
  topic.
- Added `figures/drift-chain.svg` under "What goes wrong without it" — the
  causal chain (unpinned dep → version bump → numeric shift → score change)
  and the misdiagnosis it produces are two separate things the prose was
  asserting in one breath; the figure separates them (the chain, then the
  right/wrong conclusion) instead of asking the reader to hold both in one
  sentence. Cut the SciPy/NumPy blow-by-blow from the prose since the figure
  now carries it — the remaining text only states the setup and the moral.
- First pass overflowed the slide (the closing sentence was clipped by the
  frame edge) — the figure at 260px of viewBox height left no room for the
  paragraph after it. Fixed by compressing the figure to 190px and trimming
  both the sentence before and after it by about a third; confirmed against
  a rendered deck (`output/slides.pdf` p. 6), no clipping.

## Open questions

- Is there a real incident from a past cohort or the instructors' own runs to
  cite here instead of a hypothetical SciPy/NumPy bump?

## Not doing

- Not making a general "reproducibility is good science" argument — scoped
  to why *agent* experiments specifically need it, per the topic's brief.
