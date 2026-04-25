number = int(input("Which number do you want to see the multiplication table for? "))
count = 1

print(f"\nMultiplication table for {number}:")

while count <= 10:
    if number <= 0:
        print("The number must be positive.")
        break
    result = number * count
    print(f"{number} x {count} = {result}")
    count += 1
