import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('sample_employee_data.csv')
# Sample value counts (assuming a DataFrame `df` exists)
dept_counts = df['Department'].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(dept_counts.index, dept_counts.values, color='orange')

# ✅ Set Y-axis ticks based on actual max count
max_count = dept_counts.max()
print(max_count)

# Set custom Y-axis ticks — example: every 5 steps
plt.yticks(np.arange(0, max_count+5, 5))  # You can change 5 to 1, 10, etc.

plt.xlabel("Department")
plt.ylabel("Count")  # This is just the label, not the values
plt.title("Department Frequency")

# Show actual value on top of each bar
for i, value in enumerate(dept_counts.values):
    plt.text(i, value + 1, str(value), ha='center')

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
