import os
from typing import List


def computation_sum(main_path: str) -> int:
    sum_of_computation: int = 0
    for folder in os.listdir(f"{main_path}/"):
        if os.path.isdir(f"{main_path}/{folder}"):
            for sub_folder in os.listdir(f"{main_path}/{folder}"):
                if os.path.isdir(f"{main_path}/{folder}/{sub_folder}"):
                    path: str = os.path.join(f"{main_path}/{folder}/{sub_folder}", "Solutions.csv")
                    with open(path, "r") as f:
                        stats: List[str] = f.read().splitlines()[-1].split(" ; ")
                        model: str = stats[0]
                        if model == "A":
                            computation_time: int = int(stats[-1].split("s;")[0])
                            sum_of_computation += computation_time
    return sum_of_computation


if __name__ == "__main__":
    print(computation_sum("./"))
