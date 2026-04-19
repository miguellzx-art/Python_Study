distance = int(input("Enter the distance of your trip in kilometers: "))

SHORT_TRIP_RATE = 0.50
LONG_TRIP_RATE  = 0.60
if distance <= 0:
    print("Error: Distance must be greater than zero.")
elif distance <= 200:
    ticket_price = distance * SHORT_TRIP_RATE
    print(f"\nThe price for your {distance} km trip is ${ticket_price:.2f} USD.")
else:
    ticket_price = distance * LONG_TRIP_RATE
    print(f"\nThe price for your {distance} km trip is ${ticket_price:.2f} USD.")

print("Thank you for traveling with us. Have a safe trip!")