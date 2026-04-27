# Explicit exception handling
#Value Error
try:
    a = int(input())
    print(a)
except ValueError:
    print("Value should be integer only")
print("Hello")