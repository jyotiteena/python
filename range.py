# by default start from zero(0)

# range(start,end,step)
# range(start?,end,step?)

print("0 to 4")
for ele in range(5):
    print(ele) # 0 to 4
    
print("1 to 4")
for ele in range(1,5):
    print(ele) # 1 to 5

print("odd - 1,3,5,7,9")
for ele in range(1,10,2):
    print(ele) # 1,3,5,7,9
    
print("even - 2,4,6,8, 10")
for ele in range(2,11,2):
    print(ele) # 2,4,6,8
    
print("reverse loop")
for ele in range(10,0,-1):
    print(ele)

print("multiplication")
num = int(input("enter any value = "))
for ele in range(1,11):
    print(ele*num)
    
    
# pass -> it is null statement that does nothing, placeholder for future code

for i in range(10):
    pass

print("next time")

# sum of first n number 
sum = 0
num = 5
for i in range(1,num+1):
    sum +=i
    
print("sum = ",sum)


#factorial
fact = 1
for i in range(1,num+1):
    fact *=i
    
print("fact = ",fact)