# Titanic Dataset EDA

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style='whitegrid')

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# --- Basic Info ---
print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Data Types and Null Counts ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe(include='all'))

# --- Missing Values ---
print("\n--- Missing Values Count ---")
print(df.isnull().sum())

# Visualize missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# --- Distribution of Numerical Features ---
numeric_cols = df.select_dtypes(include=np.number).columns

df[numeric_cols].hist(figsize=(14, 10), bins=20, edgecolor='black')
plt.suptitle("Histograms of Numerical Features")
plt.show()

# --- Box Plots for Outlier Detection ---
plt.figure(figsize=(14, 8))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(2, 4, i)
    sns.boxplot(x=df[col], color='skyblue')
    plt.title(f'Boxplot of {col}')
plt.tight_layout()
plt.show()

# --- Categorical Feature Distributions ---
categorical_cols = df.select_dtypes(include='object').columns

plt.figure(figsize=(14, 10))
for i, col in enumerate(categorical_cols, 1):
    plt.subplot(3, 3, i)
    sns.countplot(x=col, data=df, palette='Set2')
    plt.xticks(rotation=45)
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()

# --- Correlation Matrix ---
plt.figure(figsize=(10, 8))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# --- Relationships Between Variables ---
# Survival by Sex
sns.countplot(x='Survived', hue='Sex', data=df, palette='coolwarm')
plt.title("Survival Count by Sex")
plt.show()

# Survival by Pclass
sns.countplot(x='Survived', hue='Pclass', data=df, palette='Set1')
plt.title("Survival Count by Passenger Class")
plt.show()

# Age distribution by Survival
plt.figure(figsize=(10, 6))
sns.kdeplot(df[df['Survived'] == 1]['Age'], label='Survived', shade=True)
sns.kdeplot(df[df['Survived'] == 0]['Age'], label='Did Not Survive', shade=True)
plt.title("Age Distribution by Survival")
plt.xlabel("Age")
plt.legend()
plt.show()

# Fare distribution by Pclass
plt.figure(figsize=(10, 6))
sns.boxplot(x='Pclass', y='Fare', data=df, palette='Pastel1')
plt.title("Fare Distribution by Class")
plt.show()

# --- Feature Engineering Ideas ---
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
sns.countplot(x='FamilySize', hue='Survived', data=df)
plt.title("Survival by Family Size")
plt.show()

# Summary:
# - 'Cabin' has too many missing values.
# - Strong survival correlation with 'Sex', 'Pclass'.
# - Outliers are present in 'Fare'.
# - Age and Fare are right-skewed.
# - Larger families had lower survival rate.

# End of EDA
