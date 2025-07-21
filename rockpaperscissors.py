userchoice = input("please enter rock, paper, or scissors!")

computerchoice = "rock"

if userchoice == "rock":
    print(f"you tie! the computer chose {computerchoice}")
elif userchoice == "paper":
    print(f"you win! the computer chose {computerchoice}")
elif userchoice == "scissors":
    print(f"you lose! the computer chose {computerchoice}")
else:
    print(f"Looks like you chose an unspecified option! Please try typing in your choice again")
