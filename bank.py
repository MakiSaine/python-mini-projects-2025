class Menu:
    def __init__(self):
        self.options = [
            "Open a new account",
            "Deposit money into your account",
            "Withdraw money from your account",
            "Add interests to your account",
            "Get the current balance of your account",
            "Quit"
        ]

    def add_option(self, option):
        self.options.append(option)

    def get_input(self):
        print("\nMenu:")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(self.options):
                return choice
            else:
                print("Invalid choice. Try again.")
                return self.get_input()
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.get_input()


class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount:.2f} deposited to your account")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient amount to withdraw.")
        elif amount <= 0:
            print("Withdraw amount must be positive.")
        else:
            self.balance -= amount
            print(f"{amount:.2f} withdrawn from the account.")

    def add_interest(self):
        interest = self.balance * 0.03
        self.balance += interest
        print(f"Interest of {interest:.2f} added to the account.")

    def get_balance(self):
        return self.balance


def main():
    account = None
    menu = Menu()

    while True:
        choice = menu.get_input()

        if choice == 1:
            account = BankAccount()
            print("A new account is opened.")
        elif choice == 2:
            if account:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid input. Enter a numeric value.")
            else:
                 print("Account is not opened!. Please open your account.")
        elif choice == 3:
            if account:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid input. Enter a numeric value.")
            else:
                 print("Account is not opened!. Please open your account.")
        elif choice == 4:
            if account:
                account.add_interest()
            else:
                print("Account is not opened!. Please open your account.")
        elif choice == 5:
            if account:
                print(f"your Current balance is: {account.get_balance():.2f}")
            else:
                print("Account is not opened!. Please open your account.")
        elif choice == 6:
            print("Good Bye!")
            break


if __name__ == "__main__":
    main()
