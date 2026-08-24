import pandas as pd

file_path = r"C:\Users\CC\Downloads\employee_data_30.csv"
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

mean_salary = df_cleaned["Salary"].mean()
df_cleaned["Salary"] = df_cleaned["Salary"].fillna(mean_salary)

df_cleaned["Department"] = df_cleaned["Department"].fillna("Unassigned")

# 3. Modify Data Structure & Clean Format
df_cleaned["Name"] = df_cleaned["Name"].str.strip().str.title()

df_cleaned["Join date"] = pd.to_datetime(df_cleaned["Join date"])

df_cleaned[["First_Name","Last_Name"]] = df_cleaned["Name"].str.split(" ", expand=True)

df_cleaned["Join_year"] = df_cleaned["Join date"].dt.year

df_cleaned = df_cleaned.drop(columns=["Name"])

odered_columns = [
    "First Name",
    "Last Name",
    "Department",
    "Age",
    "salary",
    "Join date",
    "Join year",
]

print(df_cleaned)
print(df_cleaned.dtypes)