import csv

def read_csv(input_file):
    with open(input_file, mode='r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    return rows

def write_csv(output_file, fieldnames, rows):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        
def min_max_normalization(value, min_val, max_val, new_min, new_max):
    return (((value - min_val) * (new_max - new_min)) / (max_val - min_val)) + new_min

def z_score_normalization(value, mean_val, std_dev):
    return (value - mean_val) / std_dev


def calculate_mean_and_std_dev(values):
    n = len(values)
    mean_val = sum(values) / n
    variance = sum((x - mean_val) ** 2 for x in values) / n
    std_dev = variance ** 0.5
    return mean_val, std_dev

input_file = 'AirQualityUCI.csv'
rows = read_csv(input_file)

attributes = rows[0].keys()
numeric_attributes = [attr for attr in attributes if attr != 'Date' and attr != 'Time']

print("Choose normalization method:")
print("1. Min-Max Normalization")
print("2. Z-Score Normalization")
choice = input("Enter choice --> either 1 or 2: ")

if choice == '1':
    print("Available attributes for normalization:")
    for i, attr in enumerate(numeric_attributes, start=1):
        print(f"{i}. {attr}")

    attr_choice = int(input("Select attribute to normalize (enter number): ")) - 1
    selected_attribute = numeric_attributes[attr_choice]

    values = [float(row[selected_attribute]) for row in rows]

    new_min = float(input("Enter new Min: "))
    new_max = float(input("Enter new Max: "))
    for row in rows:
        value = float(row[selected_attribute])
        row[selected_attribute] = min_max_normalization(value, min(values), max(values), new_min, new_max)
    output_file = f'{selected_attribute}_min_max.csv'
    print("Min-Max normalization selected.")
elif choice == '2':
    for attr in numeric_attributes:
        values = [float(row[attr]) for row in rows]
        mean_val, std_dev = calculate_mean_and_std_dev(values)
        for row in rows:
            row[attr] = z_score_normalization(float(row[attr]), mean_val, std_dev)
    output_file = 'all_columns_z_score.csv'
    print("Z-Score normalization selected.")
else:
    print("Invalid choice.")
    output_file = None

if output_file:
    fieldnames = rows[0].keys()
    write_csv(output_file, fieldnames, rows)
    print(f"Normalization complete. Data saved to {output_file}")



# import csv

# def read_csv(filename):
#     with open(filename,mode='r') as file:
#         reader=csv.DictReader(file)
#         rows=list(reader)
#     return rows

# def write_csv(output_file,fieldnames,rows):
#     with open(output_file,mode='w',newline='') as file:
#         writer=csv.DictWriter(file,fieldnames)
#         writer.writeheader()
#         writer.writerows(rows)

# def minmax(val,minm,maxm,newMin,newMax):
#     return (((val-minm)/(maxm-minm))*(newMax-newMin))+newMin
        

# filename='AirQualityUCI.csv'

# rows=read_csv(filename)

# print("Select type of Normalization ")
# print("1. Minmax")
# print("2. Z Score")
# choice=int(input("Enter the normalization type: "))

# headers=rows[0].keys()
# if choice ==1:
#     for idx,val in enumerate(headers):
#         print(idx,val)

#     col=int(input('Enter the column to normalize'))

#     column=[val for idx,val in enumerate(headers) if idx==col][0]

#     values=[float(row[column]) for row in rows]
#     minm=min(values)
#     maxm=max(values)

#     newMin=float(input("Enter new minima "))
#     newMax=float(input("Enter new maxm "))

#     for row in rows:
#         row[column]=minmax(float(row[column]),minm,maxm,newMin,newMax)

#     output_file='MinMaxOutput.csv'

#     write_csv(output_file,headers,rows)

# elif choice==2:
#     for _,column in enumerate(headers):
#         values=[float(row[column]) for row in rows]
#         mean=sum(values)/len(values)
#         stddev=(sum((x-mean)**2 for x in values)/len(values))**0.5
#         for row in rows:
#             row[column]=(float(row[column])-mean)/stddev
    
#     output_file="ZScore.csv"
#     write_csv(output_file,headers,rows)


