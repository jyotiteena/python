# even and odd number 

# num = int(input("enter any value = "))

# if(num % 2==0):
#     print("even nuumber")
# else:
#     print("odd number")
    
a = int(input("enter first value = "))
b = int(input("enter second value = "))
c = int(input("enter third value = "))
if(a>=b and a>=c):
    print("a is maximum")
elif(b>=c):
    print("b is maximum")
else:
    print("c is maximum")