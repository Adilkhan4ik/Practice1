a=int(input())
b=int(input())
print(a+b)

#################

a, b = input().split()
print(int(a) + int(b))

#################

a, b = map(int, input().split())
print(a + b)

#################
# print(a)  # This would show a map object
a = map(int, input().split())
for x in a:
    print(x, end=' ')

#################


name = input("Enter your name: ")
print("Hello,", name)

################