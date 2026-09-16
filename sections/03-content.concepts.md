# Content — spine

> Note form only; never rendered. See `01-context.concepts.md` for what each
> heading is for.

## Purpose

Teach the HOW: the mental model, then worked use, then the failure modes — so
the reader can use the tool on a case this tutorial never showed them.

## Claims

- Interpreter, package set, and spec are three separate things; a lockfile is
  what lets you replay a resolution instead of recomputing it.
- `venv`+`pip` and `uv` solve the same problem — `uv`'s edge is speed and a
  built-in lockfile, not a new capability `venv` lacks.
- Environment locking and randomness seeding are independent: a locked
  environment with an unseeded RNG still doesn't reproduce.

## Decisions

- Demo proves reproducibility by destruction (delete the env, rebuild from
  the lock, rerun, compare) rather than asserting it — chosen because showing
  beats asserting, per the template's guidance on the "going further" unit.
- Used the course's own symbolic-regression substrate and eval harness as the
  worked example, rather than a generic toy project — keeps this section
  anchored to the same failure case `02-motivation` describes.
- `conda` is described (in "How it works") but not walked through hands-on —
  rejected running a third parallel workflow because it would spend slide
  budget without adding to the pinning/lockfile point, which `venv`/`uv`
  already make.
- Split into six `##` units rather than the shipped four — "How it works,"
  the two tool walkthroughs, pinning-vs-lockfile, the demo, and pitfalls each
  carry one idea, and each was written to a slide's worth of material rather
  than combined; confirmed against a rendered deck, no overflow.
- Added `figures/venv-create.svg` and `figures/uv-lockfile.svg` — one per
  tool walkthrough, each command annotated with an arrow to its meaning — and
  cut the prose that used to spell out the same line-by-line detail in
  sentence form, so the figure carries it instead of duplicating it. The
  remaining prose in each section is only what the figure doesn't cover (the
  framing sentence, and — for `uv` — the pointer to `conda`).
- First pass at both figures (three-line captions under each arrow) overflowed
  the slide — the caption below the image was clipped by the frame edge.
  Fixed by compressing the SVG viewBox, cutting each caption to one line, and
  shortening the framing sentence before the figure; confirmed against a
  rendered deck (`output/slides.pdf` pp. 9–10) and the document (`output/document.pdf`
  p. 3–4), no clipping in either.
- Added `figures/env-mental-model.svg` to "How it works" — this answers the
  open question below about that unit being too dense for one slide: instead
  of splitting it into two `##` units, the interpreter/package-set/spec/
  lockfile relationship moved into a diagram (resolve vs. replay, as two
  arrows into one package-set box) and the prose dropped from one long
  paragraph to a two-sentence frame plus a two-sentence close. Kept it as one
  `##` unit since the figure now carries the part that was making it dense.
- Added `figures/pin-vs-lock-tree.svg` to "Pinning vs. lockfiles" — a
  two-panel dependency tree (pin-only leaves transitive nodes floating;
  lockfile pins every node), reusing the before/after grammar from
  `figures/isolation-before-after.svg` in `01-context` so the deck has one
  consistent visual language for "here's the gap, here's it closed." Cut the
  `numpy==2.1.3` prose example and moved it into the figure; also dropped it
  from the first Pitfalls bullet, which was restating the same example a
  second time now that the figure shows it.
- First pass overflowed the slide (closing sentence clipped) the same way
  the venv/uv figures first did — figure at 300px viewBox left no headroom.
  Fixed the same way: compressed to 210px, trimmed the sentence on each side;
  confirmed against a rendered deck (`output/slides.pdf` p. 11), no clipping.
  Three figures in this section have now hit this exact failure mode on the
  first pass — worth remembering as a default starting size next time
  (viewBox height ≲ 210 for a figure that shares a slide with two sentences
  of prose), rather than rediscovering it per figure.
- Considered a fifth figure for the Demo unit (a step-flow: build twice →
  lock → delete → rebuild → compare → bump → compare) and decided against it
  — the prose is already a concrete, ordered sequence of actions to actually
  run, which is what `pedagogy`'s "follow-along" criterion wants; a diagram
  of steps that are themselves already a numbered narrative would restate,
  not clarify. Four figures in one `##`-section is already a lot — a fifth
  risked `visual`'s "do not reward figure count" flag.

