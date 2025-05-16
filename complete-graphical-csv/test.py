import pandas as pd
import numpy as np

# Create a sample dataset with 500 rows for data analysis and ML
np.random.seed(42)

# Example features for an AI/ML-friendly dataset
df = pd.DataFrame({
    'Age': np.random.randint(18, 65, 500),
    'Salary': np.random.normal(50000, 12000, 500).astype(int),
    'Experience': np.random.randint(0, 40, 500),
    'Education_Level': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 500),
    'Department': np.random.choice(['IT', 'HR', 'Marketing', 'Sales', 'Finance'], 500),
    'Performance_Score': np.round(np.random.uniform(1, 5, 500), 2),
    'Left_Company': np.random.choice([0, 1], 500, p=[0.8, 0.2])
})

# Save to CSV
csv_path = "sample_employee_data2.csv"
df.to_csv(csv_path, index=False)

csv_path
