from user import User

class Admin:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.is_active = True
        self.is_bankrupt = False
        self.users = {}

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users[user.account_number] = user
        print("Account created successfully.")

    def delete_account(self, account_number):
        if account_number in self.users:
            del self.users[account_number]
            print("Account deleted successfully.")
        else:
            print("Account not exist.")

    def all_user_accounts_list(self):
        for account_number, user in self.users.items():
            print(f"Account Number: {account_number}, Name: {user.name}, Email: {user.email}, account_type: {user.account_type}")

    def total_available_balance(self):
        total_balance = sum(user.balance for user in self.users.values())
        print("Total Available Balance:", total_balance)

    def total_loan_amount(self):
        total_loan = sum(sum(user.transaction_history) for user in self.users.values() if isinstance(user.transaction_history, list))
        print("Total Loan Amount:", total_loan)

    def change_loan_feature(self, state):
        if state in [True, False]:
            self.is_active = state
            if state:
                print("Loan feature is now active.")
            else:
                print("Loan feature is not active.")
        else:
            print("Invalid Input")

    def change_bankrupt(self, state):
        if state in [True, False]:
            self.is_bankrupt = state
            if state:
                print("Bank declared bankrupt.")
            else:
                print("Bank status is normal.")
        else:
            print("Invalid Input")