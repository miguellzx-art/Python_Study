number = input("Digite um número: ").strip()
if not number.isdigit():
    print("Digite um número válido.")
number = number.zfill(4)
milhar = number[0]
centena = number[1]
dezena = number[2]
unidade = number[3]
if number <= "9999":
    print(f"milhar: {milhar}")
    print(f"centena: {centena}")
    print(f"dezena: {dezena}")
    print(f"unidade: {unidade}")