# lambda arguments: expression

add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

# /////// with map /////
list1 = [1,2,4,5]
square = list(map(lambda ele:ele*2,list1))
print(square)

filterData = list(filter(lambda ele: ele>2,list1))
print(filterData)