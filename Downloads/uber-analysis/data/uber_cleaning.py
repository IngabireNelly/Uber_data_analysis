# uber_cleaning.py

import pandas as pd

# === Step 1: Load the Dataset ===
df = pd.read_csv("uber.csv")
print("✅ Loaded dataset. First 5 rows:")
print(df.head())

# === Step 2: Check Structure & Missing Values ===
print("\n🧾 Dataset Info:")
print(df.info())

print("\n🧹 Missing Values:")
print(df.isnull().sum())

# === Step 3: Drop Rows with Missing Values ===
df.dropna(inplace=True)
print(f"\n🚮 Dropped rows with missing values. Remaining rows: {len(df)}")

# === Step 4: Convert Pickup Datetime Column ===
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

# === Step 5: Feature Engineering ===
df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['weekday'] = df['pickup_datetime'].dt.day_name()  # Monday, Tuesday, etc.

# Peak hour definition: 7-9 AM or 5-7 PM
df['peak'] = df['hour'].apply(lambda x: 'Peak' if 7 <= x <= 9 or 17 <= x <= 19 else 'Off-Peak')

print("\n🆕 New Columns Added: hour, day, month, weekday, peak")
print(df[['pickup_datetime', 'hour', 'weekday', 'peak']].head())

# === Step 6: Descriptive Statistics ===
print("\n📊 Descriptive Statistics:")
print(df.describe())

# === Step 7: Save the Cleaned and Enhanced Dataset ===
df.to_csv("uber_cleaned.csv", index=False)
print("\n✅ Saved cleaned dataset as 'uber_cleaned.csv'")
