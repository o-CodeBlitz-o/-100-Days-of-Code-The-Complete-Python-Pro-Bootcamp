import random

print("Welcome to the Number Guessing Game :)")
print("I'm thinking of a number between 1 to 100")

Num = []
for i in range(1,101):
    Num.append(int(i))

Chosen_Number = random.choice(Num)

Player_Guess = int(input("What's your Guess : "))

def Compare():
    if Player_Guess == Chosen_Number:
        return "Congratulations!! You guessed the right Number ;)"
    elif Player_Guess > Chosen_Number:
        return "Too High, Try Again :/"
    else:
        return "Too Low,Try Again :/"

def Mode():
    Difficulty = (input("Choose a Difficulty : EASY or HARD :").upper())
    if Difficulty == "HARD" :
        while Number_of_Attempts >= 1:
            Number_of_Attempts = 5
            Compare()
            Number_of_Attempts -= Number_of_Attempts
            print(f"You have {Number_of_Attempts} attempts left to guess the number")
    else:
        while Number_of_Attempts >= 1:
            Number_of_Attempts = 10
            Compare()
            Number_of_Attempts -= Number_of_Attempts
            print(f"You have {Number_of_Attempts} attempts left to guess the number")

Mode()