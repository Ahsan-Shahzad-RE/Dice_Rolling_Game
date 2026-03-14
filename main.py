# dice rolling game 

import random
print("~~~~~~~~~Welcome to Dice Rolling Game~~~~~~~~~~~")
roll_count = 0 

while True:
    dices = int(input("How many dice you want to roll(1-6)?"))
    if dices < 1 or dices > 6  :
        print("Invalid!")
        continue
    



    result = []

    for i in range (dices):
        roll = random.randint(1,6)
        result.append(roll)

    print(f"You rolled {result} dices.")
    print("Total:", sum(result))

    roll_count += 1

    print(f"Total rolls are {roll_count}")


    again = input("Wanna roll again? (yes/no) :")
    if again.lower() == "no":

        print(f"You rolled {roll_count} times.\nThanks for playing dice rolling game.")
