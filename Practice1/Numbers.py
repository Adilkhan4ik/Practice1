p = 15       # int
q = 3.14     # float
r = 5j       # complex
print(type(p))
print(type(q))
print(type(r))
#------------------------------
p = 3.5e3
q = 2E4
r = -7.6e10

print(type(p))
print(type(q))
print(type(r))
#------------------------------
p = 1+4j
q = 8j
r = -6j

print(type(p))
print(type(q))
print(type(r))
#------------------------------
p = 12      # int
q = 7.8     # float
r = 3j      # complex

# convert from int to float:
m = float(p)

# convert from float to int:
n = int(q)

# convert from int to complex:
o = complex(p)

print(m)
print(n)
print(o)

print(type(m))
print(type(n))
print(type(o))
#--------------------------------
import random

print(random.randrange(20, 80))
