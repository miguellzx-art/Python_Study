cash = float(input("How much money do you have? "))
print("[1] Soda - $2.50")
print("[2] Chips - $1.75")
print("[3] Candy - $1.25")
print("[4] Gum - $0.50")
option = int(input("What would you like to buy? "))
if option == 1:
    if cash >= 2.50:
        print("You bought a soda, enjoy!")
    else: 
        print("You don't have enough money for a soda.")
elif option == 2:
    if cash >= 1.75:
        print("You bought chips, enjoy!")
    else:
        print("You don't have enough money for chips.")
elif option == 3:
    if cash >= 1.25:
        print("You bought candy, enjoy!")
    else:
        print("You don't have enough money for candy.")
elif option == 4:
    if cash >= 0.50:
        print("You bought gum, enjoy!")
    else:
        print("You don't have enough money for gum.")
else:
    print("Invalid option.")