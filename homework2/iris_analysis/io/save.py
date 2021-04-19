import csv
from typing import Dict, Tuple


def save_results(path: str, data: Dict[str, Tuple[float, float, float]]) -> None:
    with open(path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["", "mean", "median", "std"])
        for col, values in data.items():
            csv_writer.writerow([col, *values])


if __name__ == "__main__":
    save_results(
        "./results.csv",
        {
            'sepal.length': (1., 2., 3.,),
            'sepal.width': (4., 5., 6.,),
            'petal.length': (7., 8., 9.,),
            'petal.width': (10., 11., 12.,)
        }
    )
