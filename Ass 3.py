import pandas as pd
# 1.IMPORT dATASET
file_path =r"C:\Users\CC\Downloads\customers-1000.csv"
df = pd.read_csv(file_path)
print("Dataset import successfully\n",df)

# 2. INITIAL DATA INSPECTION
print("="*60)
print("1.First 5 Rows")
print("="*60)
print(df.head(),"\n")

print("="*60)
print("2.Dataset Dimensions")
print("="*60)

print(f"Rows:{df.shape[0]},columns:{df.shape[1]}\n")

print("="*60)
print("3.Column Name & Data Types")
print("="*60)
print(df.dtypes,"\n")

print("="*60)
print("4.Concise Summary")
print("="*60)
print("\n")

print("="*60)
print("5.Missing Values Check")
print("="*60)

missing_data = df.isnull().sum()
print(missing_data[missing_data>0]if missing_data.sum()>0 else "No missing values found")
print("\n")

print("="*60)
print("6.Duplicate Row Check")
print("="*60)
print(f"Number of Duplicate Row: {df.duplicated().sum}\n")

# 3.DESCRIPTIVE STATISTICAL ANALYSIS
print("="*60)
print("7.Numerical Summary Statistics")
print("="*60)
print(df.describe().T,"\n")

print("="*60)
print("8.Categorical Summary Statistics")
print("="*60)
print(df.describe(include=['object','category']),"\n")

print("="*60)
print("9.Value Count For Categorical Columns")
print("="*60)
categorical_cols = df.select_dtypes(include=['object','category']).columns

for col in categorical_cols:
    print(f"---{col}---")
    print(df[col].value_counts(),"\n")

print("="*60)
print("10.Additional Numeric Metrics")
print("="*60)
numeric_cols = df.select_dtypes(include =['number']).columns

metrics_df = pd.DataFrame({
    'Mean': df[numeric_cols].mean(),
    'Median': df[numeric_cols].median(),
    'Variance': df[numeric_cols].var(),
    'Skewness': df[numeric_cols].skew()

})
print(metrics_df)
