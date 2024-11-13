import csv
import math

def read_csv(file_path):
    points = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            points.append((float(row[0]), float(row[1])))
    return points

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def compute_interpoint_distance_matrix(points):
    n = len(points)
    distance_matrix = [[''] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            distance_matrix[i][j] = f"{euclidean_distance(points[i], points[j]):.2f}"
    return distance_matrix

def compute_centroid(points):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    centroid = (sum(x_coords) / len(points), sum(y_coords) / len(points))
    return centroid

def write_csv(file_path, distance_matrix):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Distance Matrix'])
        for row in distance_matrix:
            writer.writerow(row)

def main():
    input_file = 'circles.csv'
    output_file = 'distanceMat.csv'
    
    points = read_csv(input_file)
    distance_matrix = compute_interpoint_distance_matrix(points)
    centroid = compute_centroid(points)
    print(f'Centroid: {centroid}\n')
    
    print('Distance Matrix:')
    for row in distance_matrix:
        print(' '.join(row))
    
    
    write_csv(output_file, distance_matrix)

if __name__ == '__main__':
    main()
