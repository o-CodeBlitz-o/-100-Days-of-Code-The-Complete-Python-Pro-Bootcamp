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

for Num in range(2):
    User_Cards.append(Deal_Card())
    Computer_Cards.append(Deal_Card())

Calculate_Score()


