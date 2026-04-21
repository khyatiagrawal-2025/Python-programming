'''import numpy
a=list(map(int, input().split()))
print(a)
n=numpy.array(a).reshape(3,3)
print(n)
#matrix in matrix using n,m'''
import numpy as np

# 1. Get the number of rows and columns
r, c = map(int, input("Enter rows and columns (separated by space): ").split())

# 2. Initialize the matrix
matrix = [] 

print(f"Enter the {r * c} elements one by one:")
for i in range(r): 
    row = []
    for j in range(c): 
        # Take input and add it to the current row
        element = int(input(f"Element at [{i}][{j}]: "))
        row.append(element)
    # Append the completed row to the matrix
    matrix.append(row)

# 3. Convert to a numpy array
result = np.array(matrix)

print("\nResulting Numpy Matrix:")
print(result)
