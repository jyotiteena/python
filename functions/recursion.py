def show(n):
    if n==0:  # base case
        return
    print(n)
    show(n-1)
    print("end...............")
show(5)

# //// factorial /////////
def fact(n):
    if n==1 or n==0:
        return 1
    return n * fact(n-1)

print(fact(5))