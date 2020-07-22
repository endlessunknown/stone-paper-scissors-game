from random import *
n = 0  # No. of Games Played
usr_score = 0  # No. of times user won
cpu_score = 0  # No. of times cpu won
draws = 0  # No. of draws

l = ["stone", "paper", "scissors"]

print("Enter Your Choice : ")
print("Stone \nPaper \nScissors")

while n < 10: # you'll get 10 chances
    cpu_choice = choice(l)
    usr_choice = input(">>>>> ").lower()

    if usr_choice == "stone":
        if cpu_choice == "stone":
            print("Draw")
            draws += 1
            n += 1
        elif cpu_choice == "paper":
            print("You Lost")
            cpu_score += 1
            n += 1
        else:
            print("You Won")
            n += 1
            usr_score += 1
    elif usr_choice == "paper":
        if cpu_choice == "paper":
            print("Draw")
            draws += 1
            n+=1
        elif cpu_choice == "scissors":
            print("You Lost")
            cpu_score += 1
            n += 1
        else:
            print("You Won")
            n += 1
            usr_score += 1
    elif usr_choice == "scissors":
        if cpu_choice == "scissors":
            print("Draw")
            draws += 1
            n += 1
        elif cpu_choice == "stone":
            print("You Lost")
            cpu_score += 1
            n += 1
        else:
            print("You Won")
            n += 1
            usr_score += 1
    else:
        print("Invalid choice")
        continue

print("No. of Draws :", draws)
print("No. of times user won :", usr_score)
print("No. of times cpu won :", cpu_score)
print("User won") if usr_choice > cpu_choice else print("Cpu Won")
