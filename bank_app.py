class Bank:
    def __init__(self):
        self.bank_list = []
        self.accounts_list = {}
        self.Bank_created = False
        self.account_created = False
        self.logedin = False
        self.dp_ammount = False
        self.wd_amount = False

    def create_bank(self ,bankname):
        conditions = True
        if bankname in self.bank_list:
            print('\nBank is already created')
            conditions = False

        if conditions:
            print('\nBank create successfully !')
            self.bank_list.append(bankname)
            self.Bank_created = True

    def create_account(self,username,pin,amount,bankname):
        conditions = True

        if len(pin) > 4:
            print("\nPIN length attlist 4 !")
            conditions = False
        if conditions:

            account_detail = {}
            print("\nAccount created successfully !")
            account_detail['username'] = username
            account_detail['pin'] = pin
            account_detail['Balance'] = amount
            account_detail['Bankname'] = bankname
            self.accounts_list[username] = account_detail
            self.account_created = True

    def account_login(self,username,pin):
        if username in self.accounts_list.keys() and pin == self.accounts_list[username].get('pin'):
            self.logedin = True
            # print(self.accounts_list)
            print(self.accounts_list[username])
        else:
            print("\nWrong username or password")
            self.logedin = False

    def add_amount(self,usename,amount):

        self.accounts_list[usename]['Balance'] += amount
        self.dp_ammount = True
        # print(self.accounts_list)
        print(self.accounts_list[username]['Balance'])

    def withdraw_amount(self,username,amount):
        self.accounts_list[username]['Balance'] -= amount
        self.wd_amount = True
        # print(self.accounts_list)
        print(self.accounts_list[username]['Balance'])

    def show_balance(self,username):
        print(self.accounts_list[username]['Balance'])


if __name__ == "__main__":
    Bank_account_object = Bank()
    while True:
        print("\nWelcome to my Bank")
        print("1.Create Bank")
        print("2.Login")
        print("3.Create new Account")
        user = int(input("Make decision: "))

        if user == 1:
            print("\nCreating new Bank")
            bank_name = input("\nEnter Bank name : ")
            Bank_account_object.create_bank(bank_name)
            print(Bank_account_object.bank_list)

        if user == 2:
            print("\nEnter User Name and PIN for Login !")
            username = input("Enter User name : ")
            pin = input("Enter PIN number : ")
            Bank_account_object.account_login(username,pin)
            while True:
                if Bank_account_object.logedin:
                    print("\n1.Add amount")
                    print("2.Check Balcane")
                    print("3.Withdraw amount")
                    print("4.Logout")
                    login_user = int(input())
                    if login_user == 1:
                        print("\nEnter Your Amount ")
                        amount = int(input("Enter Amount : "))
                        Bank_account_object.add_amount(username,amount)
                    elif login_user == 2:
                        print("\nYour Bank Balance !")
                        Bank_account_object.show_balance(username)
                    elif login_user == 3:
                        print("\nEnter amount for Withdrawal !")
                        amount = int(input("Enter Amount : "))
                        Bank_account_object.withdraw_amount(username,amount)
                    elif login_user == 4:
                        break


        if user == 3:
            print("\nPlease Enter details to create new Account.")
            username = input("\nEnter user Name :")
            pin = input("Enter PIN :")
            amount = int(input("Enter amount : "))
            bankname = input("Enter bank name : ")
            Bank_account_object.create_account(username,pin,amount,bankname)
            # print(Bank_account_object.accounts_list)

            while True:
                if Bank_account_object.account_created:
                    print("\n1.Add amount")
                    print("2.Check Balcane")
                    print("3.Withdraw amount")
                    print("4.Logout")
                    created_user = int(input())
                    if created_user == 1:
                        print("Enter Your Amount ")
                        amount = int(input("Enter Amount : "))
                        Bank_account_object.add_amount(username,amount)
                    if created_user == 2:
                        print("\nYour Bank Balance !")
                        Bank_account_object.show_balance(username)
                    if created_user == 3:
                        print("\nEnter amount for Withdrawal !")
                        amount = int(input("Enter Amount : "))
                        Bank_account_object.withdraw_amount(username,amount)
                    if created_user == 4:
                        break

