# add, remove, clear, pop  (remove randome values)
set1 = set()
set1.add(122)
set1.add(21)
set1.add(45)
set1.add(21)
print(set1) #{122, 45, 21}
print(len(set1)) # 3

set1.remove(21)
print(set1)

# tuple can be added 
set1.add((12,22,3)) #{(12, 22, 3), 122, 45}
print(set1)

set1.clear()
print(set1)
print(len(set1)) #0

set2 = set()
set2.add(122)
set2.add(211)
set2.add(425)
set2.add(231)
print(set2.pop()) # randome
print(set2)
print(set2.pop())
print(set2)

# union and intersection 
# union -  combine both set vlaues and return new
# intersection -  combine common set vlaues and return new
set3 = {1,2,3,4}
set4 = {4,5,6}
print(set3.union(set4)) #{1, 2, 3, 4, 5, 6}

print(set3.intersection(set4)) #{4}




