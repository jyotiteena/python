
# remove - delete first occurance value 
# pop - empty pop delete last index and if specify index then remove that existing element
list1 = [1,2,3,2]

list1.remove(2)
print(list1) #[1, 3, 2]

list1.pop()
print(list1)  # [1,3]

list1.pop(1)
print(list1) # [1]

# clear - all remove data
list1.clear()
print(list1)