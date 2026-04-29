#Explicit expection handling
#Type Error
a = input()
b = int(input())
print(a*b)
try:
    print(a+b)
except TypeError:
    print("Both the values should be string or integer")
print(b*3)