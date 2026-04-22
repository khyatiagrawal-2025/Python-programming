#A dictionary is a mutable collection of key-value pairs in Python.

'''
Scenario 1:
Retrieve Contact Details In this program, you are provided with a dictionary containing the name and phone number of a contact. Your task is to retrieve and display the phone number for a given name. This question tests your ability to access values from a dictionary in Python.
Input Format:
 A single name of a contact (string).
Constraints:
 The dictionary contains only one key-value pair: {"Alice": "9876543210"}.
 The input name will always exist in the dictionary.
Output Format:
 A single line with the format: "Phone number of [Name]: [Phone Number]".
Sample Inputs and Outputs:
Sample Input
Sample Output
Alice
Phone number of Alice: 9876543210
Ram
Phone number of Ram: 9876513210
Sita
Phone number of Alice: 9819543210
Tarun
Phone number of Alice: 9876273210
Naman
Phone number of Alice: 8276543210
'''

contact = eval(input())
name = input()

print("Phone number of", name + ":", contact[name])