# Context — spine

> The register that does not ship. This file is never rendered into the document,
> the slides, or the site — but the reviewers read it, and they judge whether what
> it promises is turning into prose.
>
> Keep it in note form. Prose here is a sign you wrote in the wrong file.

## Purpose

Say WHAT the topic is and where it came from, so the reader can hold it in mind
before being told why it matters or how to use it.

## Claims

- An environment is isolation (interpreter + packages), not any one tool —
  `venv`/`conda`/`uv` are three implementations of the same idea.
- A lockfile is not the same thing as a pin: a pin fixes a direct dependency,
  a lockfile fixes the entire resolved tree, transitive packages included.
- `venv` predates the alternatives because `pip`'s original global
  `site-packages` made two projects with conflicting version needs mutually
  exclusive on one machine.

## Decisions

- Define by function (isolation) before naming any tool — chosen over
  opening with "`venv` is..." so the reader isn't left thinking the definition
  *is* a specific tool.
- Origin kept to the one problem (global-install conflicts) that explains why
  `venv` looks the way it does, rather than a chronology of releases — a
  tool-history timeline was rejected as not explaining anything the reader
  meets later.
- `conda`'s origin (binary/compiled dependencies) is stated here but not
  demonstrated until later — `03-content` is where it's actually contrasted
  against `venv`/`uv`.
- Added `figures/isolation-before-after.svg` under "Where it came from" — the
  global-`site-packages`-conflict story is the clearest relationship in the
  whole section to show rather than tell, and the project's own
  `figures/README.md` flags this kind of before/after as a strong candidate.
  Cut the paragraph's blow-by-blow of the conflict since the figure now
  carries it; the remaining prose only states the fact (one global
  `site-packages`, `venv` since 3.3) and moves on to `conda`/`uv`, which the
  figure doesn't cover.
- Tightened "What this is" for concision (six sentences to five, cut
  redundant framing) without adding a figure there — it's a definition
  naming three tools, not a single relationship a diagram would clarify;
  a tool-comparison table would decorate more than it teaches at this point,
  before the reader has seen any of the three in use.

## Open questions

- How much `conda`/binary-dependency framing does this section need, given
  the audience already runs binary-heavy scientific packages (PySR, SciPy)?
- Is "before `venv`, `pip install` was global" still accurate enough to state
  flatly, or does it need a caveat about `virtualenv` (the third-party
  predecessor `venv` absorbed)?

## Not doing

- Not covering `pip`/PyPI packaging or publishing — a distribution problem,
  not a reproducibility one.
- Not covering container-level isolation (Docker) — one layer below the
  interpreter; a pointer for it belongs in `04-conclusion`, not here.
