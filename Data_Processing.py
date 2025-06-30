# House Prices Dataset - Data Preprocessing & Feature Engineering

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Load training data
train = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/HousePricesTrain.csv")

# --- Overview ---
print("\n--- Initial Shape ---")
print(train.shape)
print("\n--- Missing Values ---")
print(train.isnull().sum()[train.isnull().sum() > 0])

# --- Drop columns with too many missing values ---
missing_threshold = 0.3
missing_ratio = train.isnull().sum() / len(train)
drop_cols = missing_ratio[missing_ratio > missing_threshold].index
train.drop(columns=drop_cols, inplace=True)

# --- Categorical and Numerical Separation ---
categorical_cols = train.select_dtypes(include='object').columns
numerical_cols = train.select_dtypes(include=['int64', 'float64']).columns.drop('Id')

# --- Imputation ---
# For numerical columns: median imputation
num_imputer = SimpleImputer(strategy='median')
train[numerical_cols] = num_imputer.fit_transform(train[numerical_cols])

# For categorical columns: mode imputation
cat_imputer = SimpleImputer(strategy='most_frequent')
train[categorical_cols] = cat_imputer.fit_transform(train[categorical_cols])

# --- Label Encoding for Ordinal Categorical Variables ---
label_encodable = ['ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond',
                   'HeatingQC', 'KitchenQual', 'FireplaceQu', 'GarageQual', 'GarageCond']

encoding_map = {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, 'NA': 0}
for col in label_encodable:
    train[col] = train[col].map(encoding_map)

# Label Encoding remaining categoricals
for col in categorical_cols:
    if col not in label_encodable:
        train[col] = LabelEncoder().fit_transform(train[col])

# --- Feature Engineering ---
# Total area feature
train['TotalSF'] = train['TotalBsmtSF'] + train['1stFlrSF'] + train['2ndFlrSF']

# Age of the house at the time of sale
train['HouseAge'] = train['YrSold'] - train['YearBuilt']
train['RemodAge'] = train['YrSold'] - train['YearRemodAdd']

# Total number of bathrooms
train['TotalBath'] = train['FullBath'] + (0.5 * train['HalfBath']) + train['BsmtFullBath'] + (0.5 * train['BsmtHalfBath'])

# Is house new
train['IsNew'] = (train['YearBuilt'] == train['YrSold']).astype(int)

# --- Scaling Numerical Features ---
scaler = StandardScaler()
scaled_features = scaler.fit_transform(train[numerical_cols])
scaled_df = pd.DataFrame(scaled_features, columns=numerical_cols)

# --- Final Dataset ---
final_df = pd.concat([scaled_df, train.drop(columns=numerical_cols)], axis=1)
print("\n--- Final Data Shape ---")
print(final_df.shape)

# --- Save Processed Data ---
final_df.to_csv("processed_house_prices.csv", index=False)
print("\nProcessed dataset saved as 'processed_house_prices.csv'")
