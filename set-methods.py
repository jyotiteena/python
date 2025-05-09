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