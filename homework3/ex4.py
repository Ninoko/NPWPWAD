import argparse
import numpy as np

COLS = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str)
    args = parser.parse_args()

    data = np.loadtxt(args.input, skiprows=1, delimiter=",", usecols=range(4))
    means = np.mean(data, axis=0)
    medians = np.median(data, axis=0)
    stds = np.std(data, axis=0)
    for col_id, col in enumerate(COLS):
        print(col)
        print(f"\tmean: {means[col_id]}")
        print(f"\tmedian: {medians[col_id]}")
        print(f"\tstd: {stds[col_id]}")
