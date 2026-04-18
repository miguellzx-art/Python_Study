phrase = input("Enter a phrase: ")
count = phrase.count("a")
first = phrase.find("a")
end = phrase.rfind("a")

print(f"The letter 'a' appears {count} times, the first time at position {first} and the last time at position {end}.")