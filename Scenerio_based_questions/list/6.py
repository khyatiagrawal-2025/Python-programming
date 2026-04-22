'''
You are given a matrix A, you have to return an list containing sum of each row elements followed by sum of each column elements of the matrix.
NOTE: If the matrix given is of size (N x M), then the array you return would be of size (N + M), where first N elements contain the sum of each N rows, and the next M elements contain the sum of each M columns.
Example
Input [[1, 2],[4, 5],[8, 9]] Output [3, 9, 17, 13, 16] Explanation SUM OF ROWS ARE 3,9,17
SUM OF COLUMNS ARE 13,16
Test Case
1. [[1, 2],[4, 5],[8, 9]] [3, 9, 17, 13, 16]
2. [[1,4,2],[8,0,3]] [7, 11, 9, 4, 5]
3. [[1,2], [6,4], [9,5], [0,7]] [3, 10, 14, 7, 16, 18]
4. [[2,4,8,1],[0,5,3,7]] [15, 15, 2, 9, 11, 8]
'''

A = eval(input())

result = []

# Row sums
for row in A:
    result.append(sum(row))

# Column sums
for j in range(len(A[0])):
    col_sum = 0
    for i in range(len(A)):
        col_sum += A[i][j]
    result.append(col_sum)

print(result)