import random
numbere_to_guess=random.randint(1,100)
while True:
    try:
        a=int(input("guess the number:"))
        if a > numbere_to_guess:
            print("too high")
        elif a< numbere_to_guess:  
            print("too low")
        else:
            print("coreect guess")  
    except ValueError:
        print("invalid value")
    