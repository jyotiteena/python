# is and is not  (	Are they the same object?)
# == (	Are the contents equal)
a = 100
b = 200
c= a
d = 200

print(a is b) # False
print(b is not c) #True
print(a is not c) # False
print(a is c) #True
print(b==d) # True
print(b is d) # True

# x = 1000
# y = 1000
# print(x == y)
# print(x is y)  