#  ma'am
# reverse string same 
# using copy method (return shallow copy of list)
# [1,2,1]  after palindrome list same a [1,2,1]

# list1 = [1,2,1]
list1 = [1,2,2]
copy_list = list1.copy()
copy_list.reverse()
if(copy_list==list1):
    print("[1,2,1] is palindrome")
else:
    print("NOT a palindrome")
