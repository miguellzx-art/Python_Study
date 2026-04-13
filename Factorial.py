number = int(input("Enter a number: "))
factorial = 1
count = number

while count >= 1:
    print(count, "x", end=" ")
    factorial *= count
    count -= 1

print(f"\nThe factorial of {number} is equal to {factorial}")