import random

print("\n \nWelcome to #--WHOSE WALLET--#\n")
print("You will give me a list of names, and I will pick a person to pay 😱")
names = input("if you're ready, enter the names separated by a comma: ")

name_list = names.split(", ")
randPerson = random.randint(0, len(name_list)-1)
picked = name_list[randPerson]


print(f"\n \nplease ask {picked} to take her/his wallet out. Dinner is on her/him 🤑\n")