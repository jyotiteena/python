# tuple unpacking = return multiple values into tuple format
def show():
    a = 40
    b = 30
    return a,b

print(show()) # (40,30)

first, second = show()
print("a = ",first) #40
print("b = ",second) #30