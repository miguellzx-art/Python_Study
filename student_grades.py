grade1 = float(input("Enter First Grade: "))
grade2 = float(input("Enter Second Grade: "))
average = (grade1 + grade2) / 2
print(f"Your Average Grade is: {average:.1f}")
if average >= 7.0:
    print("Congratulations! You passed.")
elif average >= 5.0 and average < 7.0:
     print("You are in the recovery phase.")
else:
    print("Unfortunately, you failed.")
