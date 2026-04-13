# prime_number_checker.py
# Checks if a number is prime

number = int(input("Enter a number: "))
cont = 1
contdiv = 0

while cont <= number:
    print(cont, end=" ")
    if number % cont == 0:
        contdiv += 1
    cont += 1

if contdiv > 2:
    print(f"\n{number} is not a prime number.")
else:
    print(f"\n{number} is a prime number.")