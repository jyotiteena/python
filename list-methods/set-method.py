set1 = {111,22,23,4,2,1}
set2 = {11,22,43}
print(set1)
set1.add("jyoti")

# union
print(set1.union(set2))

# difference 
print(set1.difference(set2))
print(set1-set2)

set3 = {"jyoti","teena","prem"}
print(set3.pop()) #prem
print(set3) #{"jyoti","teena"}

set3.add("love")
print(set3) # added 

set4 = set1.copy()
print(set4)