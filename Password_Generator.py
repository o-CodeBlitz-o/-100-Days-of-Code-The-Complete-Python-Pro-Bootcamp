import random
Alphabets =[]
for i in range(65,123):
        if (i >=91 and i<=96):
                continue
        Alphabets.append(chr(i))
Symbols =['~','!','@','#','$','%','^','&','*','(',')','_','+','<','>',',','?',':','{','}','/','.',';',']','[','=','-']
Numbers = ['0','1','2','3','4','5','6','7','8','9']

def generate_password():
    pass_length = int(input("Specify a length for your password :\n" ))
    print(f"Generating password for {pass_length} characters")

    password_list=""
    Characters = Alphabets+Symbols+Numbers
    for char in range(0,pass_length):
        password_list += random.choice(Characters)
        code =""
        for char in password_list:
            code += char
    print(f"Your password is : {code}")

generate_password()
