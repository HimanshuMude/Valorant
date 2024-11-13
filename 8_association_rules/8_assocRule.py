import csv

def load_frequent_itemsets(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        frequent_itemsets = {}
        for row in reader:
            itemset = frozenset(row[0].split(', '))
            support = float(row[1])
            frequent_itemsets[itemset] = support
    return frequent_itemsets

def generate_combinations(itemset, length):
    if length == 0:
        return [frozenset()]
    elif length == len(itemset):
        return [frozenset(itemset)]
    else:
        itemset = list(itemset)
        result = []
        for i in range(len(itemset)):
            for combo in generate_combinations(itemset[i+1:], length-1):
                result.append(frozenset([itemset[i]]) | combo)
        return result

def generate_association_rules(frequent_itemsets, min_confidence):
    rules = []
    for itemset in frequent_itemsets:
        if len(itemset) > 1:
            for i in range(1, len(itemset)):
                for antecedent in generate_combinations(itemset, i):
                    consequent = itemset - antecedent
                    if len(consequent) == 1: 
                        confidence = frequent_itemsets[itemset] / frequent_itemsets[antecedent]
                        if confidence >= min_confidence:
                            rules.append((antecedent, consequent, confidence))
    return rules

def write_rules(filename, rules):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Antecedent', 'Consequent', 'Confidence'])
        for antecedent, consequent, confidence in rules:
            writer.writerow([', '.join(antecedent), ', '.join(consequent), confidence])
    print(f"Association rules stored at {filename}")

def print_rules(rules):
    for antecedent, consequent, confidence in rules:
        print(f"Antecedent: {', '.join(antecedent)}, Consequent: {', '.join(consequent)}, Confidence: {confidence:.2f}")

if __name__ == "__main__":
    filename = 'frequent_itemsets.csv'
    min_confidence = float(input("Enter minimum confidence: "))

    frequent_itemsets = load_frequent_itemsets(filename)
    rules = generate_association_rules(frequent_itemsets, min_confidence)
    
    print("Generated Association Rules:")
    print_rules(rules)
    
    output_filename = 'association_rules.csv'
    write_rules(output_filename, rules)