import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file properly
df = pd.read_csv('sample_employee_data.csv')

# Step 3: Descriptive Statistics
# print("\n🔹 Descriptive Statistics:\n", df.describe())

# //////// answer above line ///////////
#                Age        Salary  Experience  Performance_Score  Left_Company
# count  500.000000    500.000000  500.000000         500.000000    500.000000
# mean    41.278000  49903.230000   19.822000           3.039420      0.192000
# std     13.389072  11852.036139   11.367355           1.145409      0.394268
# min     18.000000  17637.000000    0.000000           1.010000      0.000000
# 25%     30.000000  41592.500000   10.000000           2.120000      0.000000
# 50%     42.000000  49774.000000   19.000000           3.050000      0.000000
# 75%     52.000000  57563.250000   30.000000           4.035000      0.000000
# max     64.000000  86946.000000   39.000000           4.990000      1.000000

# Step 4: Histogram - Salary Distribution
plt.figure(figsize=(10, 5))
plt.hist(df['Salary'], bins=20, color='black', edgecolor='black')
plt.title("Histogram: Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()