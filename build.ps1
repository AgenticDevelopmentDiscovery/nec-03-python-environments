# Windows build wrapper.
#
# `just build` (see justfile) needs two things PowerShell doesn't have on PATH
# by default:
#   - `sh`, because the justfile recipes are POSIX shell lines (`mkdir -p`, …)
#   - `rsvg-convert`, to embed the SVG figures into the PDFs; without it pandoc
#     silently leaves the raw .svg in place and xelatex fails later with a
#     missing-file error.
# Both ship with Git for Windows / MSYS2, already installed on this machine,
# just not on PATH. This script adds them for the duration of the build only,
# then delegates everything else to `just` so the recipes stay the single
# source of truth.
#
# Usage:  .\build.ps1          (all three outputs, like `just build`)
#         .\build.ps1 doc      (just the document)
#         .\build.ps1 slides
#         .\build.ps1 site

param(
    [string]$Recipe = "build"
)

if ((Get-Command sh -ErrorAction SilentlyContinue) -eq $null) {
    $shDir = "C:\Program Files\Git\bin"
    if (Test-Path "$shDir\sh.exe") {
        $env:PATH = "$shDir;$env:PATH"
    } else {
        Write-Warning "sh.exe not found on PATH or at $shDir - just recipes will fail to run."
    }
}

if ((Get-Command rsvg-convert -ErrorAction SilentlyContinue) -eq $null) {
    $rsvgDir = "C:\msys64\mingw64\bin"
    if (Test-Path "$rsvgDir\rsvg-convert.exe") {
        $env:PATH = "$rsvgDir;$env:PATH"
    } else {
        Write-Warning "rsvg-convert not found on PATH or at $rsvgDir - SVG figures will fail to embed."
    }
}

just $Recipe
