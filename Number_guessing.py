import random
secret_number = random.randint(1, 50)
attempts = 0
while True:
    guess = int(input("Type a number between 1 and 50: "))
    if guess <1 or guess > 50:
        box = input("Invalid option. Do you want to try again? [Yes/No]: ")
        if box.lower() == "no":
            break
        else:
            continue
    attempts += 1
    if guess < secret_number:
        print("Too Low! Try again.")
    elif guess > secret_number:
        print("Too High! Try again.")
    else:
        print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
        break