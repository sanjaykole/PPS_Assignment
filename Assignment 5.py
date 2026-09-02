import pandas as pd

df = pd.read_csv(r"C:\Users\CC\Downloads\output.csv")

print(df.head)

high_earning_engineers = df[(df['Department'] == "IT") &(df['Salary'] > 40000)]

sorted_df = df.sort_values(by=['Join_year', 'Salary', 'Age'],ascending=[False, False, False])

top_performers = df.loc[df['Join_year'] <= 2020,['Department', 'Salary']]

import numpy as np
df['Bonus_Eligible'] = np.where(df['Join_year'] <= 2022,'Yes', 'No')
print("======= Filtered: High Earning Engineers ======")
print(high_earning_engineers)

print("====== Sorted: BY Rating & Salary(Descending) ======")
print(sorted_df)

print("====== Conditional Selection: Top Performers(Rating>=4.0) ======")
print(top_performers)

print("====== Final DataFrame With Conditional 'Bonus Eligible' Column ======")
print(df)