- Split "How it works" into two `##` units — "spec to lockfile" and
  "lockfile to environment" — after user feedback that the resolve/replay
  dual-branch diagram should instead read as one linear pipeline: spec
  handed to the interpreter resolves into a lockfile; that lockfile handed
  back to the interpreter installs the exact package set, which together
  with the interpreter *is* the environment. Replaced the single
  `env-mental-model.svg` (which drew both branches at once) with two
  figures, one per step (`env-mental-model.svg`, `env-mental-model-2.svg`),
  since the two-step story doesn't fit one honest diagram at slide size —
  same reasoning as every other split in this file, applied to a figure
  instead of prose. Confirmed against a rendered deck (`output/slides.pdf`
  pp. 8–9), comfortable room on both, not just clearing the frame edge.
- Addressed three reader questions logged in `questions.txt` (slide 8: how
  does spec relate to what follows, is `requirements.txt` a spec, is spec a
  form of pinning; slide 10: does the lockfile update live, how does
  `uv.lock` differ from `venv`'s `requirements-lock.txt`; slide 13: what is
  seeding) without adding a figure or a `##` unit. "How it works" gained one
  clause naming `requirements.txt` as the spec and forward-pointing to the
  two sections that turn it into a lockfile — deliberately *not* added to
  `env-mental-model.svg` itself, since an earlier decision (below) already
  moved that figure away from filenames and onto the loose-vs-exact property,
  and reintroducing them would undo that. "Pinning vs. lockfiles" gained
  three words ("in the spec") tying pinning to the spec instead of treating
  them as synonyms. The `uv` section's answer went into
  `figures/uv-lockfile.svg`'s caption instead of prose — replaced "full
  resolved tree; uv sync replays it exactly" with "hashes + platform pins —
  rerun to update," mirroring `venv-create.svg`'s existing "rerun to update"
  answer to the same real-time question, so the two figures now answer it
  the same way instead of one prose block growing lopsided against the
  other. Pitfalls gained a one-clause definition of seeding
  (`random.seed(42)`) since that bullet named the term without defining it.
  Confirmed against a rendered deck (`output/slides.pdf` pp. 8, 11, 13, 16)
  — no overflow on any of the four touched slides.
- Fixed `figures/drift-chain.svg`: the right-hand "actual: environment
  moved" box ran to x=1000 inside a 980-wide viewBox, clipping its last 20px
  in every output. Widened the viewBox (and background rect) to 1020 to
  match the existing ~20px margin on the left rather than resizing the
  boxes.
- Reworked `figures/env-mental-model.svg` after user feedback that the
  spec-vs-lockfile distinction wasn't landing — the boxes were labeled by
  filename (`requirements.txt`, `uv.lock`), which names the artifact but not
  the property that matters. Changed the box contents to an actual loose
  constraint vs. an actual pin (`numpy>=2.0` vs. `numpy==2.1.3`) and reworded
  the arrow labels from vague ("can give a different answer" / "the same,
  every time") to causal ("asks the index — can change" / "no index needed
  — can't drift"). Added a matching sentence to the prose so the distinction
  is stated in words, not left to the figure alone.
- Added a fourth command to `figures/venv-create.svg` — `pip freeze >
  requirements-lock.txt` — after user feedback that the `venv` walkthrough
  showed only the spec-based install with no lockfile step at all, unlike
  the `uv` walkthrough that ends in `uv lock`. `pip`/`venv` has no built-in
  resolver-grade lockfile; `pip freeze` is the standard workaround (pins
  every installed version, no hashes or cross-platform resolution). Added a
  prose sentence stating that caveat explicitly, and reworded the framing
  sentence ("create, activate, install... freeze") to match the new step.
  This also answers "how do you update it": rerun `pip freeze` by hand,
  which the figure's caption says directly ("rerun to update").
- Both reworked figures overflowed their slide on first render — same
  failure mode as before, worse this time because the explanatory rewrite
  made the prose *longer*, not shorter, working against the fix. Took two
  more rounds each to actually land: `env-mental-model.svg` shrank 300px→
  220px viewBox and the caption/prose dropped by roughly half; `venv-create.svg`
  grew to 320px to fit the new row, then had to shrink to 280px once the
  trailing sentence was added. Confirmed clean on a full rendered-deck re-scan
  (`output/slides.pdf`, all 16 content slides), not just the two that broke.
  Lesson restated from before, now with a number attached: when a figure
  grows *or* the prose next to it grows, re-render before calling it done —
  "made it clearer" and "still fits" are two different checks.

## Open questions

- Now that "How it works," both tool walkthroughs, and "Pinning vs.
  lockfiles" all carry a figure, does this section read as visually
  front-loaded, with "Demo" and "Pitfalls" comparatively bare? For the
  `visual` reviewer — the two text-only units are text-only by choice (see
  Decisions), not by omission, but worth an outside read.

## Not doing

- Not covering `poetry` or `pipenv` — `venv` and `uv` are enough to make the
  pinning/lockfile point without a tool survey.
- Not walking through `conda` hands-on — described in "How it works" only.
