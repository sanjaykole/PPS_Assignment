import numpy as np

print("--Array Creation--")
arr_1d= np.array([10,20,30,40,50,60,70])
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("1D Array:",arr_1d)
print("2D Array:",arr_2d)
print()

print("--Indexing--")
first_element = arr_1d[0]
last_element = arr_1d[-1]
element_2d = arr_2d[1, 2]

print(f"First element: {first_element}")
print(f"last element: {last_element}")
print(f"Element in row 1, Column 2: {element_2d}")
print()

print("--Slicing--")
slice_1d = arr_1d[1:4]
sub_grid = arr_2d[0:2,1:3]

print("1D slice:",slice_1d)
print("2D Sub Grid:\n",sub_grid)
print()

print("--Vectorized Operations--")
a = np.array([1,2,3])
b = np.array([10,20,30])

addition = a+b
multiplication = a*5
squared = a**2
sine_vales = np.sin(a)

print("Vectorized addition (a+b):",addition)
print("scalar multiplication (a*5):",multiplication)
print("Element wise power (a**2):",squared)
print("Sine values of a:",sine_vales)
print()

print("--Boolean Operation--")
prices= np.array([15, 18, 125, 55, 80])
expensive_prices = prices[prices>50]
print(expensive_prices)
