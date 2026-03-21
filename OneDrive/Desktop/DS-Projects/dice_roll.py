#loop
#ask the user 
#if user enters y 
#generate twom random number 
#print them
#if user enters n
#print thank you message 
#terminate 
#else
#print invalide choice
import random
count=0
while True:
    a=input("roll the dice(y/n):").lower()
    if a == "y" :
        b=input("how many dies:")
        if b=='1' :
            die1=random.randint(1,6)
            print(f'{die1}')
        if b=='2':
            die3=random.randint(1,6)
            die2=random.randint(1,6)
            print(f'{die3},{die2}')
            count+=1n
        else:
            print('ynot enough dies')
            
    elif a == "n":
            print("thank you for playing ")
            print("times roll dies:",count)
    else:
        print("invalid option")
    