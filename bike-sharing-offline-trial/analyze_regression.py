import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog, lsq_linear


ROOT = Path(__file__).parent
PREDICTORS = ["temp", "hum", "windspeed"]


def load_data(path):
    with path.open(newline="") as file:
        rows = list(csv.DictReader(file))
    features = np.array([[float(row[name]) for name in PREDICTORS] for row in rows])
    target = np.array([float(row["cnt"]) for row in rows])
    return np.column_stack([np.ones(len(features)), features]), target


def lad_design(design, target, nonnegative_slopes=False):
    observation_count = len(target)
    objective = np.r_[np.zeros(4), np.ones(observation_count)]
    inequality_matrix = np.vstack(
        [
            np.hstack([design, -np.eye(observation_count)]),
            np.hstack([-design, -np.eye(observation_count)]),
        ]
    )
    inequality_rhs = np.r_[target, -target]
    coefficient_bounds = [(None, None)] + (
        [(0, None)] * 3 if nonnegative_slopes else [(None, None)] * 3
    )
    result = linprog(
        objective,
        A_ub=inequality_matrix,
        b_ub=inequality_rhs,
        bounds=coefficient_bounds + [(0, None)] * observation_count,
        method="highs",
    )
    if not result.success:
        raise RuntimeError(f"LAD optimization failed: {result.message}")
    return result.x[:4]


def fit_models(design, target):
    return {
        "LS": np.linalg.lstsq(design, target, rcond=None)[0],
        "LAD": lad_design(design, target),
        "NNLS": lsq_linear(design, target, bounds=([-np.inf, 0, 0, 0], np.inf)).x,
        "NNLAD": lad_design(design, target, nonnegative_slopes=True),
    }


def main():
    training_design, training_target = load_data(ROOT / "data" / "training.csv")
    testing_design, testing_target = load_data(ROOT / "data" / "testing.csv")
    coefficients = fit_models(training_design, training_target)

    metrics = {}
    predictions = {}
    for method, beta in coefficients.items():
        prediction = testing_design @ beta
        residual = testing_target - prediction
        predictions[method] = prediction
        metrics[method] = {
            "MAE": float(np.mean(np.abs(residual))),
            "RMSE": float(np.sqrt(np.mean(residual**2))),
        }

    output_path = ROOT / "output" / "submission.csv"
    with output_path.open("w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["method", "b_0", "b_1_temp", "b_2_hum", "b_3_windspeed"])
        for method in ["LS", "LAD", "NNLS", "NNLAD"]:
            writer.writerow([method, *[f"{value:.12g}" for value in coefficients[method]]])

    figures_path = ROOT / "figures"
    figures_path.mkdir(exist_ok=True)
    figure, axes = plt.subplots(2, 2, figsize=(10, 8), sharex=True, sharey=True)
    limits = [testing_target.min(), testing_target.max()]
    for axis, method in zip(axes.flat, ["LS", "LAD", "NNLS", "NNLAD"]):
        axis.scatter(testing_target, predictions[method], alpha=0.72, color="#176b87", edgecolors="none")
        axis.plot(limits, limits, color="#d1495b", linewidth=1.5)
        axis.set_title(method)
        axis.set_xlabel("Actual rentals per day")
        axis.set_ylabel("Predicted rentals per day")
        axis.text(
            0.04,
            0.94,
            f"MAE {metrics[method]['MAE']:.1f}\nRMSE {metrics[method]['RMSE']:.1f}",
            transform=axis.transAxes,
            va="top",
            bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "none"},
        )
    figure.suptitle("Bike-sharing test predictions by regression method")
    figure.tight_layout()
    figure.savefig(figures_path / "actual-vs-predicted.png", dpi=180)
    plt.close(figure)

    results_path = ROOT / "analysis_results.json"
    results_path.write_text(
        json.dumps(
            {"coefficients": {name: values.tolist() for name, values in coefficients.items()}, "metrics": metrics},
            indent=2,
        )
    )


if __name__ == "__main__":
    main()