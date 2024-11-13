import csv

def read_distance_matrix(filename):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        labels = next(reader)
        matrix = []
        for row in reader:
            matrix.append([float(value) if value else 0 for value in row[1:]])
    return labels[1:], matrix

def single_linkage(matrix, cluster1, cluster2):
    return min(matrix[cluster1][cluster2], matrix[cluster2][cluster1])

def agglomerative_clustering(matrix, labels):
    clusters = [[label] for label in labels]
    while len(clusters) > 1:
        min_distance = float('inf')
        to_merge = None

        # Find the closest pair of clusters
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                dist = single_linkage(matrix, i, j)
                if dist < min_distance:
                    min_distance = dist
                    to_merge = (i, j)

        # Merge the closest clusters
        i, j = to_merge
        clusters[i] += clusters[j]
        del clusters[j]

        # Update the distance matrix
        for k in range(len(matrix)):
            if k != i and k != j:
                matrix[i][k] = min(matrix[i][k], matrix[j][k])
                matrix[k][i] = matrix[i][k]

        matrix = [row[:j] + row[j+1:] for row in matrix]
        matrix.pop(j)

    return clusters

if __name__ == "__main__":
    labels, matrix = read_distance_matrix('mat.csv')
    result = agglomerative_clustering(matrix, labels)
    print("Final Clusters:", result)
