#Explicit exception handling
a = int(input())
b = int(input())
try:
    c = a-b
    print(a/c)
except ZeroDivisionError:
    print("We can't divide a number by zero")