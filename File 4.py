import pandas as pd

file_path = r"C:\Users\CC\Downloads\employee_data1.csv"
df = pd.read_csv(file_path)
print("Dataset imported successfully\n", df)
print("\n" + "=" * 70 + "\n")

# 1. Remove Duplicates
duplicate_count = df.duplicated().sum()
print("Number of duplicate rows:", duplicate_count)

df_cleaned = df.drop_duplicates().copy()

# 2. Handle Missing Values (NaN / None)
print("\nMissing values per column:")
print(df_cleaned.isnull().sum())

median_age = df_cleaned["Age"].median()
df_cleaned["Age"] = df_cleaned["Age"].fillna(median_age)

mean_salary = df_cleaned["salary"].mean()
df_cleaned["salary"] = df_cleaned["salary"].fillna(mean_salary)

df_cleaned["department"] = df_cleaned["department"].fillna("Unassigned")

# 3. Modify Data Structure & Clean Format
df_cleaned["name"] = df_cleaned["name"].str.strip().str.title()

df_cleaned["join date"] = pd.to_datetime(df_cleaned["join date"])

df_cleaned[["First_name","Last_name"]] = df_cleaned["name"].str.split(" ", expand=True)

df_cleaned["join_year"] = df_cleaned["join_date"].dt.year

df_cleaned = df_cleaned.drop(columns=["name"])

odered_columns = [
    "First Name",
    "Last Name",
    "department",
    "Age",
    "salary",
    "Join Date",
    "join year",
]

print(df_cleaned)
print(df_cleaned.dtypes)