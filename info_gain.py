
import csv
import math

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        attributes = []
        labels = []
        for row in csv_reader:
            attributes.append(row[:-1])  
            labels.append(row[-1]) 
    return attributes, labels
def calculate_info(labels):
    yes_count = labels.count('yes')
    no_count = labels.count('no')
    total_count = len(labels)
    if yes_count == 0 or no_count == 0:
        return 0
    p_yes = yes_count / total_count
    p_no = no_count / total_count
    entropy = 0
    if p_yes > 0:
        entropy -= p_yes * math.log2(p_yes)
    if p_no > 0:
        entropy -= p_no * math.log2(p_no)
    return entropy
def info_gain(attribute_values, labels):
    total_entropy = calculate_info(labels)
    total_length = len(labels)
    
    unique_values = set(attribute_values)
    weighted_entropy = 0
    
    for value in unique_values:
        subset_labels = [labels[i] for i in range(total_length) if attribute_values[i] == value]
        subset_entropy = calculate_info(subset_labels)
        weighted_entropy += (len(subset_labels) / total_length) * subset_entropy
    
    return total_entropy - weighted_entropy
def outp(file_path):
    attributes, labels = read_csv(file_path)
    outlook_values = [row[1] for row in attributes]
    temperature_values = [row[2] for row in attributes]
    humidity_values = [row[3] for row in attributes]
    wind_values = [row[4] for row in attributes]
    gain_outlook = info_gain(outlook_values, labels)
    gain_temperature = info_gain(temperature_values, labels)
    gain_humidity = info_gain(humidity_values, labels)
    gain_wind = info_gain(wind_values, labels)
    print(f"Information Gain for Outlook: {gain_outlook:.4f}")
    print(f"Information Gain for Temperature: {gain_temperature:.4f}")
    print(f"Information Gain for Humidity: {gain_humidity:.4f}")
    print(f"Information Gain for Wind: {gain_wind:.4f}")
file_path = r"C:\Users\bhilw\OneDrive\Documents\DM\4_info_gain\data.csv"
outp(file_path)
