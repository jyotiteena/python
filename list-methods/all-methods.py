# append, pop, clear, insert, count, remove, extend , index, sort, reverse, copy 


# count  - count of element exist in list 
list1 = [12,3,44,5,6,3,12]
print(list1.count(12))
print(list1.count(44))

list2 = [12,3,5,63,2,4]
list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)

list2.reverse()
print(list2)

list3 = list2.copy()
print(list3)

print(list2.index(3))