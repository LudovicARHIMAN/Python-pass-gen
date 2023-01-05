from random import randint

symb=["!","@","?","$","&","#"]





def pass_def_lengh(lenght):
    '''
    This function define the password length 
    '''
    length = int(input("Password lenght ? (At least 12 charateres long)"))
    while length < 12:
        
        print("Password lenght need to be at least 12 charateres")
        length = int(input())
  
    return length



def password_gen(lenght):
    
    lim=pass_def_lengh(lenght)
    
    for i in range(lim):
        print('hello')


