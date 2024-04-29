class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = name + "_" + email
        self.transaction_history = []
        self.loan_taken = 0
        self.is_bankrupt = False

    def deposit(self, amount):
        if not self.is_bankrupt:
            self.balance += amount
            self.transaction_history.append(f"{amount} is deposited")
            print("Deposit successful.")
        else:
            print("Bank is bankrupt. Unable to deposit.")

    def withdraw(self, amount):
        if not self.is_bankrupt:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"{amount} is withdrawn")
                print("Withdrawal successful.")
            else:
                print("Withdrawal amount exceeded.")
        else:
            print("Bank is bankrupt. Unable to withdraw.")

    def check_available_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, loan_amount):
        if not self.is_bankrupt:
            if self.loan_taken < 2:
                self.balance += loan_amount
                self.transaction_history.append(loan_amount)
                self.loan_taken += 1
                print("Loan taken successfully.")
            else:
                print("You have already taken maximum number of loans.")
        else:
            print("Bank is bankrupt. Unable to take loan.")

    def transfer_amount(self, amount, other_account):
        if not self.is_bankrupt:
            if self.balance >= amount:
                if other_account.account_number in User.accounts:
                    other_account.deposit(amount)
                    self.balance -= amount
                    self.transaction_history.append(f"{amount} is transferred to {other_account.name}")
                    print("Transfer successful.")
                else:
                    print("Account does not exist.")
            else:
                print("Insufficient balance.")
        else:
            print("Bank is bankrupt. Unable to transfer.")