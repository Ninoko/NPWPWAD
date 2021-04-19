import argparse

from iris_analysis import load_iris, calculate_statistics, save_results

COLS = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str)
    parser.add_argument("-o", "--output", type=str)
    args = parser.parse_args()

    data = load_iris(args.input)
    save_results(
        path=args.output,
        data={
            col: calculate_statistics(list(map(lambda row: row[col], data)))
            for col in COLS
        }
    )
