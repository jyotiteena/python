tuple1 = (12,3,4,3,22,12)
print(tuple1[1:])

# methods -> index(ele) and count(ele)-> how many time of element
print(tuple1.index(12)) #0 index
# print(tuple1.index(1)) // ValueError: tuple.index(x): x not in tuple
print(tuple1.count(12)) #2
print(tuple1.count(3)) #2
print(tuple1.count(4)) #1
print(tuple1.count(4233)) #0