userchoice = input("please enter rock, paper, or scissors!")

userchoicelower = userchoice.lower()

computerchoice = "rock"

if userchoicelower == "rock":
    print(f"you tie! the computer chose {computerchoice}")
elif userchoicelower == "paper":
    print(f"you win! the computer chose {computerchoice}")
elif userchoicelower == "scissors":
    print(f"you lose! the computer chose {computerchoice}")
else:
    print(f"Looks like you chose an unspecified option! Please try typing in your choice again")

#originally had multiple if statements but it was causing the else to print. elif makes it so that the else statement isn't tied to the last option and only runs if all the others aren't true