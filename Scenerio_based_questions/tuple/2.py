'''
Scenario: You have been given a tuple containing a list of products sold in a store. However, some of these products have been listed multiple times. As part of the inventory management system, you need to remove any duplicates from the tuple to get a list of unique products. Your task is to write a function that returns a new tuple with only the unique product names.
Example Input 1:
products = ("apple", "banana", "orange", "banana", "apple", "grape", "orange")
Expected Output 1:('apple', 'banana', 'orange', 'grape')
Explanation: In this case, the tuple contains the following products: ("apple", "banana", "orange", "banana", "apple", "grape", "orange"). To remove duplicates:
 The first occurrence of "apple" remains, and the second occurrence is removed.
 The first occurrence of "banana" remains, and the second is removed.
 The first occurrence of "orange" remains, and the second is removed.
 "grape" remains as it appears only once. Thus, the result will be ('apple', 'banana', 'orange', 'grape').
Example Input 2:
products = ("laptop", "phone", "tablet", "laptop", "camera", "phone")
Expected Output 2:
('laptop', 'phone', 'tablet', 'camera')
Explanation:
In this case, the tuple contains the following products: ("laptop", "phone", "tablet", "laptop", "camera", "phone"). To remove duplicates:
 The first occurrence of "laptop" remains, and the second is removed.
 The first occurrence of "phone" remains, and the second is removed.
 "tablet" and "camera" are unique, so they are included as well. Thus, the result will be ('laptop', 'phone', 'tablet', 'camera').
Test Cases:
1. Input: ("cat", "dog", "cat", "bird", "dog", "fish") Output: ('cat', 'dog', 'bird', 'fish')
2. Input: ("red", "blue", "green", "blue", "yellow", "green") Output: ('red', 'blue', 'green', 'yellow')
3. Input: ("book", "pen", "book", "pencil", "pen") Output: ('book', 'pen', 'pencil')
4. Input: ("apple", "banana", "apple", "orange", "kiwi", "orange") Output: ('apple', 'banana', 'orange', 'kiwi')
5. Input: ("milk", "bread", "butter", "cheese", "milk", "butter") Output: ('milk', 'bread', 'butter', 'cheese')
'''

products = eval(input())

unique = []

for item in products:
    if item not in unique:
        unique.append(item)

result = tuple(unique)

print(result)