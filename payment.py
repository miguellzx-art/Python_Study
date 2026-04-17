percentage = int(input("What is the salary increase percentage? "))
current_salary = float(input("What is the employee's current salary? "))

new_salary = current_salary + (current_salary * percentage / 100)

print(f"The employee's new salary is: R${new_salary:.2f}, with a {percentage}% increase from the old salary of R${current_salary:.2f}.")