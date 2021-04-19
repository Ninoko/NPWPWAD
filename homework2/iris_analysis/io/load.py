import csv
from typing import Any, Dict, List


def load_iris(path: str) -> List[Dict[str, Any]]:
    data: List[Dict[str, Any]] = []
    with open(path, "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        columns = next(csv_reader)
        for row in csv_reader:
            row_data = dict()
            for col_id, col in enumerate(columns):
                if col != "variety":
                    row_data[col] = float(row[col_id])
                else:
                    row_data[col] = row[col_id]
            data.append(row_data)
    return data


if __name__ == "__main__":
    df = load_iris("/home/neyo/Pobrane/iris.csv")
    print(df)
