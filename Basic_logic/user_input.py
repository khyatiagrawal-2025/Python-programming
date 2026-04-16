# basic input
name = input("Enter your name: ")
print("Hello", name)

# integer input
age = int(input("Enter your age: "))
print("Age:", age)

# float input
price = float(input("Enter price: "))
print("Price:", price)

# multiple inputs in one line
a, b = map(int, input("Enter two numbers: ").split())
print("Sum:", a + b)