try:
    
    user_age=int(input("Enter your age:  "))
    if user_age%2==0:
       print("the age is an even number")

    else:
        print("the age is an odd number")

except ValueError:
    print("please enter a whole number only")
