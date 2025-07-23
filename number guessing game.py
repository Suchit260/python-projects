import random

num = int(input("Give a number from 1 - 10:  "))
number = random.randint(1, 10)
if num == number:
    print(number)
    print("You Win")
else:
    print(number)
    print("You Lose")
