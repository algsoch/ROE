import pandas as pd

# Read the CSV file
df = pd.read_csv('groupmark.csv')

# Convert columns to numeric to ensure proper comparison
for col in ['Group', 'Maths', 'Physics', 'English', 'Economics', 'Biology']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Filter students who scored 67 or more in English and are in groups 60-96
filtered_df = df[(df['English'] >= 67) & (df['Group'] >= 60) & (df['Group'] <= 96)]

# Calculate the sum of Maths marks for these students
total_maths = filtered_df['Maths'].sum()

print(f"Total Maths marks: {total_maths}")
print(f"Number of students meeting criteria: {len(filtered_df)}")
print("\nSample of filtered students:")
print(filtered_df[['Group', 'Maths', 'English']].head(10))