'''
Scenario 4:
Employee Dictionary Manipulation
Theory: This task involves creating an employee dictionary from user input, where each employee has an ID and a name. Additionally, you will create a second dictionary that stores the length of each employee’s name. This problem strengthens your knowledge of dictionary manipulations and basic string operations.
Input Format:
 An integer N (number of employees).
 N lines containing space-separated employee ID (integer) and name (string).
Constraints:
 1 ≤ N ≤ 100.
 Employee name length ≤ 50.
Output Format:
 The employee dictionary.
 The dictionary of employee name lengths.
Sample Inputs and Outputs:
Sample Input
Sample Output
3 101 Alice 102 Bob 103 Charlie
Employees: {101: 'Alice', 102: 'Bob', 103: 'Charlie'} Name Lengths: {101: 5, 102: 3, 103: 7}
2 201 David 202 Edward
Employees: {201: 'David', 202: 'Edward'} Name Lengths: {201: 5, 202: 6}
4 301 Grace 302 Helen 303 Irene
Employees: {301: 'Grace', 302: 'Helen', 303: 'Irene', 304: 'Julia'} Name Lengths: {301: 5, 302: 5, 303: 5, 304: 5}
304 Julia
1 401 Frank
Employees: {401: 'Frank'} Name Lengths: {401: 5}
5 501 Anne 502 Bea 503 Chloe 504 Diana 505 Elle
Employees: {501: 'Anne', 502: 'Bea', 503: 'Chloe', 504: 'Diana', 505: 'Elle'} Name Lengths: {501: 4, 502: 3, 503: 5, 504: 5, 505: 4}
'''


n = int(input())

employees = {}
name_lengths = {}

for _ in range(n):
    emp_id, name = input().split()
    emp_id = int(emp_id)
    
    employees[emp_id] = name
    name_lengths[emp_id] = len(name)

print("Employees:", employees)
print("Name Lengths:", name_lengths)