import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example DataFrame
df = pd.DataFrame({
    'Age': [25, 30, 22, 35, 28, 40, 45, 23, 36, 31],
    'Score': [80, 90, 70, 85, 75, 95, 88, 60, 92, 78],
    'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'C', 'A', 'B', 'A'],
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D')
})

plt.figure(figsize=(6,4))
sns.histplot(df['Age'], kde=True, bins=5)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
