class Bank:
    account_number = 1000
    def __init__(self,name,age,initial_deposit,account_number):
        self.account_number = account_number
        self.name = name
        self.age = age
        self.initial_deposit = initial_deposit
    def create_account(self):
        print("\t Create Account")
        print("\t ==============")
        name = input("Enter your Name : ")
        valid_age = True
        while valid_age:
            age = int(input("Enter your age : "))
            if age >= 18:
                valid_amount = True
                while valid_amount:
                    initial_deposit = int(input("Enter your Initial Deposit Amount : "))
                    if initial_deposit >= 1000:
                        print(f'Your Account has been Successfully Created with this {Bank.account_number} Account Number')
                        valid_amount = False
                    else:
                        print("Sorry, Your Initial Deposit Amount is valid if and only if it must be greater than or equal to Thousand rupees !")
                user = Bank(name,age,initial_deposit,Bank.account_number)
                store.append(user)
                Bank.account_number += 1
                valid_age = False
            else:
                print("Sorry, you must be at least 18 years old to create a bank account.")
                valid_age = False
    def deposit(self):
        print("\t Deposit Amount")
        print("\t ==============")
        print(f'Name : {self.name}')
        print(f'Balance : {self.initial_deposit}')
        valid_amount = True
        while valid_amount:
            amount = int(input("Enter your Deposit Amount : "))
            if amount > 0:
                self.initial_deposit += amount
                print("Your deposit transaction was completed successfully!")
                print(f'Current Balance : {self.initial_deposit}')
                valid_amount = False
            else:
                print("Enter valid Amount")
    def withdraw(self):
        print("\t Withdraw Amount")
        print("\t ===============")
        print(f'Name : {self.name}')
        print(f'Balance : {self.initial_deposit}')
        valid_amount = True
        while valid_amount:
            amount = int(input("Enter your Withdraw Amount : "))
            if amount > 0 and amount <= self.initial_deposit:
                self.initial_deposit -= amount
                print("Your withdrawal transaction was completed successfully!")
                print(f'Current Balance : {self.initial_deposit}')
                valid_amount = False
            else:
                print("Enter valid Amount")
    def find_account(self,enter_account_number):
        for account in store:
            if account.account_number == enter_account_number:
                return account
        return None
    def view_everyone_accounts(self):
        print("\t View Everyone Account")
        print("\t =====================")
        print("| Name      |     Age   |    Account Number   |   Initial Deposit |")
        for account in store:
            print(f'| {account.name}    | {account.age}       |        {account.account_number}          |   {account.initial_deposit} |')
    def view_particular_account(self):
        print("\t View Particular Account")
        print("\t =======================")
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')
        print(f'Account Number : {self.account_number}')
        print(f'Initial Deposit : {self.initial_deposit}')
store = []
user = Bank("",0,0,0)
repeat = "yes"
while repeat.lower() == "yes":
    print("\t Welcome to SH Bank of India!")
    print("\t ============================")
    print("\t 1. Create Account")
    print("\t 2. Deposit")
    print("\t 3. Withdraw")
    print("\t 4. View Everyone Account")
    print("\t 5. View Particular Account")
    choice = int(input("Enter your choice : "))

    match choice:
        case 1:
            user.create_account()
        case 2:
            acc_number = int(input("Enter your account number : "))
            account = user.find_account(acc_number)
            if account is not None:
                account.deposit()
            else:
                print("Your Account Number does not exist")
        case 3:
            acc_number = int(input("Enter your account number : "))
            account = user.find_account(acc_number)
            if account is not None:
                account.withdraw()
            else:
                print("Your Account Number does not exist")
        case 4:
            user.view_everyone_accounts()
        case 5:
            acc_number = int(input("Enter your account number : "))
            account = user.find_account(acc_number)
            if account is not None:
                account.view_particular_account()
            else:
                print("Your Account Number does not exist")
        case _:
            print("Invalid Choice")
    repeat = input("Do you want to continue ? (yes/no):")
print("Thanks for using SH Bank of India!!")
