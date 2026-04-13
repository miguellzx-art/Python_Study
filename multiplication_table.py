number = int(input("Which number do you want to see the multiplication table for? "))
count = 1

print(f"\nMultiplication table for {number}:")

while count <= 10:
    result = number * count
    print(f"{number} x {count} = {result}")
    count += 1