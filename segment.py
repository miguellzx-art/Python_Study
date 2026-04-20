r1 = float(input("Enter the first segment: "))
r2 = float(input("Enter the second segment: "))
r3 = float(input("Enter the third segment: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("The segments can form a triangle!")
else:
    print("The segments cannot form a triangle!")