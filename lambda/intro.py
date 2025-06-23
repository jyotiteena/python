# lambda arguments: expression

add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

# /////// with map /////
list1 = [1,2,4,5]
square = list(map(lambda ele:ele*2,list1))
print(square)

filterData = list(filter(lambda ele: ele>2,list1))
print(filterData)

list2 = [{"id":123,"name":"jyoti"},{"id":232,"name":"teena"}]
show = map(lambda ele:ele, list2)
show2 = list(map(lambda ele:ele['name'], list2))
print("show = ",show)
print("show2 = ",show2) #['jyoti', 'teena']

filterData = list(filter(lambda ele: ele['id']==123, list2))
print(filterData)

