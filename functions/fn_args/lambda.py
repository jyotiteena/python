# lambda or anonymous function (fn without name)
# syntax => lambda args : expression 

# simple way 
def cube(n):
    return n**3

ans = cube(3)
print(ans)

# lambda way
ans = lambda n : n**3
print(ans(4))