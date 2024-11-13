import csv
import math

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames
        data = {col: [] for col in columns}
        for row in reader:
            for col in columns:
                data[col].append(float(row[col]))
    return data, columns

def mean(values):
    return sum(values) / len(values)

def pearson_correlation(x, y):
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    
    sum_xy = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    sum_xx = sum((x[i] - mean_x) ** 2 for i in range(n))
    sum_yy = sum((y[i] - mean_y) ** 2 for i in range(n))
    
    return sum_xy / math.sqrt(sum_xx * sum_yy)

if __name__ == "__main__":
    filename = 'correlation_data.csv'
    
    data, columns = read_csv(filename)
    
    
    col1 = columns[0]
    col2 = columns[1]
    
    x = data[col1]
    y = data[col2]
    
    correlation = pearson_correlation(x, y)
    print(f"Pearson correlation coefficient between {col1} and {col2}: {correlation:.4f}")