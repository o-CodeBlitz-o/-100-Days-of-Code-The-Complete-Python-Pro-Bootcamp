def Highest_bidder(Bid_Sequence):
    winner = max(Bid_Sequence,key=Bid_Sequence.get)

    print(f"The winner is {winner} with the highest bid of Rs. {Bid}")

Bid_Sequence ={}
continue_bidding=True
while continue_bidding:
    Name = input("What is your name?\n")
    print("\nHello "+ Name +"!!"+"\nWelcome to the Auction!!")

    Bid= int(input("Place your Bid Price: Rs. "))
    Bid_Sequence[Name]=Bid
    Continuation= input("Are there anymore Bidders?\nType 'yes' or 'no'. \n").lower()
    if Continuation=="no":
        continue_bidding=False
        Highest_bidder(Bid_Sequence)
    elif Continuation=="yes":
        print("\n"*50)
