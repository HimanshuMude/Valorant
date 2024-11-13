import csv

def calculate_quartiles(data):
    data.sort()
    n = len(data)
    
    def get_quartile_position(n, frac):
        pos = (n-1) * frac
        if pos.is_integer():
            return data[int(pos)]
        else:
            l = int(pos)
            h = l + 1
            return (data[l] + data[h]) / 2

    Q1 = get_quartile_position(n, 0.25)
    Q3 = get_quartile_position(n, 0.75)
    
    return Q1, Q3

def calculate_median(data):
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]

def five_number_summary(data):
    sorted_data = sorted(data)
    median = calculate_median(sorted_data)
    Q1, Q3 = calculate_quartiles(sorted_data)
    min_val = min(sorted_data)
    max_val = max(sorted_data)
    print("\nFive number summary\n")
    print(f"Min: {min_val:.2f}\nQ1: {Q1:.2f}\nMedian: {median:.2f}\nQ3: {Q3:.2f}\nMax: {max_val:.2f}\nIQR: {Q3-Q1 :.2f}\n")


def main():
    filename = 'financial_risk_analysis.csv'
    columns_data = {}

    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        print("Available columns:")
        for i, header in enumerate(headers):
            print(f"{i + 1}. {header}")
        
        column_index = int(input("Enter the number of the column to analyze or 0 to analyze all columns: ")) - 1

    if column_index == -1:
        column_name = 'all'
    else:
        column_name = headers[column_index]
    filename = 'financial_risk_analysis.csv'
    columns_data = {}

    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for column in row:
                if column not in columns_data:
                    columns_data[column] = []
                columns_data[column].append(float(row[column]))

    if column_name == 'all':
        for column, data in columns_data.items():
            print(f"\nColumn: {column}")
            five_number_summary(data)
    else:
        if column_name in columns_data:
            five_number_summary(columns_data[column_name])
        else:
            print(f"Column '{column_name}' not found in the CSV file.")

    

if __name__ == "__main__":
    main()
