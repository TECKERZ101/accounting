import datetime
import os

class AccountingSoftware:
    def __init__(self):
        self.transactions = []

    def log_transaction_in(self):
        amount = float(input("Enter the transaction amount: "))
        description = input("Enter the transaction description: ")
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.transactions.append({"type": "In", "amount": amount, "description": description, "date": date})
        self.save_transactions()

    def log_transaction_out(self):
        amount = float(input("Enter the transaction amount: "))
        description = input("Enter the transaction description: ")
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.transactions.append({"type": "Out", "amount": amount, "description": description, "date": date})
        self.save_transactions()

    def set_balance(self):
        balance = float(input("Enter the balance: "))
        self.transactions.append({"type": "Balance", "amount": balance, "description": "Balance Set", "date": datetime.datetime.now().strftime("%Y-%m-%d")})
        self.save_transactions()

    def list_transactions(self):
        for transaction in self.transactions:
            print(f"Type: {transaction['type']}, Amount: {transaction['amount']}, Description: {transaction['description']}, Date: {transaction['date']}")

    def save_transactions(self):
        with open('accounting.txt', 'a') as f:
            for transaction in self.transactions:
                f.write(f"{transaction['type']},{str(transaction['amount'])},{transaction['description']},{transaction['date']}\n")

    def load_transactions(self):
        if os.path.exists('accounting.txt'):
            with open('accounting.txt', 'w') as f:
                lines = f.readlines()
                for line in lines:
                    type, amount, description, date = line.strip().split(',')
                    self.transactions.append({"type": type, "amount": float(amount), "description": description, "date": date})

    def current_balance(self):
        total = 0
        for transaction in self.transactions:
            if transaction["type"] == "Balance":
                total = transaction["amount"]
            elif transaction["type"] == "In":
                total += transaction["amount"]
            elif transaction["type"] == "Out":
                total -= transaction["amount"]
        return total


def main():
    software = AccountingSoftware()
    while True:
        software.load_transactions()
        print("\nAccounting Software\n1. Log Transaction In\n2. Log Transaction Out\n3. Set Balance\n4. List Transactions\n5. Current Balance\n6. Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            software.log_transaction_in()
        elif choice == 2:
            software.log_transaction_out()
        elif choice == 3:
            software.set_balance()
        elif choice == 4:
            software.list_transactions()
        elif choice == 5:
            print(f"Current Balance: {software.current_balance()}")
        elif choice == 6:
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
