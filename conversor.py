reais = float(input("How many Brazilian Reais do you have? "))
usd_rate = 5.12
dollars = reais / usd_rate
print(f"You have: R$ {reais:.2f}")
print(f"You can buy: US$ {dollars:.2f}")