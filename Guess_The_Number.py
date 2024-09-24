from random import randint

HARD_TURN = 5
EASY_TURN = 10

def Compare(P_Guess,C_Number):
    if P_Guess == C_Number:
        print( "Congratulations!! You guessed the right Number ;)")
    elif P_Guess > C_Number:
        print( "Too High, Try Again :/")
        return turns - 1
    else:
        print( "Too Low,Try Again :/")
        return turns - 1

def Mode():
    Difficulty = (input("Choose a Difficulty : EASY or HARD :").upper())
    if Difficulty == "HARD" :
        return HARD_TURN
    elif Difficulty == "EASY" :
        return EASY_TURN
    else :
        print("Wrong Input")
        exit()

def Game():
    print("Welcome to the Number Guessing Game :)")
    print("I'm thinking of a number between 1 to 100")
    Chosen_Number = randint(1,100)
    turns = Mode()
    
    Player_Guess = 0
    while Player_Guess != Chosen_Number:
        print(f"You have {turns} attempts left")
        Player_Guess = int(input("What's your Guess : "))
        turns = Compare(Player_Guess,Chosen_Number,turns)
        if turns == 0:
            print("You've run out of guesses :/ ")
            return
        elif Player_Guess != Chosen_Number:
            print("Guess Again.")

Game()
