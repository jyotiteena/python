# only 2 types = while and for loop 
# i++ not work 

# count, i, j => interator
count = 1
# while (count<=5):
while count<=5:
    print("jyoti =>",count)
    count = count+1
    
    
i = 1
while(i<=10):
    print(i*i)
    i +=1
    
list = [1,2,3,4,5,6]
i = 0
while(i<len(list)):
    print(list[i])
    i+=1
    
# tuple 
tuple = (1,2,3,4,5,6)
# find index number of any element 
print("find value =")
idx = 1
while idx<len(tuple):
    if(tuple[idx]==3):
        print("found at index number",idx)
    else:
        print("not found")
    idx+=1


# skip value 
j=1
while(j<=5):
    if(j==3):
        j+=1
        continue
    print(j)
    j+=1
    