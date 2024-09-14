import random
name = input( "What is your name?\n")
print("\nHello "+ name+"!!" + "\nWelcome to this Rock, Paper and Scissors Game\nHope You love it! ;)\n")

# list items are ordered in such a way that 1 less index(player_choice) leads to loss
choice =["Scissors","Rock","Paper"]

def result():
    player_choice = int(input('What do you choose?\n"0" for Scissors\n"1" for Rock\n"2" for Paper?\n\n'))
    if player_choice<0 or player_choice >=len(choice):
        print("Choose again\n")
    else:
        print("You chose : " + choice[player_choice])
    
        computer_choice = random.randint(0,2)
        print("Computer chose : " + choice[computer_choice])
        if player_choice == computer_choice:
            print("It's a DRAW!!")
        elif player_choice-computer_choice ==-1:
            print("You lost :( ")
        elif player_choice-computer_choice ==1:
            print("You WON ,Congratulations ;)") 
        elif player_choice-computer_choice ==-2:
            print("You WON ,Congratulations ;) ") 
        else :
            print("You lost :( ")

def play_game():
    while True:
        result()  
        play_again = input("\nDo you want to play again? (Yes/No): ")

        if play_again != 'Yes':
            print("Thanks for playing!")
            break 
play_game()