import random
Alphabets =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Symbols =['~','!','@','#','$','%','^','&','*','(',')','_','+','<','>',',','?',':','{','}','/','.',';',']','[','=','-']
Numbers = ['0','1','2','3','4','5','6','7','8','9']

def generate_password():
    pass_length = int(input("Specify a length for your password :\n" ))
    print(f"Generating password for {pass_length} characters")

    password_list=[]
    Characters = Alphabets+Symbols+Numbers
    for char in range(0,pass_length):
        password_list += random.choice(Characters)
        code =""
        for char in password_list:
            code += char
    print(f"Your password is : {code}")

generate_password()