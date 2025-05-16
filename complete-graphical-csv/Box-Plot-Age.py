import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file properly
df = pd.read_csv('sample_employee_data.csv')

print("\n🔹 Descriptive Statistics:\n", df.describe())

# Step 4: box plot - Salary Distribution
plt.figure(figsize=(6, 4))
plt.boxplot(df['Age'])
plt.title("Box Plot: Age")
plt.ylabel("Age")
plt.grid(True)
plt.show()