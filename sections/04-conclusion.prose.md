# Conclusion

## What you can do now

You can create an isolated Python environment with `venv` or `uv`, lock it,
and reconstruct it exactly — on another machine, or after deleting the
original. You can explain why pinning isn't enough, and name the transitive
packages a lockfile catches that a pin misses. This isn't academic here:
it's the lockfile C1 requires as an artifact, what makes C2's leaderboard
comparable across students, and the precondition for C4's
generate→evaluate→select loop to run without a mid-loop reinstall quietly
changing what it measures.

## Where to go next

Start with the `uv` docs [@uv-docs] for `uv run` and workspaces, which this
tutorial didn't touch. Read "Twelve-Factor App" [@twelve-factor]
§Dependencies and §Config for the same mindset applied to whole services. If
a dependency needs more than pure Python and wheels, that's when to read the
`conda`/`conda-lock` docs [@conda-docs; @conda-lock] this tutorial only
described. Container-level reproducibility (Docker) is the next layer down —
worth knowing exists, out of scope here.

## Open edges

`uv`'s lockfile format is still young — treat `uv.lock` as something to
regenerate with a current `uv`, not a format to depend on staying fixed. And
locking the environment is only half of reproducibility: it fixes *what's
installed*, not *what happens at runtime* — GPU nondeterminism, unseeded
randomness, and network calls all sit outside what a lockfile can pin.
