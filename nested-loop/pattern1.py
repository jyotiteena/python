print("pattern.............1")
for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()

print("pattern.............2")
for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()

print("pattern.............3")
for i in range(1,5):
    for j in range(i):
        print(i,end=" ")
    print()

print("pattern.............4")
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("pattern.............5")
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print("pattern.............6")

for i in range(5,0,-1):
    for j in range(i):
        print(i,end=" ")
    print() 

print("pattern.............7")

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()   

print("pattern............8")
for i in range(5):
    for j in range(5-i-1):
        print(" ", end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()

