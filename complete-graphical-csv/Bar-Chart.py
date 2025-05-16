import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the CSV file properly
df = pd.read_csv('sample_employee_data.csv')

# Step 4: bar chart - Salary Distribution
plt.figure(figsize=(7, 5))
dept_counts = df['Department'].value_counts()
print(dept_counts.index) # department name
print(dept_counts.values) 
plt.bar(dept_counts.index, dept_counts.values, color='orange')

# max_count = dept_counts.max()
# plt.yticks(np.arange(0, max_count + 1, 1))

plt.title("Bar Chart: Department Frequency")
plt.xlabel("Department")
plt.ylabel("Count")
plt.grid(axis='y')
plt.show()