import random
import pandas as pd # The DS engine

all_rolls = [] # We will store every roll here
count = 0

while True:
    a = input("roll the dice(y/n): ").lower()
    if a == "y":
        b = input("how many dice (1 or 2): ")
        
        if b == '1':
            die = random.randint(1, 6)
            print(f"Result: {die}")
            all_rolls.append(die) # Save the data!
            count += 1
            
        elif b == '2':
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f"Results: {die1}, {die2}")
            all_rolls.extend([die1, die2]) # Save both!
            count += 1
        else:
            print("Invalid number of dice.")
            
    elif a == "n":
        print("Thank you for playing!")
        print(f"Total times you rolled: {count}")
        break # Exit the loop
    else:
        print("Invalid option")


if all_rolls:
    
    df = pd.DataFrame(all_rolls, columns=['Die_Value'])
    

    print("\n--- Your Session Statistics ---")
    print(f"Average Roll Value: {df['Die_Value'].mean():.2f}")
    print(f"Most Frequent Number: {df['Die_Value'].mode()[0]}")
    
    
    df.to_csv("my_dice_data.csv", index=False)
    print("Results saved to 'my_dice_data.csv'!")

