'''
Scenario: You are working as a software engineer at a company that tracks inventory. Each product is assigned a unique number in a consecutive series. However, due to a system glitch, one number is missing from the series. Your task is to identify the missing number so the inventory can be corrected. The series is guaranteed to have exactly one missing number, and all other numbers appear exactly once.
Constraints:
1. The input list will contain integers in ascending order.
2. The list will always have at least two numbers with one number missing from the series.
Sample Input and Output with Explanation:
1. Input: [1, 2, 4, 5] Output: 3 Explanation: The series [1, 2, 3, 4, 5] is expected, but 3 is missing.
2. Input: [10, 11, 12, 14] Output: 13 Explanation: The series [10, 11, 12, 13, 14] is expected, but 13 is missing.
3. Input: [100, 101, 102, 103, 105] Output: 104 Explanation: The series [100, 101, 102, 103, 104, 105] is expected, but 104 is missing.
Test Cases:
1. Input: [1, 2, 3, 5] Output: 4
2. Input: [20, 21, 22, 24] Output: 23
3. Input: [50, 51, 52, 54] Output: 53
4. Input: [7, 8, 10] Output: 9
5. Input: [15, 16, 17, 19] Output: 18
'''

arr = eval(input())

for i in range(len(arr) - 1):
    if arr[i+1] != arr[i] + 1:
        print(arr[i] + 1)
        break