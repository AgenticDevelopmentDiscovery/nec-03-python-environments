"""Reproducibility demo helper -- not part of the regression assignment.

Reuses only the CSV loading from analyze_regression.py. The LAD/NNLAD
fitting here is a deliberately weakened copy of the real thing: the real
script calls scipy.optimize.linprog(..., method="highs") explicitly; this
one calls it with no method= at all, so it uses whatever solver
scipy.optimize.linprog defaults to. That default is not cosmetic -- scipy
changed it in version 1.9 (2022) from 'interior-point' to 'highs', a
different solver family with a different convergence guarantee.

Every method prints its test-set RMSE at full floating-point precision
(decimal + exact IEEE-754 hex), and LAD/NNLAD also print the solver's own
success flag and message, so a version bump that changes the picked
algorithm is impossible to miss -- no code here ever changes between runs.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy
import scipy
from scipy.optimize import linprog, lsq_linear

from analyze_regression import load_data


def lad_design(design, target, nonnegative_slopes=False):
    observation_count = len(target)
    objective = numpy.r_[numpy.zeros(4), numpy.ones(observation_count)]
    inequality_matrix = numpy.vstack(
        [
            numpy.hstack([design, -numpy.eye(observation_count)]),
            numpy.hstack([-design, -numpy.eye(observation_count)]),
        ]
    )
    inequality_rhs = numpy.r_[target, -target]
    coefficient_bounds = [(None, None)] + (
        [(0, None)] * 3 if nonnegative_slopes else [(None, None)] * 3
    )
    # No method= here -- this is the whole point of the script. The real
    # analyze_regression.py pins method="highs" explicitly and does not
    # have this problem.
    result = linprog(
        objective,
        A_ub=inequality_matrix,
        b_ub=inequality_rhs,
        bounds=coefficient_bounds + [(0, None)] * observation_count,
    )
    print(f"    solver success={result.success} status={result.status} : {result.message}")
    return result.x[:4]


def fit_models(design, target):
    return {
        "LS": numpy.linalg.lstsq(design, target, rcond=None)[0],
        "LAD": lad_design(design, target),
        "NNLS": lsq_linear(design, target, bounds=([-numpy.inf, 0, 0, 0], numpy.inf)).x,
        "NNLAD": lad_design(design, target, nonnegative_slopes=True),
    }


def main():
    print(f"numpy   {numpy.__version__}")
    print(f"scipy   {scipy.__version__}")

    training_design, training_target = load_data(ROOT / "data" / "training.csv")
    testing_design, testing_target = load_data(ROOT / "data" / "testing.csv")
    coefficients = fit_models(training_design, training_target)

    for method, beta in coefficients.items():
        residual = testing_target - testing_design @ beta
        rmse = float(numpy.sqrt(numpy.mean(residual**2)))
        print(f"  {method:<5} RMSE = {rmse!r}  [{rmse.hex()}]")


if __name__ == "__main__":
    main()
