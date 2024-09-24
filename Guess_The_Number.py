from random import randint

Chosen_Number = randint(1,100)
HARD_TURN = 5
EASY_TURN = 10

Player_Guess = int(input("What's your Guess : "))

def Compare(P_Guess,C_Number):
    if P_Guess == C_Number:
        return "Congratulations!! You guessed the right Number ;)"
    elif P_Guess > C_Number:
        return "Too High, Try Again :/"
    else:
        return "Too Low,Try Again :/"

def Mode():
    Difficulty = (input("Choose a Difficulty : EASY or HARD :").upper())
    if Difficulty == "HARD" :
        return HARD_TURN
    elif Difficulty == "EASY" :
        return EASY_TURN
    else :
        print("Wrong Input")


print("Welcome to the Number Guessing Game :)")
print("I'm thinking of a number between 1 to 100")
turns = Mode()
print(f"You have {turns} attempts left")
Player_Guess = int(input("What's your Guess : "))

Compare(P_Guess=Player_Guess,C_Number=Chosen_Number)
