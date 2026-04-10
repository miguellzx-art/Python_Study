print("[1] Expresso: $5.00")
print("[2] Capuccino: $8.00")
print("[3] Iced Latte: $10.00")
option = int(input("Choose your coffee: "))
if option == 1:
    coffee = "Expresso"
    price = 5.00
    extra_sugar = input("Do you want extra sugar? (yes/no): ")
    if extra_sugar == "yes":
        price = price + 1.00
elif option == 2:
    coffee = "Capuccino"
    price = 8.00
    extra_sugar = input("Do you want extra sugar? (yes/no): ")
    if extra_sugar == "yes":
        price = price + 1.00
elif option == 3:
    coffee = "Iced Latte"
    price = 10.00
    extra_sugar = input("Do you want extra sugar? (yes/no): ")
    if extra_sugar == "yes":
        price = price + 1.00
else:
    print("Invalid Option")
if option in [1, 2, 3]:
    print(f"You have ordered {coffee} with a total price of ${price:.2f}")
    print("Thank you for your order!")
