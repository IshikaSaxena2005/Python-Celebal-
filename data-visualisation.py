pip install pandas matplotlib seaborn
# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset (You can also load from Kaggle or CSV)
titanic = sns.load_dataset('titanic')  # Automatically loads from seaborn

# Show first few rows
print("First 5 rows of the dataset:")
print(titanic.head())

# Check for null values
print("\nMissing values:")
print(titanic.isnull().sum())

# Drop columns with too many missing values or irrelevant ones
titanic.drop(columns=['deck', 'embark_town', 'alive'], inplace=True)

# Fill missing age with median
titanic['age'].fillna(titanic['age'].median(), inplace=True)
titanic['embarked'].fillna(titanic['embarked'].mode()[0], inplace=True)

# --- Univariate Analysis ---
# Plot the distribution of Age
plt.figure(figsize=(8, 4))
sns.histplot(titanic['age'], kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Count of survivors
plt.figure(figsize=(6, 4))
sns.countplot(x='survived', data=titanic, palette='Set2')
plt.title('Survival Count (0 = Not Survived, 1 = Survived)')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()

# --- Bivariate Analysis ---
# Survival by Sex
plt.figure(figsize=(6, 4))
sns.countplot(x='sex', hue='survived', data=titanic, palette='pastel')
plt.title('Survival Count by Gender')
plt.show()

# Age vs Survival
plt.figure(figsize=(8, 4))
sns.boxplot(x='survived', y='age', data=titanic, palette='Set3')
plt.title('Age Distribution by Survival')
plt.show()

# Class vs Survival
plt.figure(figsize=(6, 4))
sns.countplot(x='class', hue='survived', data=titanic, palette='coolwarm')
plt.title('Survival Count by Passenger Class')
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(titanic.corr(numeric_only=True), annot=True, cmap='Blues', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
