# Round 1 — Synthesis

**Panel recommendation:** needs revision
**Seats:** clarity needs revision · pedagogy needs revision · visual minor polish

## Since last round
First round — no prior docket.

## Consensus
- **The Demo section is the document's weakest point, flagged by all three seats from different angles.** Clarity: it narrates rather than shows ("build the same environment two ways... rebuild it from the lock alone, and rerun") with no commands, unlike every walkthrough before it. Pedagogy: it is literally not executable from the page — the tutorial's one proof step, and the only hands-on claim in the document with zero backing transcript or figure, failing the "follow-along" criterion outright. Visual: it is one of only two units in the section with no figure, and independently flagged as the densest text-only unit in the document (an estimated overflow risk, unconfirmed). Three seats, three different lenses, one passage: `sections/03-content.prose.md` § Demo: prove it with the symbolic-regression substrate.
- **04-conclusion's "What you can do now" omits the C1/C2/C4 downstream content that both `topic.md` §Shape and `03-content.concepts.md`'s own Decisions log say was already folded in.** Clarity and pedagogy both independently caught the same gap: the spine describes prose that was never written — the promise-not-delivery pattern the sidecar exists to surface, here catching itself before either reviewer had to.

## Conflicts
- none

## Docket
1. **Make the Demo section executable** — `sections/03-content.prose.md` § Demo: prove it with the symbolic-regression substrate
   *Raised by:* clarity · pedagogy · visual · *Effort:* medium
   Replace the narrated paragraph with the actual command sequence or transcript for each named action (build via `venv`, build via `uv`, confirm identical fitness, lock, delete, rebuild from lock, rerun, confirm match, bump one dependency unpinned, rerun, observe drift) — matching the concreteness the `venv`/`uv` walkthrough sections above it already use. Once the transcript exists, consider pairing it with a compact outcome figure (visual's suggestion: reuse `drift-chain.svg`'s check/✗ grammar — two build paths converging on one fitness score, destroy-and-rebuild landing on that same score, the unpinned bump landing on a different one). The transcript is the fix; the figure is additive.

2. **Write the C1/C2/C4 downstream content into "What you can do now"** — `sections/04-conclusion.prose.md` § What you can do now
   *Raised by:* clarity · pedagogy · *Effort:* small
   Add the one clause per challenge that `topic.md` §Shape promises and `03-content.concepts.md`'s Decisions log already claims exists — closing a gap between the document's own stated intent and what actually shipped.

3. **Add `PYTHONHASHSEED` to the seeding pitfall** — `sections/03-content.prose.md` § Pitfalls
   *Raised by:* pedagogy · *Effort:* small
   `topic.md` scopes seeding as covering both library seeds and `PYTHONHASHSEED`; the shipped bullet names only `random.seed(42)`. One clause closes the gap.

4. **Confirm and fix the "Where it came from" slide** — `sections/01-context.prose.md` § Where it came from
   *Raised by:* visual · *Effort:* medium
   The unit carries the tallest figure in the document (`figures/isolation-before-after.svg`, ~300px viewBox) across two unrelated origin stories (venv's, then conda's/uv's), and — unlike every other figure in the project — its `concepts.md` entry logs no check against a rendered deck. Look at `output/slides.pdf` first; if it overflows, split venv's origin into its own unit, or shrink the figure toward the ~210px ceiling this project already uses elsewhere and cut the conda/uv close to one clause.

5. **Fix the "same three jobs" callback** — `sections/03-content.prose.md` § `uv`: fast installs and lockfiles
   *Raised by:* visual · *Effort:* small
   The count is wrong (`venv`'s walkthrough shows four commands, not three) and the phrase depends on the reader having just seen the `venv` slide, breaking on the presentation and website registers. Name the jobs inline, or drop the callback and let `figures/uv-lockfile.svg` carry it.

6. **Give "What this tutorial covers" a working roadmap sentence** — `sections/01-context.prose.md` § What this tutorial covers
   *Raised by:* clarity · *Effort:* small
   "The difference between pinning a dependency and locking the full resolved tree — what actually makes a run reproducible." has no main verb as its own sentence. Give it one, or convert the five-fragment roadmap into a short bulleted list.

7. **Define "interpreter" alongside spec and lockfile, or drop it from the four-things framing** — `sections/03-content.prose.md` § How it works: spec to lockfile
   *Raised by:* clarity · *Effort:* small
   The opening line promises four confusable terms defined; only spec and lockfile actually get a defining clause. Interpreter is used only as an actor ("hand it to the interpreter"), never itself defined.

## Deferred
- Name where the demo's substrate/baseline actually lives (repo, prior session, path) — `sections/03-content.prose.md` § Demo — pedagogy's own lowest-priority item; folds naturally into docket item 1's rewrite rather than needing separate action.

## Do next
1. Make the Demo section executable (docket #1) — the highest-leverage single fix, and the only passage all three independent seats converged on.
2. Write the C1/C2/C4 content into "What you can do now" (docket #2) — cheap, and closes a gap the document's own spine already admits exists.
3. Add `PYTHONHASHSEED` to the seeding pitfall (docket #3) — one clause, closes a scope gap `topic.md` names explicitly.

## Panel health
- I noticed a pattern no seat named directly: `sections/01-context.prose.md` and `sections/04-conclusion.prose.md` both use Markdown hard line-breaks (trailing double-spaces) to force single-sentence lines inside paragraphs that used to read as flowing prose. Clarity caught one *symptom* of this in `01-context` (the resulting sentence fragment in "What this tutorial covers") but didn't name the pattern itself, and didn't flag the same technique in `04-conclusion`'s "Where to go next" at all. None of the three briefs have source-level formatting/typography explicitly in scope, which may be why it surfaced only partially. Worth a direct look at how this renders in `output/slides.pdf` and `output/document.pdf` before the next round, and worth considering whether `clarity.md`'s brief should cover formatting mechanics, not just sentence-level wording, if this recurs.