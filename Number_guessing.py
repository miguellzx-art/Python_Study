import random
secret_number = random.randint(1, 50)
while True:
    guess = int(input("Type a number between 1 and 50: "))
    if guess < secret_number:
            print("Too low, try again.")
    elif guess > secret_number:
            print("Too high, try again.")
    else:
            print("Congratulations! You guessed the number.")
            break