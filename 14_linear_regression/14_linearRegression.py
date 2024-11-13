import csv

def load_dataset(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        dataset = list(reader)
        return header, [[float(x) for x in row] for row in dataset]

def linear_regression_coefficients(X, y):
    n = len(X)
    x_mean = sum(X) / n
    y_mean = sum(y) / n
    numerator = sum((X[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator = sum((X[i] - x_mean) ** 2 for i in range(n))
    m = numerator / denominator
    c = y_mean - m * x_mean
    return c, m

def main():
    filename = 'real_estate.csv'
    header, dataset = load_dataset(filename)
    X = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    c, m = linear_regression_coefficients(X, y)
    print(f"Attributes used:\nX: {header[0]}\nY: {header[1]}")
    print(f"Linear Regression Coefficients:\nIntercept (c): {c:0.3f}\nSlope (m): {m:0.3f}")
    print(f"\nThe equation of the line is: Y = {m:0.3f}X + {c:0.3f}\n")

if __name__ == "__main__":
    main()
