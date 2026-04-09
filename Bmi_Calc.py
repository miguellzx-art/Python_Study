weight = float(input("Enter your weight in kg: " ))
height = float(input("Enter your height in m: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")
if (bmi >= 18.5) and (bmi < 25):
    print("You are in the normal weight range.")
else:
    print("You are outside the normal weight range.")