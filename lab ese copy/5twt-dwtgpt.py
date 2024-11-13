import csv

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def calculate_weights(data):
    headers = list(data[0].keys())
    numeric_headers = [header for header in headers if header != 'Region']

    # Calculate totals for each numeric header
    totals = {header: sum(int(row[header]) for row in data) for header in numeric_headers}

    total_dwt = {header: 0 for header in numeric_headers}
    total_twt = {header: 0 for header in numeric_headers}

    # Process each row and calculate d-wt and t-wt
    for row in data:
        region = row['Region']
        total = sum(int(row[header]) for header in numeric_headers)

        dwt = {header: (int(row[header]) / totals[header]) * 100 if totals[header] > 0 else 0 for header in numeric_headers}
        twt = {header: (int(row[header]) / total) * 100 if total > 0 else 0 for header in numeric_headers}

        for header in numeric_headers:
            total_dwt[header] += dwt[header]
            total_twt[header] += twt[header]

        # Print row details
        print(region, [row[header] for header in numeric_headers], list(dwt.values()), list(twt.values()), total)

    # Calculate overall t-wt
    overall_twt = {header: totals[header] / sum(totals.values()) * 100 for header in numeric_headers}
    final_total = sum(totals.values())

    # Print totals
    print("Totals:", list(totals.values()))
    print("Total d-wt:", list(total_dwt.values()))
    print("Overall t-wt:", list(overall_twt.values()))
    print("Final total:", final_total)

filename = 'sales_data.csv'
data = read_csv(filename)
calculate_weights(data)
