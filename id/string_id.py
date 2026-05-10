# Strings are immutable.

s = "hello"

print(id(s))

s = s + " world"

print(id(s))

# OUTPUT:
# Different ids

# Explanation:
# New string object is created.