import random
playing = True
number =str(random.randint(0,9))

print("i will genarate a number from 0 to 9 and you have to guess a number one digit at a time. ")
print("the game ends when you get one hero!")

while playing:
    guess= input("enter a number from 0 to 9:")
    if number == guess:
        print("you win the game")
        print("the number was:", number)
        break

    else:
        print("your guess wasnt quite right, try again.\n")