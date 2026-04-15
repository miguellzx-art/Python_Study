cash = float(input("How much money do you have? $"))

print("\n=== VENDING MACHINE ===")
print("[1] Soda  - $2.50")
print("[2] Chips - $1.75")
print("[3] Candy - $1.25")
print("[4] Gum   - $0.50")

option = int(input("\nWhat would you like to buy? "))

if option == 1:
    price = 2.50
    item = "Soda"
elif option == 2:
    price = 1.75
    item = "Chips"
elif option == 3:
    price = 1.25
    item = "Candy"
elif option == 4:
    price = 0.50
    item = "Gum"
else:
    print("Invalid option.")

if option >= 1 and option <= 4:
    if cash >= price:
        print(f"\nYou bought {item} for ${price:.2f}, enjoy!")
        print(f"Your change: ${cash - price:.2f}")
    else:
        print(f"\nYou don't have enough money to buy {item}.")