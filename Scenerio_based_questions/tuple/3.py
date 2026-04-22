'''
Scenario: You are working on an employee management system where you are storing employee names in a tuple. 
One day, a manager asks for the position of a specific employee within the list. 
Your task is to write a function that finds the index of a given employee name in the tuple. 
The function should return the index if the employee is present in the tuple, and it should return -1 if the employee is not found.
Example Input 1:
employees = ("John", "Alice", "Bob", "Sarah", "Tom")
Expected Output 1:
Index of 'Bob': 2
Explanation:
In this case, the tuple contains the employee names: ("John", "Alice", "Bob", "Sarah", "Tom").
 "John" is at index 0.
 "Alice" is at index 1.
 "Bob" is at index 2, so the function returns 2.
Example Input 2:
employees = ("Michael", "Anna", "James", "Emma")
Expected Output 2:
Index of 'James': 2
Explanation:
In this case, the tuple contains the employee names: ("Michael", "Anna", "James", "Emma").
 "Michael" is at index 0.
Page 59 of 71
 "Anna" is at index 1.
 "James" is at index 2, so the function returns 2.
Test Cases:
1. Input: ("George", "Sophia", "William", "Emma") Output: Index of 'Sophia': 1
2. Input: ("Daniel", "Sophia", "Paul", "Lucas") Output: Index of 'Lucas': 3
3. Input: ("Eve", "Grace", "Henry", "Zoe") Output: Index of 'Zoe': 3
4. Input: ("Ava", "Ella", "Liam", "Noah") Output: Index of 'Liam': 2
5. Input: ("Jack", "Emma", "Mason", "Olivia") Output: Index of 'Zara': -1
'''

employees = eval(input())
name = input()

if name in employees:
    print("Index of", name, ":", employees.index(name))
else:
    print("Index of", name, ":", -1)