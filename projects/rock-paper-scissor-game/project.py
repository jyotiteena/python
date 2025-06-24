"""
    cases
     A -Rock
     Rock - Rock => tie
     Rock - Paper =>paper win
     rock - scissor => rock win
     
     B - Paper
     Paper - Paper => tie
     Papper - Rock => paper win
     Paper = scissor => scissor wind
     
     C - Scissor
     Scissor - Scissor = tie
     Scissor - Rock = Rock win
     Scissor - paper = Scissor win
    
"""
import random
list_item = ["Rock","Scissor", "Paper"]
choice = input("Enter your move = Rock, Paper and Scissor = ")
random_choice = random.choice(list_item)
print(f"User choice = {choice} and computer choice = {random_choice}")

if(choice==random_choice):
    print("both chooses same so that Match Tie 😥")
    
elif choice=="Rock":
    if random_choice == "Paper":
        print("paper cover rock - computer win")
    else:
        print("Rock smashes scissor = you win")
        
elif choice=="Scissor":
    if random_choice == "Paper":
        print("scissor cut paper - you win")
    else:
        print("Rock smashes scissor = computer win")
        
elif choice=="Paper":
    if random_choice == "Scissor":
        print("scissor cut paper - computer win")
    else:
        print("paper cover rock = you win")