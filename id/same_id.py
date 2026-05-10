# If two variables point to same object,
# then their id can be same.

a = 10
b = 10

print(id(a))
print(id(b))

# OUTPUT:
# Same ids may be printed

# Explanation:
# Python reuses small immutable objects like integers.
