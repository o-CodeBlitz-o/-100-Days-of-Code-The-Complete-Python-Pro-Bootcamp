Alphabets =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Name = input("What is your name?\n")
print("\nHello "+ Name +"!!"+"\nWelcome to Caesar Cypher/Decypher")

Function=input("Type 'ENCODE' to encrypt/'DECODE' to decrypt message :\n").upper()

def cypher(original_text,shift,encode_decode):
        output_text=""
        if encode_decode == "DECODE":
                shift*=-1
            
        for letter in original_text:
            shifted_position=Alphabets.index(letter)+shift
            shifted_position%= len(Alphabets)
            output_text+=Alphabets[shifted_position]
        print(f"Encoded Text : {output_text}")
if Function!= "ENCODE" and Function!="DECODE":
    print("Oops Something went wrong :(\nPlease try again ")
else :

    message= input("Type the message you want to cypher :\n")
    key=int(input("How much SHIFT do you want/encryption key or decryption key? \n"))
    cypher(original_text=message,shift=key,encode_decode=Function)


            

    