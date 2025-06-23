# problem 

# def sum(a,b,c):
#     print(a+b+c)
    
# sum(23,4,5,2) # can't pass extra arg


# ///////////// solution ///////////////////////
def add(*values):
    print(values)
    # print(type(values))
    print(sum(values))
    print(values.count(2))
    
    
add(34,4,2,5)