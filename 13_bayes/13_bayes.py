import csv

def load_dataset(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        dataset = list(reader)
    return dataset[1:]  


def separate_features_labels(dataset):
    features = []
    labels = []
    for row in dataset:
        features.append([float(value) for value in row[:-1]]) 
        labels.append(row[-1])  
    return features, labels


def calculate_prior(labels):
    total_count = len(labels)
    label_count = {}
    for label in labels:
        if label not in label_count:
            label_count[label] = 0
        label_count[label] += 1
    prior = {label: count / total_count for label, count in label_count.items()}
    return prior


def calculate_conditional_probabilities(features, labels):
    conditional_probabilities = {}
    label_count = {}
    
    for i in range(len(features)):
        label = labels[i]
        if label not in conditional_probabilities:
            conditional_probabilities[label] = {}
            label_count[label] = 0
        label_count[label] += 1
        
        for j in range(len(features[i])):
            if j not in conditional_probabilities[label]:
                conditional_probabilities[label][j] = []
            conditional_probabilities[label][j].append(features[i][j])
    
    for label in conditional_probabilities:
        for j in conditional_probabilities[label]:
            mean = sum(conditional_probabilities[label][j]) / label_count[label]
            variance = sum((x - mean) ** 2 for x in conditional_probabilities[label][j]) / label_count[label]
            conditional_probabilities[label][j] = (mean, variance)
    
    return conditional_probabilities


def calculate_class_probability(sample, prior, conditional_probabilities):
    total_prob = {}
    
    for label in prior:
        prob = prior[label]
        for j in range(len(sample)):
            mean, variance = conditional_probabilities[label][j]
            
            prob *= (1 / ((2 * 3.14159 * variance) ** 0.5)) * \
                     (2.71828 ** (-((sample[j] - mean) ** 2) / (2 * variance)))
        total_prob[label] = prob
    
    return total_prob


def predict(sample, prior, conditional_probabilities):
    probabilities = calculate_class_probability(sample, prior, conditional_probabilities)
    return max(probabilities, key=probabilities.get)

def main():
    filename = 'iris.csv'  
    dataset = load_dataset(filename)
    features, labels = separate_features_labels(dataset)
    
    prior = calculate_prior(labels)
    conditional_probabilities = calculate_conditional_probabilities(features, labels)
    print("Completed computing prior and conditional probabilities.\n")

    print("Enter sample features for Iris dataset (sepal length, sepal width, petal length, petal width) separated by commas:")
    random_sample = [float(x) for x in input().split(',')]
    predicted_class = predict(random_sample, prior, conditional_probabilities)

    print("Sample features:", random_sample)
    print("Predicted class:", predicted_class)
    probabilities = calculate_class_probability(random_sample, prior, conditional_probabilities)
    print("Class probabilities:")
    for label, probability in probabilities.items():
        formatted_probability = "{:.2e}".format(probability).replace('e', ' * 10^')
        print(f"Class {label}: {formatted_probability}")

if __name__ == "__main__":
    main()
