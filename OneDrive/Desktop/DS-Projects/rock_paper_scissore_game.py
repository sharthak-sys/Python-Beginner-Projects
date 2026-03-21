import random
while True:
 choice=('r','p','s')
 your_choice=input("choose rock paper scizer(r,p,s):")
 computer_choice=random.choice(choice)
 print('you chose:',your_choice)
 print('computer choice:',computer_choice)
 if your_choice not in choice:
        print("invalid choice")
        break
 if computer_choice=='r':
        print("rock")
 elif computer_choice=='s':
        print("scizor")
 elif computer_choice=='p':
        print("paper")
 else :
        print("invalid choice")
    

    

