class Bankacc:
    def __init__(self, acc_number, owner_name, balance):
        self.acc_number = acc_number
        self.ower_name = owner_name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            "Insufficient funds"
        
    def show_balance(self):
        print("Your balance: " + str(self.balance))



class Savings(Bankacc):
    def __init__(self, acc_number, owner_name, balance, interest_rate):
        super().__init__(acc_number, owner_name, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        cal_interest = self.balance * self.interest_rate / 100
        self.balance += cal_interest
        print(f"Updated balance: {self.balance}")


class BankManager:
    def __init__(self):
        self.accounts = []

    def create_acc(self):
        choice = input("Enter 1 for Normal, 2 for Savings: ")
        acc_number = input("Enter account number: ")
        owner_name = input("Enter owner name: ")
        balance = float(input("Enter starting balance: "))

        if choice == "1":
            account = Bankacc(acc_number, owner_name, balance)
        elif choice == "2":
            interest_rate = float(input("Enter interest rate: "))
            account = Savings(acc_number, owner_name, balance, interest_rate)
        else:
            print("Invalid choice")
            return

        self.accounts.append(account)  # ✅ save it
        print("Account created successfully!")

    def find_acc(self, acc_number):
        for acc in self.accounts:
            if acc.acc_number == acc_number:  # ✅ correct comparison
                return acc
        return None

        
        

manager = BankManager()

while True:
    print("\n--- Bank Menu ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Balance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        manager.create_acc()

    elif choice == "2":
        acc_num = input("Enter account number: ")
        acc = manager.find_acc(acc_num)
        if acc:
            amount = float(input("Enter amount to deposit: "))
            acc.deposit(amount)
            print("Deposit successful!")
        else:
            print("Account not found.")

    elif choice == "3":
        acc_num = input("Enter account number: ")
        acc = manager.find_acc(acc_num)
        if acc:
            amount = float(input("Enter amount to withdraw: "))
            acc.withdraw(amount)
            print("Withdraw successful!")
        else:
            print("Account not found.")

    elif choice == "4":
        acc_num = input("Enter account number: ")
        acc = manager.find_acc(acc_num)
        if acc:
            acc.show_balance()
        else:
            print("Account not found.")
    else:
        break
