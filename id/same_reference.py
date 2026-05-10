# Here both variables refer to same object.

a = [1, 2]
b = a

print(id(a))
print(id(b))

# OUTPUT:
# Same ids

# Explanation:
# b is not creating new list.
# It is pointing to same object as a.