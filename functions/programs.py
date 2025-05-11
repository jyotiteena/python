list1 = [1,2,4,5]
list2 = ["a",1,True,"jyoti",'final']

def length_list(list):
    return len(list)

print(length_list(list1))
print(length_list(list2))

def print_list(list):
    for value in list:
        print(value,end=" ")
    print()

print_list(list1)
print_list(list2)

# USD to INR conversion

def convertor(price):
    inr = price  * 83
    # print(price, "usd = ", inr,"INR")
    print(f"{price} USD = {inr} INR")

convertor(10)
