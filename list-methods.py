# append, sort, reverse, insert , remove(value)->first occurance, pop(index), 
# append like a push 
list1 = [12,3,45]
print(list1.append("new")) # can't return None
list1.append("word")
print(list1) #[12, 3, 45, 'new', 'word']
# list1.append(5,6,7) error
list1.append(5)
print(list1) #[12, 3, 45, 'new', 'word',5]
list2 = [23,5,34,89,9]
list2.sort()
print(list2) #[5, 9, 23, 34, 89]
list2.sort(reverse=True)
print(list2) #[89, 34, 23, 9, 5]

str1 = ["teena","mega", "jyoti","joy"]
str1.sort()
print(str1) #['joy', 'jyoti', 'mega', 'teena']
str1.sort(reverse=True)
print(str1) #['teena', 'mega', 'jyoti', 'joy']

mix = ["3",3,23,"jyoti"]
# mix.sort() #TypeError: '<' not supported between instances of 'int' and 'str'
# print(mix)

list3 = ['a',34,"abc",342]
list3.reverse()
print(list3) #[342, 'abc', 34, 'a']


# insert (idx,ele) -> insert element at index 
list3.insert(1,"xyz")
print(list3) #[342, 'xyz', 'abc', 34, 'a']

list3.remove(34)
print(list3) #[342, 'xyz', 'abc', 'a']
print(list3.pop(2)) #abc
print(list3) #[342, 'xyz', 'a']