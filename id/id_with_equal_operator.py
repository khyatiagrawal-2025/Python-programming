# == checks value
# id() checks object identity

a = [1, 2]
b = [1, 2]

print(a == b)
print(id(a) == id(b))

# OUTPUT:
# True
# False

# Explanation:
# Values are same
# But objects are different.