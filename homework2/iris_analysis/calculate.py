import statistics
from typing import List, Tuple


def calculate_statistics(data: List[float]) -> Tuple[float, float, float]:
    mean: float = statistics.mean(data)
    median: float = statistics.median(data)
    std: float = statistics.stdev(data)
    return mean, median, std
