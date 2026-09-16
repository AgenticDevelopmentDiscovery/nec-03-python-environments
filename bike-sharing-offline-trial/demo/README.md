# Venv reproducibility demo — presenter script

Not part of the regression assignment. This walks through, live, in front
of the class: generate a lockfile from the project's declared dependencies,
delete the environment, rebuild it from the lock alone, and show the
numbers match to the last bit; then bump one dependency without pinning it
and show the numbers shift.

`demo/compare_rmse.py` reuses only the CSV loading from the real
`analyze_regression.py`. Its LAD/NNLAD fitting is a deliberately weakened
copy of the real thing: `analyze_regression.py` calls
`scipy.optimize.linprog(..., method="highs")` explicitly; this script
calls it with no `method=` at all, so it uses whatever solver
`linprog` defaults to. That default is not cosmetic — scipy changed it in
version 1.9 (2022) from `'interior-point'` to `'highs'`, a different
solver family with a different convergence guarantee, not a rounding
difference. Every method prints its test-set RMSE at full precision
(decimal + exact IEEE-754 hex); LAD and NNLAD also print the solver's own
success flag and message, so a version bump that changes the picked
algorithm is impossible to miss.

Rehearsed end-to-end on 2026-09-15; every output below is real, not a
prediction. Run all commands from the repo root, in PowerShell.

**Why Python 3.10:** this demo pins scipy to a genuinely old release
(1.7.3, from 2021) as its "locked a while back" baseline, and old scipy
has no prebuilt wheel for newer Pythons. 3.10 is the interpreter that has
prebuilt wheels for both the old scipy and the new one, so nothing needs
to compile from source live.

Before class starts, confirm the repo is at rest in its clean-slate state:
`pyproject.toml` declares `scipy==1.7.3` (an exact pin, not a range), and
neither `uv.lock` nor `.venv` exists yet — nothing has been resolved or
installed. If you're not sure, jump to **Resetting** at the bottom first.

---

## Part 0 — generate the lockfile

**Say:** "Before there's a lockfile, there's just `pyproject.toml`
declaring what this project needs. No `uv.lock`, no `.venv` — nothing has
been resolved yet. Let's turn that declaration into a lockfile."

**1. Show the declared dependencies, and that nothing's been resolved.**

```powershell
type pyproject.toml
dir uv.lock, .venv
```

Point at `scipy==1.7.3` — an exact pin, on purpose (Part 2 loosens this).
The `dir` command should error on both — nothing exists yet.

**2. Generate the lockfile.**

```powershell
uv lock
```

Expected:

```
Resolved 12 packages in 20ms
```

A new `uv.lock` file appears. **Say:** "Twelve packages — three we asked
for, nine transitive dependencies we never named (matplotlib alone pulls
in `pillow`, `fonttools`, `cycler`...). Every one of them is now pinned to
an exact version and an exact hash in this file. `uv.lock` is what
actually gets committed and reproduced — not `pyproject.toml`, which only
states *ranges* you're willing to accept."

Optionally open `uv.lock` and scroll to the `[[package]]` block for
`scipy`, pointing at its `version = "1.7.3"` and hash entries.

**3. Build the environment from that lock.**

```powershell
uv sync
```

Expected: creates `.venv`, installs all 11 resolved packages (`scipy`
itself plus its dependencies).

---

## Part 1 — the lockfile survives deleting the environment

**Say:** "Now let's prove that lock reproduces exactly, even after
deleting the environment completely."

**1. Run the script once, to set a baseline.**

```powershell
uv run python demo/compare_rmse.py
```

Expected:

```
numpy   1.22.4
scipy   1.7.3
    solver success=False status=4 : The solution does not satisfy the
    constraints within the required tolerance of 3.16E-04, yet no errors
    were raised and there is no certificate of infeasibility or
    unboundedness. ...
    solver success=False status=4 : (same message, for NNLAD)
  LS    RMSE = 1457.364860292828  [0x1.6c5759defc539p+10]
  LAD   RMSE = 1470.528582973419  [0x1.6fa1d44dae03ap+10]
  NNLS  RMSE = 1563.5478871298567  [0x1.86e310952e289p+10]
  NNLAD RMSE = 1567.8444942493943  [0x1.87f60c319bb3cp+10]
```

**Say:** "Notice: even on the *locked* environment, we already get
`success=False` twice — scipy's old default solver (interior-point)
doesn't fully converge on this problem. That's not a bug we're about to
introduce, that's already the reality of not pinning your solver choice.
Keep those two `success=False` lines in view — you'll want to compare
them to what happens after the bump."

**2. Delete the environment. All of it.**

```powershell
Remove-Item -Recurse -Force .venv
```

