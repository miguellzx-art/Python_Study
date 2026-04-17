from math import sqrt

opposite = float(input("Enter the length of the opposite cathetus (m): "))
adjacent = float(input("Enter the length of the adjacent cathetus (m): "))

hypotenuse = sqrt(opposite ** 2 + adjacent ** 2)

print(f"Opposite cathetus: {opposite:.2f} m")
print(f"Adjacent cathetus: {adjacent:.2f} m")
print(f"Hypotenuse: {hypotenuse:.2f} m")