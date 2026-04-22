'''
Input-Output
Scenario 1:
Display Product Information You need to create a program that accepts details about a product (name, price, and availability) and displays the information in a structured format. This question evaluates your understanding of Python's basic syntax and input/output operations.

Input Format:
 Name of the product (string).
 Price of the product (float).
 Availability (boolean).

Constraints:
 Product name length ≤ 50 characters.
 Price ≥ 0.
 Availability should be True or False.

Output Format:
 Three lines displaying product details.

Sample Inputs and Outputs:

Sample Input  : 
Laptop 59999.99 True
Phone 29999.50 False
Tablet 15000.0 True
Desktop 45000.75 False
Camera 25000.0 True

Sample Output :
Product Name: Laptop 
Price: 59999.99 
In Stock: True

Product Name: Phone 
Price: 29999.50 
In Stock: False

Product Name: Tablet 
Price: 15000.0 
In Stock: True

Product Name: Desktop 
Price: 45000.75 
In Stock: False

Product Name: Camera
Price: 25000.0 
In Stock: True
'''

a,b,c = input().split()
print("Product Name:",a)
print("Price:",b)
print("Instock:",c)