list = [1,2,3]
print("list loop")

for val in list:
    print(val)
    
print("tuple loop")
    
tuple = (11,12,13)
for val in tuple:
    print(val)
    
print("string loop")
str1 = "first"
for char in str1:
    print(char)
    
    
# else is optional 
print("else part")
str2 = "second"
for char in str2:
    print(char)
else:
    print("END...........")
    
# list and tuple question
list1 = [1,2,3,4,5]

print("Square..........list")
for val in list1:
    print(val*val)
    
tuple1 = (1,2,3,4,5)

print("Square..........tuple")
for val in tuple1:
    print(val*val)
    
    
# find index of any existing element
idx = 0
for val in list1:
    if(val==3):
        print("find = ",idx)
        
    idx+=1
        
    
    
    
