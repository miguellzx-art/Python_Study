from datetime import date

year = int(input("Enter a year to check if it's a leap year (enter 0 for current year): "))

if year == 0:
    year = date.today().year

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")