# 1: Create a set
s = {1, 2, 3, 3}
print(s)  # {1, 2, 3}

# 2: Add element
s.add(4)
print(s)

# 3: Remove element
s.remove(2)
print(s)

# 4: Union
s2 = {3, 4, 5}
print(s | s2)  # {1, 2, 3, 4, 5}

# 5: Intersection
print(s & s2)  # {3, 4}
