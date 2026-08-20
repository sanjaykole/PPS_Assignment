import numpy as np
#=======================================================
# 1.Generate the full truth table(2*3=8 Combination)
#=======================================================
truth_table = np.array([
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1],
], dtype=np.uint8)
print("---1.Input Truth Table Matrix (8x3)---")
print("A B C")
print(truth_table)
print()

#===========================================================
# 2.EXTRACT COLUMNS (SLICING) & EVALUATE BOOLEAN LOGIC
#===========================================================
#Slicing Indivial Columns: matrix[:,column_index]
#In Numpy: & is AND,| is OR
A=truth_table[:,0]
B=truth_table[:,1]
C=truth_table[:,2]

alarm_method_A = (A&B)|(B&C)|(A&C)


senser_sum = np.sum(truth_table,axis=1)
alarm_method_B = (senser_sum >=2).astype(np.uint8)

is_identical = np.array_equal(alarm_method_A,alarm_method_B)

print("---2.Logic Evaluation---")
print(f"Active Senser Counts per Row: {senser_sum}")

#===================================================================
# 3.VERIFY & APPEND OUTPUT TO FULL DIGITAL MATRIX
#===================================================================
full_circuit_table = np.column_stack((truth_table,alarm_method_B))

print("---3.Complete Circuit Verification Table---")
print("A B C")
print("-------------")
for row in full_circuit_table:
    print(f"{row[0]} {row[1]} {row[2]} | {row[3]}")
