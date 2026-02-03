# 1: Square numbers 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)

# 2: Even numbers 1 to 10
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)

# 3: Convert strings to uppercase
words = ["hello", "world"]
upper_words = [w.upper() for w in words]
print(upper_words)

# 4: Multiply numbers by 10
nums = [1, 2, 3]
times_ten = [n*10 for n in nums]
print(times_ten)

# 5: Nested comprehension (pairs)
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)
