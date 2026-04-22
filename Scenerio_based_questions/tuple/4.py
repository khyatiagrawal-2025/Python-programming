'''
Scenario: You are developing an e-commerce system where a tuple contains the product IDs of items in a customer's shopping cart. However, the system needs to update the cart by adding or removing products dynamically. Since tuples are immutable, you need to convert the tuple to a list, which will allow modifications (such as adding or removing product IDs). Your task is to write a function that converts a given tuple of product IDs into a list.
Example Input 1:
cart_items = (101, 102, 103, 104)
Expected Output 1:
[101, 102, 103, 104]
Explanation:
In this case, the cart contains the following product IDs: (101, 102, 103, 104). After converting the tuple to a list, the result will be [101, 102, 103, 104].
Example Input 2:
cart_items = (201, 202, 203)
Expected Output 2:
[201, 202, 203]
Explanation:
Here, the cart contains the product IDs: (201, 202, 203). After converting to a list, the result is [201, 202, 203].
Test Cases:
1. Input: (301, 302, 303, 304) Output: [301, 302, 303, 304]
2. Input: (501, 502) Output: [501, 502]
3. Input: (1001, 1002, 1003) Output: [1001, 1002, 1003]
4. Input: (11, 22, 33) Output: [11, 22, 33]
5. Input: (1, 2, 3, 4, 5) Output: [1, 2, 3, 4, 5]
'''

cart_items = eval(input())

result = list(cart_items)

print(result)