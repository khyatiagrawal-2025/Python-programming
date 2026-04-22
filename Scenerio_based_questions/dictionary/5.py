'''
Filter Dictionary Using Comprehension
Dictionary comprehensions allow creating dictionaries from existing ones based on a specific condition. You can use {key: value for key, value in original_dict.items() if condition} for filtering.
This task involves filtering a dictionary by retaining only those key-value pairs where the value is greater than a given threshold.
Input Format:
 A dictionary with integer values.
 A threshold value ttt.
Constraints:
 The dictionary will contain only integer values.
 Only keys with values greater than ttt should remain.
Output Format:
 A dictionary containing the filtered key-value pairs.
Sample Inputs and Outputs:
Sample Input
Sample Output
{"a": 10, "b": 20, "c": 5} 15
{"b": 20}
{"x": 100, "y": 200, "z": 50} 150
{"y": 200}
{"apple": 3, "banana": 7} 5
{"banana": 7}
{"p": 1, "q": 5, "r": 10} 0
{"p": 1, "q": 5, "r": 10}
{"math": 75, "science": 80} 90
{}
'''

d = eval(input())
t = int(input())

result = {k: v for k, v in d.items() if v > t}
print(result)