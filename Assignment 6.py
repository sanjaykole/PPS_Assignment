import pandas as pd

df = pd.read_csv(r"C:\Users\CC\Downloads\employee_data_Ass 6.csv")
print(df.head)

print("1.Basic Grouping(Average Salary & Bonus Per Department)")
dept_means = df.groupby("Department")[["Salary","Bonus"]].mean()
dept_means_formatted = dept_means.round(2)
print(dept_means_formatted)

print("\n"+"="*70 + "\n")

print("2.MultiColumn Grouping(Average Salary By Dept & Role)")
role_hierarchy = (
    df.groupby(["Department","Role"])[["Salary","Performance Rating"]]
    .mean()
    .round(2)
)
print(role_hierarchy)
print("\n"+"="*70 + "\n")

print("3. Advanced Aggregation Using .agg")
agg_operation =  {
    "Salary": ["mean", "min", "max"],
    "Bonus": "sum",
    "Project Completion" : "sum",
    "Performance Rating": "mean"
}
dept_summary = df.groupby("Department").agg(agg_operation).round(2)
print(dept_summary)
print("\n"+"="*70 + "\n")
