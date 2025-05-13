import random
print("enter any number from 1 to 100")

num1 = int(input("enter start the number = "))
num2 = int(input("enter end the number = "))

if(num1>=1 and num2<=100):
    random_num = random.randint(num1,num2)
    print("your value is = ",random_num)
else:
    print("range should be from 1 to 100")