**Say:** "That directory is gone — every package, every file uv installed.
Nothing left but `pyproject.toml` and `uv.lock`."

**3. Rebuild purely from the lockfile.**

```powershell
uv sync
```

Watch the install list scroll — same package list, same versions, no
resolution happening (uv is reading `uv.lock`, not re-resolving from the
open internet).

**4. Rerun the script and diff by eye against step 1.**

```powershell
uv run python demo/compare_rmse.py
```

Identical output, every digit, every hex character, the exact same
warning message twice. **Say:** "Delete-and-rebuild-from-lock gave us the
identical result, down to the bit, including a stale solver warning
nobody asked for. That's what a lockfile buys you."

---

## Part 2 — bump one dependency without pinning it

**Say:** "Now let's do the ordinary thing that breaks real projects:
loosen one pin, no code touched."

**1. Edit `pyproject.toml` live.** Open it in your editor and change:

```diff
-    "scipy==1.7.3",
+    "scipy>=1.7.3",
```

Save. Point out: that's the *only* file changed. `demo/compare_rmse.py`
itself was not touched.

**2. Re-resolve just that one package.**

```powershell
uv lock --upgrade-package scipy
```

Expected:

```
Updated scipy v1.7.3 -> v1.13.1
```

**3. Sync and rerun.**

```powershell
uv sync
uv run python demo/compare_rmse.py
```

Expected:

```
numpy   1.22.4
scipy   1.13.1
    solver success=True status=0 : Optimization terminated successfully.
    (HiGHS Status 7: Optimal)
    solver success=True status=0 : Optimization terminated successfully.
    (HiGHS Status 7: Optimal)
  LS    RMSE = 1457.364860292828  [0x1.6c5759defc539p+10]
  LAD   RMSE = 1470.528567077177  [0x1.6fa1d40b018dfp+10]
  NNLS  RMSE = 1563.5478871298567  [0x1.86e310952e289p+10]
  NNLAD RMSE = 1567.8443940386974  [0x1.87f60a8d4b492p+10]
```

**4. Put the before/after side by side** and walk through three things
that changed, in order of how convincing they are to a room:

```
BEFORE (scipy 1.7.3, locked):  success=False status=4  LAD RMSE = 1470.528582973419
AFTER  (scipy 1.13.1, bumped): success=True  status=0  LAD RMSE = 1470.528567077177
```

- The solver's own **success flag flipped** — `False` to `True`, for both
  LAD and NNLAD. Before the bump, scipy was telling you (if you'd checked
  `result.success`, which the real assignment code does check) that it
  wasn't fully confident in its answer.
- The **message changed categorically** — a constraint-tolerance warning
  became "Optimization terminated successfully." Different solver
  algorithm entirely (`interior-point` vs `highs`), not a rounding
  artifact.
- The **RMSE moved at the 5th decimal place** for both LAD and NNLAD
  (`1470.528582973419` vs `1470.528567077177`) — real, visible without
  printing hex, but modest in size. Say so plainly: the headline here
  isn't the size of the number change, it's that the *kind* of algorithm
  silently changed underneath code that never asked for a specific one.
- Also point out what **didn't** move: `LS` and `NNLS` are bit-identical
  before and after (`numpy` never changed, and `NNLS` doesn't go through
  `linprog` at all). The drift is specific to the one code path that
  leaned on an unpinned default.

**Say, to close:** "One line changed in `pyproject.toml`, no code touched
at all, and two of these four numbers moved while two didn't — because
the two that moved were the two calls relying on a library default
instead of stating their choice explicitly. That's the same lesson as the
lockfile itself, one layer down: pin what you depend on, whether that's a
package version or a function argument."

---

## Resetting for a second take

**Full reset, back to the true Part 0 starting point** (no lockfile, no
environment — for running the whole demo again from the top):

```powershell
Remove-Item -Recurse -Force .venv
Remove-Item -Force uv.lock
```

If `pyproject.toml` isn't already back to `"scipy==1.7.3",` (an exact
pin), restore it too — `git checkout -- pyproject.toml` if it's committed,
otherwise edit it by hand. `dir uv.lock, .venv` should now error on both,
matching the state described at the top of this file.

**Quicker reset, just back to the Part 1 starting point** (skip
regenerating the lockfile from scratch, only undo the Part 2 bump):

```powershell
git checkout -- pyproject.toml   # or hand-edit back to "scipy==1.7.3",
uv lock
Remove-Item -Recurse -Force .venv
uv sync
```

Either way, `uv run python demo/compare_rmse.py` afterward should print
the exact Part 1 baseline again (including both `success=False`
warnings), confirming you're back at the start.
