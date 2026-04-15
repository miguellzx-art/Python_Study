age = int(input("Type your age: "))

print(f"\nYour age is: {age}")
if age < 12:
    print("Category: Child")
elif age < 18:
    print("Category: Teenager")
elif age < 60:
    print("Category: Adult")
else:
    print("Category: Elderly")