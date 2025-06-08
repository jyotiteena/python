list1 = [1,2,3,4]

for i in list1:
    print(i)

print("using while loop")
j = 0
while j < len(list1):
    print(list1[j])
    j = j+1

print("using range")
for i in range(len(list1)):
    print(list1[i])