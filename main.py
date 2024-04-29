from user import User
from admin import Admin

def user_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    account_type = input("Enter your account type: ")
    user = User(name, email, address, account_type)

    while True:
        print(f"Welcome {user.name}!!!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Take Loan")
        print("4. Transfer Amount")
        print("5. Check Balance")
        print("6. Check Transaction History")
        print("7. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            user.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(amount)
        elif choice == 3:
            loan_amount = float(input("Enter loan amount: "))
            user.take_loan(loan_amount)
        elif choice == 4:
            receiver_account_number = input("Enter receiver's account number: ")
            amount = float(input("Enter amount to transfer: "))
            receiver = User.users.get(receiver_account_number)
            if receiver:
                user.transfer_amount(amount, receiver)
            else:
                print("Receiver account not found.")
        elif choice == 5:
            print("Available balance:", user.check_available_balance())
        elif choice == 6:
            print("Transaction history:", user.check_transaction_history())
        elif choice == 7:
            break
        else:
            print("Invalid Input")

def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    admin = Admin(name, email, address)

    while True:
        print(f"Welcome {admin.name}!!!")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View All User Accounts")
        print("4. Total Available Balance")
        print("5. Total Loan Amount")
        print("6. Change Loan Feature")
        print("7. Change Bankrupt Status")
        print("8. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            account_type = input("Enter user's account type: ")
            admin.create_account(name, email, address, account_type)
        elif choice == 2:
            account_number = input("Enter account number to delete: ")
            admin.delete_account(account_number)
        elif choice == 3:
            admin.all_user_accounts_list()
        elif choice == 4:
            admin.total_available_balance()
        elif choice == 5:
            admin.total_loan_amount()
        elif choice == 6:
            state = input("Enter new state (True/False): ").lower() == 'true'
            admin.change_loan_feature(state)
        elif choice == 7:
            state = input("Enter new state (True/False): ").lower() == 'true'
            admin.change_bankrupt(state)
        elif choice == 8:
            break
        else:
            print("Invalid Input")

while True:
    print("Welcome!!")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        user_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("INVALID INPUT")
