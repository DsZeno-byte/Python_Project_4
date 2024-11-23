import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'businessCSV.xlsx'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Info:")
print(data.info())

# Select a numeric column for analysis
column_name = 'your_column_name'  # Replace with your numeric column name
if column_name not in data.columns:
    print(f"Column '{column_name}' not found in dataset.")
else:
    # Calculate mean, median, and mode
    column_data = data[column_name].dropna()
    mean_value = np.mean(column_data)
    median_value = np.median(column_data)
    mode_value = column_data.mode().iloc[0]  # Using `.iloc[0]` to get the first mode

    # Print the results
    print(f"\nAnalysis for column '{column_name}':")
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Mode: {mode_value}")

    # Visualization
    plt.figure(figsize=(10, 5))
    plt.hist(column_data, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=1.5, label=f'Mean: {mean_value:.2f}')
    plt.axvline(median_value, color='green', linestyle='dashed', linewidth=1.5, label=f'Median: {median_value:.2f}')
    plt.axvline(mode_value, color='blue', linestyle='dashed', linewidth=1.5, label=f'Mode: {mode_value:.2f}')
    plt.title(f'Distribution of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
