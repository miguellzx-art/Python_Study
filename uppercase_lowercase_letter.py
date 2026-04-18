name = input("Enter your full name: ").strip()

uppercase_name = name.upper()
lowercase_name = name.lower()
total_letters = len(name.replace(" ", ""))
first_name_letters = len(name.split()[0])

print(uppercase_name)
print(lowercase_name)
print(total_letters)
print(first_name_letters)