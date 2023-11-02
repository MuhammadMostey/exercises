import random


print("Welcome to the Challenging Computer gussing Game, you can challenge the computer what number can guess?")

random_Pc_number = random.randint(0, 9999)
random_formated_four_digits = str(random_Pc_number).zfill(4)





print(random_formated_four_digits)
print('\n')

user_guess = input("Enter 4 digit number: ")


print('\n')



def randomNumChecker():
    if (user_guess == random_formated_four_digits):
        print("Awsome! Your PIN code did match.")
        print(f"The Computer generated this code {random_formated_four_digits}")
    else:
        print("Failure! Your PIN code did not match.")
        print(f"The Computer generated this code {random_formated_four_digits}")




if ( len(user_guess) != 4):
    print("Try again! Please Enter 4 digit number")
else:
    randomNumChecker()
