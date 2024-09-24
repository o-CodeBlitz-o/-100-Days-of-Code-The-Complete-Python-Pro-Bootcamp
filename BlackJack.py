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

User_Cards = []
Computer_Cards = []
Is_Game_Over = False

for Num in range(2):
    User_Cards.append(Deal_Card())
    Computer_Cards.append(Deal_Card())
    
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
