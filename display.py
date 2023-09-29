import os
import matplotlib.pyplot as plt
import numpy as np

# Function to read data from a text file
def read_data(file_path):
    with open(file_path, 'r') as file:
        max_val = float('-inf')
        min_val = float('inf')
        data = [float(line.strip()) for line in file]
        for i in data:
            if i > max_val:
                max_val = i
            if i < min_val:
                min_val = i
    return data, max_val, min_val

data_dir = '/Users/levineuwirth/Desktop/Cdev/agate/it/'
# List to store the results

for filename in os.listdir(data_dir):
    if filename.endswith('.txt')and not(filename.startswith('primes')):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                        # Step 2: Count the occurrences of each number
            number_counts = {}            
            for line in lines:
                try:
                    number = float(line.strip())  # Convert the line to a number
                    if number in number_counts:
                        number_counts[number] += 1
                    else:
                        number_counts[number] = 1
                except ValueError:
                    pass  # Ignore non-numeric lines
            numbers = list(number_counts.keys())
            counts = list(number_counts.values())
            plt.bar(numbers, counts)
            plt.xlabel('Numbers')
            plt.ylabel('Counts')
            plt.title('Number Occurrences in Text File')
            plt.show()
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            exit()

            # Split the text into words
            words = text.split()
