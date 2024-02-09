import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")

# user account ke liye class define kiye hai
class Account:
    
    def __init__(self, balance):
        
        self.balance = balance
        self.history = []

   
    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited {amount}")
        logging.info(f"Deposit successful. Your new balance is {self.balance}")

    # paisa withdrawl karne ke liye
    def withdraw(self, amount):
        if amount > self.balance:
            logging.error("Insufficient funds")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew {amount}")
            logging.info(f"Withdrawal successful. Your new balance is {self.balance}")

    # paisa transfer ke liye
    def transfer(self, other, amount):
        if amount > self.balance:
            logging.error("Insufficient funds")
        else:
            self.balance -= amount
            other.balance += amount
            self.history.append(f"Transferred {amount} to {other}")
            other.history.append(f"Received {amount} from {self}")
            logging.info(f"Transfer successful. Your new balance is {self.balance}")

    # balance check ke liye
    def check_balance(self):
        print(f"Your balance is {self.balance}")

    # transaction history dekhne ke liye
    def view_history(self):
        print("Your transaction history:")
        for transaction in self.history:
            print(transaction)

# demo ke liye
account1 = Account(1000)
account2 = Account(500)

# menu show kw liye
def display_menu():
    print("Welcome to the ATM")
    print("Please choose an option:")
    print("1. Transactions History")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Transfer")
    print("5. Quit")

# menu ka function
def execute_choice(choice):
    global account1
    global account2
    if choice == 1:
        account1.view_history()
    elif choice == 2:
        amount = int(input("Enter the amount to withdraw: "))
        account1.withdraw(amount)
    elif choice == 3:
        amount = int(input("Enter the amount to deposit: "))
        account1.deposit(amount)
    elif choice == 4:
        amount = int(input("Enter the amount to transfer: "))
        account1.transfer(account2, amount)
    elif choice == 5:
        print("Thank you for using the ATM")
        quit()
    else:
        print("Invalid choice. Please try again.")

# loop ke liye
while True:
    display_menu()
    choice = int(input("Enter your choice: "))
    execute_choice(choice)
