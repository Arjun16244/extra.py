print("🍕WELCOME TO PIZZA SHOP🍕")
try:
    quantity = int(input("Enter number of pizzas: "))
    price = float(input("enter the price of 1 pizza:  "))
    total= quantity*price

except ValueError:
    print("please enter numbers only")
else:
    print("total bill is:💵$", total)
    print("\nthank you for your order!😊")
finally:
    print("\nvisit again!")