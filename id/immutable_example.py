# Integers are immutable.
# Changing value creates new object.

x = 5

print(id(x))

x = x + 1

print(id(x))

# OUTPUT:
# Different ids

# Explanation:
# New object is created after modification.