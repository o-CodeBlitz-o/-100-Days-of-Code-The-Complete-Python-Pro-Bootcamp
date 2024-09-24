import random

def Deal_Card():
    Cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    Card = random.choice(Cards)
    return Card

def Calculate_Score(Cards):
    if sum == 21 and len(Cards)== 2:
        return 0
    if 11 in Cards and sum(Cards)>21:
        Cards.remove(11)
        Cards.append(1)
    return sum(Cards)

def Compare(U_Score,C_Score):
    if U_Score == C_Score:
        return "It's a DRAW!!"
    elif C_Score == 0:
        return "You LOSE \nOpponent has a BlackJack!!"
    elif U_Score == 0:
        return "You WON \nIt's a BlackJack!!"
    elif U_Score > 21:
        return "You went over \nYou LOSE"
    elif C_Score > 21:
        return "Opponent went over \nYou WON!!"
    elif U_Score > C_Score:
        return "You WON!!"
    else:
        return "You LOSE"
        
def Play_Game():
    User_Cards = []
    Computer_Cards = []
    User_Score = -1
    Computer_Score = -1
    Is_Game_Over = False
    
    for Num in range(2):
        User_Cards.append(Deal_Card())
        Computer_Cards.append(Deal_Card())
    while not Is_Game_Over :    
        User_Score = Calculate_Score(User_Cards)
        Computer_Score = Calculate_Score(Computer_Cards)
        print(f" Your Cards : {User_Cards} , Current Score = {User_Score}")
        print(f"Computer's First Cards : {Computer_Cards[0]}")
        
        if User_Score == 0 or Computer_Score == 0 or User_Score > 21:
            Is_Game_Over = True
        else:
            User_should_deal = input("Type 'Y' to DRAW ANOTHER card, Type 'N' to PASS").upper()
            if User_should_deal == 'Y':
                User_Cards.append(Deal_card())
            else:
                Is_Game_Over = True
                
    while Computer_Score != 0 and Computer_Score < 17:
        Computer_Cards.append(Deal_Cards())
        Computer_Score = Calculate_Score(Computer_Cards)
    
    print(f"Your Final hand : {User_Cards}, Final Score : {User_Score}")
    print(f"Opponent's Final hand : {Computer_Cards}, Opponent's Final Score : {Computer_Score}")
    print(Compare(User_Score,Computer_Score))

while (input("Do you want to Play a game of BlackJack?\nType 'Y' for Yes or 'N' for No").upper())== 'Y':
    print("\n"*50)
    Play_Game()
    
