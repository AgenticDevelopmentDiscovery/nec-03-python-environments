# Conclusion

## What you can do now

You can create an isolated Python environment with `venv` or `uv`, lock it,
and reconstruct it exactly — on another machine, or after deleting the
original. You can explain why pinning isn't enough, and name the transitive
packages a lockfile catches that a pin misses.

## Where to go next

- For the `venv` and `pip` commands this tutorial only used a slice of, see
the official docs [@python-venv; @pip-userguide]. Start with the `uv` docs
[@uv-docs] for `uv run` and workspaces, which this tutorial didn't touch.  
- Read "Twelve-Factor App" [@twelve-factor] §Dependencies and §Config for the
same mindset applied to whole services.  
- If a dependency needs more than pure
Python and wheels, that's when to read the `conda`/`conda-lock` docs
[@conda-docs; @conda-lock].  
- Container-level reproducibility (Docker) is the
next layer down — worth knowing exists, out of scope here.

## Open edges

`uv`'s lockfile format is still young — do not treat `uv.lock` as a format to depend on staying fixed. And
locking the environment is only half of reproducibility: it fixes *what's
installed*, not *what happens at runtime* — GPU nondeterminism, unseeded
randomness, and network calls all sit outside what a lockfile can pin.

## References {.allowframebreaks}

::: {#refs}
:::
