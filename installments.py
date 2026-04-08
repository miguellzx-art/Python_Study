value = 1000
interest_rate = 0.20
total = value + (value * interest_rate)
installments = int(input(f"how many installments do you want to divide? "))
if installments <= 0:
    print("Invalid number of installments!")
installment_value = total / installments
print(f"The value with interest is: R${total:.2f}")
print(f"The value of each installment is: R${installment_value:.2f}")
