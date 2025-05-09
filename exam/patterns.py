print("pattern1........")
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()

print("pattern2........")

for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()

print("pattern3........")

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()

print("pattern4........")

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

print("pattern5........")

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

print("pattern6........")

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

print("pattern7........")
for i in range(1,6):
    for j in range(1,i):
        print(" ",end="")
    for k in range(i,6):
        print(k,end="")
    print()
