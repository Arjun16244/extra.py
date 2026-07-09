import random
while True:
    user_action=input("enter a choice from rock, paper, scissors:  ")
    possible_actions=["rock","paper", "scissors"]
    computer_action= random.choice(possible_actions)
    print(f"\nyou choosed, {user_action}  and computor choosed {computer_action}.\n")

    if user_action==computer_action:
        print(" it is a draw")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("rock smashes scissors, you win!")
        else:
            print("paper covers rock, you lose!")
    elif user_action=="paper":
        if computer_action=="rock":
            print("paper covers rock, you win!")
        else:
            print("scissors cut paper, you lose!")
    elif user_action=="scissors":
        if computer_action=="paper":
            print("scissors cut paper, you win!")
        else:
            print("rock smashes scissors, you lose!")
    
    play_again=input("play again? (y/n): ")
    if play_again != "y":
        break

