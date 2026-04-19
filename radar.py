speed = int(input("Enter the vehicle's speed when passing the radar (km/h): "))

if speed > 80:
    print("You have been fined for exceeding the speed limit!")
    fine_amount = (speed - 80) * 7
    print(f"Fine amount: R${fine_amount:.2f}")
else:
    print("You are within the speed limit. Drive safely and have a great day!")