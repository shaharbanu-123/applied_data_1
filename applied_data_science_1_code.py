import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set(style="whitegrid")

# Load the dataset & display few rows 

df = pd.read_csv("cats_dataset.csv")
print(df.head())

#display summary statistics
print(df.describe())

# 1 . Age Distribution Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['Age (Years)'], bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution of Cats')
plt.xlabel('Age (Years)')
plt.ylabel('Frequency')
plt.show()

# 2. Correlation Heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(df[['Age (Years)', 'Weight (kg)']].corr(), annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Heatmap')
plt.show()

# 3. Scatter plot for Age vs. Weight
plt.figure(figsize=(8, 5))
plt.scatter(df['Age (Years)'],df['Weight (kg)'], alpha=1, color='cyan')
plt.title('Relationship between Age and Weight')
plt.xlabel('Age (Years)')
plt.ylabel('Weight (kg)')
plt.show()