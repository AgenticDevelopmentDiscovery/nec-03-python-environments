# Conclusion — spine

> Note form only; never rendered. See `01-context.concepts.md` for what each
> heading is for.

## Purpose

Say what the reader can now do, point at what comes next, and name what is still
open.

## Claims

- The capability this tutorial delivers is directly instrumentalized
  downstream: C1 (lockfile as a required repo artifact), C2 (deterministic
  fitness for a leaderboard comparable across students), C4 (a locked
  environment as a precondition for a reliable generate→evaluate→select
  loop).
- Locking the environment fixes what's installed, not what happens at
  runtime — it does not by itself make a run fully deterministic.

## Decisions

- Folded the C1/C2/C4 connections into "What you can do now" as concrete
  downstream use, rather than a separate "Connections" section — the shipped
  arc has no slot for one, and capability-with-application reads stronger
  than capability-then-a-list-of-course-codes a reader outside this course
  wouldn't recognize anyway.
- "Open edges" names two limits explicitly (lockfile format churn, and
  locking vs. runtime determinism) rather than one — kept both because they
  fail differently: one is "this specific tool is unsettled," the other is
  "this technique has an inherent boundary."
- Tightened all three units for concision (part of a whole-tutorial pass) and
  deliberately added no figure here — unlike `01`–`03`, nothing in this
  section is a mechanism or a relationship a diagram would clarify; it is a
  recap, a reading list, and a set of caveats. A figure here would be the
  exact "restates a list as boxes" defect `visual` is briefed to penalize.
- Wired real citations into "Where to go next" (`uv-docs`, `twelve-factor`,
  `conda-docs`, `conda-lock` in `references.bib`) — replaced the plain-text
  "the `uv` docs (Astral)" style mentions with `[@key]` so the sources are an
  actual, checkable bibliography, not just names. `references.bib` holds
  three more entries (`python-venv`, `pep405`, `pip-userguide`) that are
  documented but deliberately left uncited: citing all seven pushed the
  generated References slide past one frame (only ~5 of 7 entries fit, the
  rest clipped) — citeproc gives beamer no automatic multi-frame
  bibliography, and pandoc's per-heading class attributes don't reach the
  auto-generated bibliography heading, so there's no clean way to ask for
  `allowframebreaks` on it. Cutting to four is the same move this project
  makes for any other overflowing `##` unit: fewer things, not a smaller
  font. The three uncited entries are there for whoever adds the next
  citation to pick from, not a self-cleaning TODO — remove them if a round
  or a rewrite makes clear they'll never be cited.

## Open questions

- Is naming C1/C2/C4 by code too course-internal for a tutorial that might be
  read outside this cohort? Consider spelling out what each challenge is in
  one clause if the panel flags the codes as opaque.
- Should "Open edges" say more about *why* `uv.lock`'s format has changed, or
  is naming the risk (without the history) enough for this audience?

## Not doing

- Not claiming this tutorial makes agent runs fully deterministic — GPU
  nondeterminism and network calls are named as boundaries, not solved.
