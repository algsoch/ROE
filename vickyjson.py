import json
import numpy as np
import math

# Load the JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Extract columns A and B
A = [item['A'] for item in data]
B = [item['B'] for item in data]

# Manually calculate Pearson correlation
def pearson_correlation(x, y):
    n = len(x)
    
    # Calculate means
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    # Calculate covariance and standard deviations
    covariance = 0
    sum_squared_x = 0
    sum_squared_y = 0
    
    for i in range(n):
        x_dev = x[i] - mean_x
        y_dev = y[i] - mean_y
        covariance += x_dev * y_dev
        sum_squared_x += x_dev ** 2
        sum_squared_y += y_dev ** 2
    
    # Calculate correlation coefficient
    std_x = math.sqrt(sum_squared_x)
    std_y = math.sqrt(sum_squared_y)
    
    if std_x == 0 or std_y == 0:
        return 0
    
    return covariance / (std_x * std_y)

# Calculate using manual method
correlation_manual = pearson_correlation(A, B)
correlation_rounded_manual = round(correlation_manual, 3)

# Also calculate using numpy for comparison
correlation_numpy = np.corrcoef(A, B)[0, 1]
correlation_rounded_numpy = round(correlation_numpy, 3)

print(f"Manual calculation: {correlation_rounded_manual}")
print(f"NumPy calculation: {correlation_rounded_numpy}")