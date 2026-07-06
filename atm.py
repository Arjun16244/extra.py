pin=1234
balance=5000

userpin= int(input("enter 4 digit pin"))
if userpin==pin:
    print("\nwelcome to python ATM!")
    while True:

        print("\n===========ATM MENU================")
        print("1. check balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. help")
        print("5. exit")

        choice= int(input("enter your choice:  "))
        if choice == 1:
            print("currenet balance = $", balance)
        elif choice == 2:
            amount=int(input("enter the amount to deposit:$"))

            if amount==0:
                print("invalid input!")
                continue
            balance = balance+amount
            print("money deposited successfully")
            print("updated balance=", balance)
        elif choice == 3:
            amount=int(input("enter amount to withdraw;  "))
            if amount > balance:
                print("insufficiant balance")
            else:
                balance=balance-amount
                print("please collect cash💵")
                print("remaining balance=",balance)
        elif choice == 4:
            pass
            
            print("\nHelp")
            print("1. check balance")
            print("2. deposit money")
            print("3. withdraw money")
            print("5. exit ATM")

        elif choice == 5:
            print("thank you for visiting")
            break
        else:
            print("invalid choice")

else:
    print("incorrect pin")
    


        