import os

while True:
    print("\n" + "="*20)
    print("CALCULATOR")
    print("="*20)
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Exit")
    
    option = input("\nChoose an option: ")

    if option == '5':
        print("Closing calculator... See you later!")
        break 
    
    if option in ['1', '2', '3', '4']:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))

        if option == '1':
            result = n1 + n2
            print(f"\nResult: {n1} + {n2} = {result}")
        
        elif option == '2':
            result = n1 - n2
            print(f"\nResult: {n1} - {n2} = {result}")
            
        elif option == '3':
            result = n1 * n2
            print(f"\nResult: {n1} * {n2} = {result}")
            
        elif option == '4':
            if n2 == 0:
                print("\n[ERROR] Division by zero is not allowed!")
            else:
                result = n1 / n2
                print(f"\nResult: {n1} / {n2} = {result}")
    else:
        print("\n[ERROR] Invalid option! Please try again.")

    input("\nPress Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')