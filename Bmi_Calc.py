weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}", end=" - ")

if bmi < 17.0:
    print("Very underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25.0:
    print("Normal weight")
elif bmi < 30.0:
    print("Overweight")
elif bmi < 35.0:
    print("Obesity")
elif bmi < 40.0:
    print("Severe Obesity")
else:
    print("Morbid Obesity")