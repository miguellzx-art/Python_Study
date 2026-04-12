print("=== MULTIPLE CURRENCY CONVERTER (BRL → USD) ===\n")
conversions = int(input("How many conversions do you want to make? "))
count = 1
while count <= conversions:
    print(f"\nConversion {count} of {conversions}")
    reais = float(input("How many Brazilian Reais do you have? "))
    usd_rate = 5.12
    dollars = reais / usd_rate
    print(f"You have: R$ {reais:.2f}")
    print(f"You can buy: US$ {dollars:.2f}")
    print(f"The current exchange rate is: {usd_rate:.2f} BRL per 1 USD")
    count += 1
print("\n============================================")
print("Thank you for using the Currency Converter!")
print("============================================")