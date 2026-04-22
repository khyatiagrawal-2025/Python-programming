'''
Access Value from Dictionary
A dictionary in Python stores data in key-value pairs, where keys are unique, and values are associated with these keys. You can retrieve a value by specifying its corresponding key using the syntax dictionary[key].
This program allows you to input a dictionary and a key to retrieve the associated value.
Input Format:
 A dictionary in JSON-like format.
 A key whose value needs to be retrieved.
Constraints:
 The key must exist in the dictionary.
Output Format:
 The value corresponding to the input key.
Sample Inputs and Outputs:
Sample Input                                 Sample Output
{"name": "Alice", "age": 25} name               Alice
{"a": 10, "b": 20, "c": 30} b                    20
{"fruit": "apple", "color": "red"} color         red
{"x": 5, "y": 15} y                              15
{"language": "Python"} language                 Python
'''
d = eval(input())   # dictionary input
key = input()       # key input

print(d[key])