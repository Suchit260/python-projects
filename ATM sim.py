balance = int(input("Enter your balance: "))


while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        quant = int(input("How much you wanna deposit? "))
        balance += quant
        print(f"New Balance: {balance}")
    elif choice == "2":
        quant2 = int(input("How much you wanna withdraw? "))
        if quant2 > balance:
            print("Insufficient funds")
        else:
            print(f"New Balance: {balance - quant2}")

    else:
        break



