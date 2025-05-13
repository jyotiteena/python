import random
target = random.randint(1,100)

while True:
    choice = input("Guess the target or Quit(Q):")
    if(choice=="Q" or choice=="q"):
        break
    choice = int(choice)
    if(choice==target):
        print("correct guess = ",target)
        break
    elif(choice<target):
        print("your value is less than target value")
    else:
        print("your value is greater than target value")
    
print("GAME OVER")