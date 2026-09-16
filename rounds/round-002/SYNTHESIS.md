# Round 2 — Synthesis

**Panel recommendation:** needs revision
**Seats:** clarity needs revision · pedagogy needs revision · visual needs revision

## Since last round

None of round 1's seven docket items were completed. The edits made between rounds 1 and 2 were structural rather than targeted at the docket — three units were converted from prose to bulleted lists (`01-context`'s "What this is" and "What this tutorial covers," `04-conclusion`'s "Where to go next"), and `03-content`'s Demo was rewritten around a new, unexplained "bike-sharing example" in place of the symbolic-regression substrate `topic.md` and `02-motivation` still describe. None of that touches what round 1 actually asked for, and two of the structural edits introduced new problems this round's panel caught independently (see Consensus and Docket).

1. Make the Demo section executable — **not done.** The section was rewritten (renamed, shortened to three bullets, the `venv`-vs-`uv` comparison dropped to `uv` alone) but remains pure narration: no path, command, or expected output. Pedagogy this round found the only real recipe in the repo, `bike-sharing-offline-trial/demo/README.md`, is an unlinked, presenter-only script ("**Say:** ...", explicitly marked not part of the assignment) — the gap round 1 flagged is not just unfixed, it's now traceable to a specific unused asset.
2. Write C1/C2/C4 into "What you can do now" — **not done.** The section is byte-for-byte unchanged. Clarity and pedagogy both reconfirmed the gap independently this round, exactly as they did last round — a 2-seat consensus finding surviving two rounds unchanged. See Consensus below.
3. Add `PYTHONHASHSEED` to Pitfalls — **not done.** Unchanged; pedagogy reconfirmed.
4. Confirm/fix "Where it came from" slide overflow — **not done.** Unchanged text; visual reconfirmed the identical overflow risk, still unverified against a render in either round.
5. Fix the "same three jobs" callback — **not done.** Unchanged; visual reconfirmed it verbatim.
6. Give "What this tutorial covers" a working roadmap sentence — **overtaken.** The unit was rewritten as a bulleted list rather than fixed as prose. The specific sentence-fragment finding no longer applies in the same form, but a broader register-consistency problem replaced it (see Docket #3).
7. Define "interpreter" alongside spec and lockfile — **not done.** Unchanged text. The same undefined-term pattern is now also flagged for "package set" (see Docket #4).

## Consensus
- **C1/C2/C4 downstream content is still missing from "What you can do now," for the second round running.** Clarity and pedagogy both independently reconfirmed this — the exact same 2-seat pairing as round 1, against exactly the same unchanged text. This is the clearest recurrence in the project: `topic.md` §Shape and `04-conclusion.concepts.md`'s own Decisions log both state this content exists, and it does not.

## Conflicts
- none

## Docket
1. **Make the Demo section executable** — `sections/03-content.prose.md` § Demo: prove it with the bike-sharing example
   *Raised by:* pedagogy · *Effort:* medium
   Replace the three abstract bullets with the actual sequence: working directory, literal commands, and the specific output that confirms success (RMSE digits before/after) — mirroring Parts 0–2 of `bike-sharing-offline-trial/demo/README.md`. Either adapt it into a first-person walkthrough the declared reader runs solo, or frame it explicitly as "here's what you'll watch happen" and link the presenter script as its source. Second round this has been the top-ranked item; last round it was 3-seat consensus (clarity, pedagogy, visual all flagged it from different angles) and the specific defect — narration with no path, command, or output — is unchanged.

2. **Write the C1/C2/C4 downstream content into "What you can do now"** — `sections/04-conclusion.prose.md` § What you can do now
   *Raised by:* clarity · pedagogy · *Effort:* small
   Add the clause per challenge that `topic.md` §Shape promises and `04-conclusion.concepts.md`'s Decisions log already claims exists. Two rounds, two-seat consensus both times, against unchanged text — see Consensus above.

3. **Rewrite `01-context`'s two bulleted units back to prose** — `sections/01-context.prose.md` §§ What this is / What this tutorial covers
   *Raised by:* clarity · visual · *Effort:* small–medium
   Clarity: the section now shifts register three times (list → prose → prose "Where it came from" → list), reading as assembled notes rather than the document's established voice, and is the reader's very first impression of it. Visual, independently: both bulleted units are five full-sentence items apiece with no figure to absorb the density — plausible slide-overflow risk on the deck's first three slides. Two seats naming the same passages for different reasons, converging on the same fix: both want these two units back to 2–4 sentence prose paragraphs, matching "Where it came from" and the rest of the document.

4. **Define "interpreter" and "package set" where the four terms are introduced** — `sections/03-content.prose.md` § How it works: spec to lockfile
   *Raised by:* clarity · *Effort:* small
   "Four things are easy to confuse" promises four definitions; only spec and lockfile get one. Round 1 flagged "interpreter" specifically; round 2's independent read flagged "package set" instead — same unresolved defect, two instances of it now on record. Give each a short defining clause at first mention.

5. **Confirm and fix the "Where it came from" slide** — `sections/01-context.prose.md` § Where it came from
   *Raised by:* visual · *Effort:* medium
   Second round flagged, text unchanged both times. The unit's figure (`figures/isolation-before-after.svg`, 980×300 viewBox) is proportionally the tallest in the document — 30.6% of width vs. 19–22% for the `03-content` figures already tuned to survive this constraint — while carrying a history paragraph before it and a `conda`/`uv` paragraph after. Look at `output/slides.pdf` first; if it overflows, move the closing `conda`/`uv` sentence into "What this is" (where both tools are already named) so this unit is just the history plus the figure.

6. **Make the two-header-spanning openers stand alone** — `sections/03-content.prose.md` § `uv`: fast installs and lockfiles / § How it works: lockfile to environment
   *Raised by:* visual · *Effort:* small
   "`uv` does the same three jobs faster" (recurring from round 1, unchanged, and the count is also wrong — `venv`'s walkthrough shows four commands, not three) and "The lockfile isn't a second spec" (new this round) both presuppose the reader just saw the previous slide. Reword each to name what it's contrasting against inline, so both survive a reader landing on the slide or the page directly.

7. **Add `PYTHONHASHSEED` to the seeding pitfall** — `sections/03-content.prose.md` § Pitfalls
   *Raised by:* pedagogy · *Effort:* small
   Second round flagged, unchanged both times. `topic.md` scopes seeding as covering both library seeds and `PYTHONHASHSEED`; the shipped bullet names only `random.seed(42)`.

## Deferred
- "Pinning" is used in `02-motivation.prose.md` before `01-context.prose.md` ever defines it, despite `01-context.concepts.md`'s own Claims listing that distinction as owed there — `sections/01-context.prose.md` § What this is (clarity, new this round).
- Every `venv`/`uv` command lives only inside SVG figures, nothing copyable as text — `sections/03-content.prose.md` (pedagogy, new this round).
- Add a small figure for the seeding/locking independence claim (the one core `03-content.concepts.md` Claim with no visual) — `sections/03-content.prose.md` § Pitfalls (visual, new this round).
- Split the first bullet of "Where to go next" — it bundles two pointers (venv/pip docs, then uv docs) where every other bullet carries one — `sections/04-conclusion.prose.md` (visual, new this round, near-miss overflow).

## Do next
1. Make the Demo section executable (docket #1) — two rounds running as the top-ranked item; this is the tutorial's stated central proof and it still isn't on the page.
2. Write the C1/C2/C4 content into "What you can do now" (docket #2) — two-round, two-seat consensus against unchanged text; cheapest high-leverage fix available.
3. Rewrite `01-context`'s two bulleted units back to prose (docket #3) — cheap, and reverses a self-inflicted regression from the edits made since round 1 before it compounds further.

## Panel health
- I noticed something no seat named directly: `03-content.prose.md`'s Demo section now runs on a "bike-sharing example" that appears nowhere else in the document. `topic.md` §Shape names "the course's own symbolic-regression substrate" and "the linear-regression baseline" as the worked example, and `02-motivation.prose.md` (unchanged) still frames its failure case around a SciPy/NumPy version bump (`figures/drift-chain.svg` says so explicitly). The Demo section is supposed to be where `02-motivation`'s failure case "is reproduced on purpose" — but the substrate it now names doesn't match either the proposal or the section it's supposed to cash out. Clarity's brief asks it to judge whether "notation and naming... [are] quietly redefined halfway through," which is close to this, but a worked-example swap to a differently-named example seems to have read as a fresh detail rather than a redefinition — worth a look, and possibly worth sharpening `clarity.md` or `pedagogy.md`'s brief to explicitly check the worked example against `topic.md`'s Shape section by name, not just by capability.