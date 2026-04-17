from math import sqrt

opposite = float(input("Enter the length of the opposite side: "))
adjacent = float(input("Enter the length of the adjacent side: "))

hypotenuse = sqrt(opposite ** 2 + adjacent ** 2)

print(f"The opposite side is {opposite:.2f}, the adjacent side is {adjacent:.2f} and the hypotenuse is {hypotenuse:.2f}.")