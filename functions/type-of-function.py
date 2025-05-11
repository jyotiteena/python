# two type of function 
# built-in fn -> print(), len(), type(), range()
# user define fn 

print("first", end=" / ")
print("second")

print("third", "forth", sep=", ")

# default parameter 
def sum(a=23,b=4):
    print(a+b)
sum(3)
sum()