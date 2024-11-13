def read_csv(filename):
    with open(filename, 'r') as file:
        headers = file.readline().strip().split(',')
        data = []
        for line in file:
            values = line.strip().split(',')
            row = {headers[i]: values[i] for i in range(len(headers))}
            data.append(row)
    return data

def calculate_and_display_weights(data):
    headers = data[0].keys()
    numeric_headers = [header for header in headers if header != 'Region']

    totals = {header: sum(int(row[header]) for row in data) for header in numeric_headers}

    print(f"\n{'Region':<10} " + " ".join([f"{header:<10} d-wt {header:<10} t-wt {header:<10} " for header in numeric_headers])+"Total")
    print("-" * (10 + len(numeric_headers) * 60))

    total_dwt = {header: 0 for header in numeric_headers}
    total_twt = {header: 0 for header in numeric_headers}

    for row in data:
        region = row['Region']
        total = sum(int(row[header]) for header in numeric_headers)

        dwt = {header: (int(row[header]) / totals[header]) * 100 if totals[header] > 0 else 0 for header in numeric_headers}
        twt = {header: (int(row[header]) / total) * 100 if total > 0 else 0 for header in numeric_headers}

        for header in numeric_headers:
            total_dwt[header] += dwt[header]
            total_twt[header] += twt[header]

        print(f"{region:<14} " + " ".join([f"{row[header]:<14}{dwt[header]:<14.2f}{twt[header]:<14.2f}" for header in numeric_headers]) + f" {total:<10}")

    overall_twt = {header: totals[header] / sum(totals.values()) * 100 for header in numeric_headers}
    final_total = sum(totals.values())

    print("-" * (10 + len(numeric_headers) * 60))
    print(f"{'Total':<13} " + " ".join([f"{totals[header]:<13} {total_dwt[header]:<13.2f} {overall_twt[header]:<13.2f}" for header in numeric_headers]) + f" {final_total:<10}\n")

filename = 'sales_data.csv'
data = read_csv(filename)
calculate_and_display_weights(data)
