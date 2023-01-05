import random
import pyperclip


symb=["!","@","?","$","&","#"]


def pass_def_lengh():
    '''
    This function define the password length 
    '''
    length = int(input("Password lenght ? (At least 12 charateres long)"))
    while length < 12:
        
        print("Password lenght need to be at least 12 charateres")
        length = int(input())
  
    return length


def random_choice():
    '''
    Make random choice between Uppercase, Lowercase, Integer and symbols
    '''
    ch=random.randint(1,4)

    if ch == 1:
        randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
        return randomLowerLetter

    if ch == 2: 
        randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
        return randomUpperLetter

    if ch == 3:
        randomInteger= random.randint(0,9)
        return str(randomInteger)

    if ch == 4:
        randomSymb= (random.choice(symb))
        return randomSymb      

def list_to_str(list):
    passwd= " ".join(str(x) for x in list)
    
    return passwd.replace(" ","")


def password_gen():
    '''
    Main function make random password 
    '''
    password=[]

    lim=pass_def_lengh()
    
    
    for i in range(0,lim):
        password.insert(0,random_choice())
    
    
    passSTR=list_to_str(password)

    return pyperclip.copy(list_to_str(password))

print(password_gen())



