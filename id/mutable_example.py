# Lists are mutable.
# Changes happen in same object.

a = [1, 2]

print(id(a))

a.append(3)

print(id(a))

# OUTPUT:
# Same ids

# Explanation:
# List changes without creating new object.