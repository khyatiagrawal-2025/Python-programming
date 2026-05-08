# == checks value equality
# is checks memory location (object identity)

a = [1,2]
b = [1,2]

print(a == b)   # True
print(a is b)   # False