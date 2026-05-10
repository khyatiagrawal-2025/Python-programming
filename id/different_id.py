# Two lists with same values can still have different ids.

a = [1, 2]
b = [1, 2]

print(id(a))
print(id(b))

# OUTPUT:
# Different ids

# Explanation:
# Both lists are separate objects in memory.