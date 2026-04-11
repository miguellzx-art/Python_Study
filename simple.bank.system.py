balance = 1000.00
print("=== SIMPLE BANK SYSTEM ===")
print("[1] Check Balance:")
print("[2] Deposit Money:")
print("[3] Withdraw Money:")
print("[4] Exit:")
print("==========================")
option = int(input("Select an option: "))
if option == 1:
    print(f"\nYour balance is ${balance:.2f}")
elif option == 2:
    amount = float(input("Enter the amount to deposit: $"))
    balance += amount
    print(f"You have deposited ${amount:.2f}.")
    print(f"Your new balance is ${balance:.2f}")
elif option == 3:
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > balance:
        print("\nError: Insufficient funds!")
    else:
        balance -= amount
        print(f"\nYou have withdrawn ${amount:.2f}.")
        print(f"Your new balance is ${balance:.2f}")
elif option == 4:
    print("\nThank you for using our Bank System. Goodbye!")
else:
    print("Invalid option. Please select a valid option.")