# different data type values store 

list1 = [12,22.3,True,"jyoti"]
print(list1)
print(type(list1)) #<class 'list'>
print(len(list1))

# string is immutabe
# list is mutable

str1 = "jyoti"
# str1[0] = "t" #TypeError: 'str' object does not support item assignment
  print(list1)
list1[2] = "second"
print(list1)
# print(list1[7]) #IndexError: list index out of range