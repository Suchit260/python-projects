import random

num = int(input("Guess a number between 1 and 6: "))
answer = input("To roll the dice type 'Roll': ")

if answer.lower() == "roll":
    roll = random.randint(1, 6)
    print("You rolled: ",  roll)
    if num == roll:
        print("You Win!!")
    else:
        print("You Lose!!")
else:
    print("Okay get out!!")
