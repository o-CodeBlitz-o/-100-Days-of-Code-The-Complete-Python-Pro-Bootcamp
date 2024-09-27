import random
from GameData import data

def Format_Data(Account):
    Account_Name = Account["name"]
    Account_Descr = Account["description"]
    Account_Country = Account["country"]
    return (f"{Account_Name}, a {Account_Descr}, from {Account_Country}")

def Check(User_Guess,Follower_A,Follower_B):
        if Follower_A > Follower_B :
            return User_Guess == "A"
        else :
            return User_Guess == "B"

Account_A = random.choice(data)
Account_B = random.choice(data)
if Account_A == Account_B:
    Account_B =  random.choice(data)

Name = input("What is your name?\n")
print(f"\nHello {Name}!!"+"\nWelcome to Higher Lower Game")

print(f"Compare A against B :\n{Format_Data(Account_A)}\n\nVS\n\n{Format_Data(Account_B)}")
Guess = input("Which one of these has MORE FOLLOWER COUNT? \n Type A or B : ").upper()

A_Follower_Count = ["follower_count"]
B_Follower_Count = ["follower_count"]
