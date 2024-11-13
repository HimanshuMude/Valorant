import csv

def gini_index(y):
    counts = {}
    for label in y:
        counts[label] = counts.get(label, 0) + 1
    total = len(y)
    gini = 1.0
    for count in counts.values():
        prob = count / total
        gini -= prob ** 2
    return gini

def gini_for_feature(X, y, feature_index):
    splits = {}
    for i in range(len(X)):
        value = X[i][feature_index]
        if value not in splits:
            splits[value] = []
        splits[value].append(y[i])
    weighted_gini = 0.0
    for subset in splits.values():
        prob = len(subset) / len(y)
        weighted_gini += prob * gini_index(subset)
    return weighted_gini

def read_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)
    X = [row[:-1] for row in data]
    y = [row[-1] for row in data]
    return X, y, header

if __name__ == "__main__":
    X, y, header = read_data('datasheet.csv')
    best_gini = float('inf')
    best_feature = None

    for i in range(len(X[0])):
        gini = gini_for_feature(X, y, i)
        print(f"Gini Index for '{header[i]}': {gini:.4f}")
        if gini < best_gini:
            best_gini = gini
            best_feature = header[i]

    print(f"Best feature to split: {best_feature} with Gini Index: {best_gini:.4f}")
