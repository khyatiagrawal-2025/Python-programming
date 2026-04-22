'''
Scenario: You are working on a customer database system where customer IDs are stored in two separate tuples. These tuples contain unique customer IDs from two different departments. However, some customers might have been added in both departments' lists, resulting in duplicate IDs. Your task is to merge these two tuples into one, remove any duplicate customer IDs, and return the result as a new tuple.
Example Input 1:
department_a = (101, 102, 103, 104)
department_b = (103, 105, 106)
Expected Output 1:
(101, 102, 103, 104, 105, 106)
Explanation:
In this case, the customer IDs from both departments are: department_a = (101, 102, 103, 104) department_b = (103, 105, 106).
 The ID "103" appears in both tuples, so it should appear only once in the merged result.
 After merging and removing duplicates, the final result is: (101, 102, 103, 104, 105, 106).
Example Input 2:
department_a = (201, 202, 203)
department_b = (203, 204, 205)
Expected Output 2:
(201, 202, 203, 204, 205)
Page 63 of 71
Explanation:
In this case, the customer IDs from both departments are: department_a = (201, 202, 203) department_b = (203, 204, 205).
 The ID "203" appears in both tuples, so it should appear only once.
 After merging and removing duplicates, the result is: (201, 202, 203, 204, 205).
Test Cases:
1. Input: (111, 112, 113, 114), (113, 115, 116) Output: (111, 112, 113, 114, 115, 116)
2. Input: (301, 302, 303, 304), (305, 302, 306) Output: (301, 302, 303, 304, 305, 306)
3. Input: (501, 502, 503), (503, 504, 505) Output: (501, 502, 503, 504, 505)
4. Input: (1001, 1002), (1003, 1004, 1001) Output: (1001, 1002, 1003, 1004)
5. Input: (121, 122, 123), (123, 124, 125) Output: (121, 122, 123, 124, 125)
'''

department_a = eval(input())
department_b = eval(input())

merged = department_a + department_b

unique = []

for item in merged:
    if item not in unique:
        unique.append(item)

result = tuple(unique)

print(result)