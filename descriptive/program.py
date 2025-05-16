import numpy as np
import pandas as pd
# from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data (house prices in $1000s)
data = [10,15,23,31,40,50,60,70,80,90]  # 800 is an outlier

# Convert to NumPy array
arr = np.array(data)

# Mean
mean = np.mean(arr)
print(f"Mean: {mean}")

# Median
median = np.median(arr)
print(f"Median: {median}")

# Mode
# mode = stats.mode(arr, keepdims=True)
# print(f"Mode: {mode.mode[0]} (appears {mode.count[0]} times)")

# Range
range_val = np.max(arr) - np.min(arr)
print(f"Range: {range_val}")

# Variance
variance = np.var(arr)
print(f"Variance: {variance}")

# Standard Deviation
std_dev = np.std(arr)
print(f"Standard Deviation: {std_dev}")

# Quartiles and IQR
q1 = np.percentile(arr, 25)
q3 = np.percentile(arr, 75)
iqr = q3 - q1
print(f"Q1: {q1}, Q3: {q3}, IQR: {iqr}")

# Skewness
# skewness = stats.skew(arr)
# print(f"Skewness: {skewness}")

# Kurtosis
# kurt = stats.kurtosis(arr)
# print(f"Kurtosis: {kurt}")

# Frequency Distribution using pandas
df = pd.DataFrame({'prices': arr})
freq_table = df['prices'].value_counts().sort_index()
print("\nFrequency Distribution:\n", freq_table)

# Visualization: Histogram and Boxplot
plt.figure(figsize=(12, 5))

# Histogram
plt.subplot(1, 2, 1)
sns.histplot(arr, kde=True, bins=10, color='skyblue')
plt.title('Histogram of House Prices')

# Boxplot
plt.subplot(1, 2, 2)
sns.boxplot(x=arr, color='orange')
plt.title('Boxplot with IQR and Outlier')

plt.tight_layout()
plt.show()
