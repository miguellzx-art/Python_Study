number = input("Enter a number: ").strip()

if not number.isdigit():
    print("Please enter a valid number.")

number = number.zfill(4)

thousand = number[0]
hundred = number[1]
tens = number[2]
units = number[3]

if number <= "9999":
    print(f"Thousand: {thousand}")
    print(f"Hundred: {hundred}")
    print(f"Tens: {tens}")
    print(f"Units: {units}")
else:
    print("Please enter a number less than or equal to 9999.")