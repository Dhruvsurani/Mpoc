class Bank:
    def __init__(self):
        self.dp_ammount = False
        self.bank_list = []
        self.accounts_list = {}
        self.transaction_history = []
        self.Bank_created = False
        self.logedin = False

    def create_bank(self, bankname):

        if bankname in self.bank_list:
            print('\nBank is already created')

        else:
            print('\nBank create successfully !')
            self.bank_list.append(bankname)

    def create_account(self,username,pin,amount,bankname,count):
        condtn=True
        if bankname in self.bank_list:
            for accounts in self.accounts_list:
                if self.accounts_list[accounts]['username'] == username and self.accounts_list[accounts]['Bankname'] == bankname:
                    print('User is already created !')
                    condtn = False
                    break
            if condtn:
                account_detail = {}
                print("\nAccount created successfully !")
                account_detail['username'] = username
                account_detail['pin'] = pin
                account_detail['Balance'] = amount
                account_detail['Bankname'] = bankname
                self.accounts_list[count] = account_detail
                self.accounts_list[count]['transactions'] = []

        else:
            print("Entered Bank name is not in Bank List !")

    def account_login(self,username,account_no):
        condition = True
        if account_no in self.accounts_list.keys() and username in self.accounts_list[account_no]['username']:
            self.logedin = True
            print(self.accounts_list[account_no])
        else:
            condition = False
        return condition

    def add_amount(self,amount, account_no):
        deposit_history = {'dp_amount': amount}
        self.accounts_list[account_no]['transactions'].insert(0, deposit_history)
        print(self.accounts_list[account_no])
        self.accounts_list[account_no]['Balance'] += amount
        print(self.accounts_list[account_no]['Balance'])
        print(self.accounts_list[account_no]['transactions'])

    def withdraw_amount(self,amount, account_no):
        withdraw_history = {'wd_amount': amount}
        self.accounts_list[account_no]['transactions'].insert(0, withdraw_history)
        self.accounts_list[account_no]['Balance'] -= amount
        self.wd_amount = True
        print(self.accounts_list[account_no]['Balance'])

    def show_balance(self,account_no):
        print(self.accounts_list[account_no]['Balance'])

    def delete_account(self,account_no,pin):
        if account_no in self.accounts_list.keys() and pin == self.accounts_list[account_no].get('pin'):
            del self.accounts_list[account_no]
            print("Account delete successfully !")
        else:
            print("\nWrong username or pin !")

    def show_transaction(self,account_no):
        if account_no in self.accounts_list:
            while len(self.accounts_list[account_no]['transactions']) > 5:
                self.accounts_list[account_no]['transactions'].pop()
            print(self.accounts_list[account_no]['transactions'])


if __name__ == "__main__":
    Bank_account_object = Bank()
    count = 0
    while True:
        print("\nWelcome to my Bank")
        print("1.Create Bank")
        print("2.Login")
        print("3.Create new Account")
        print("4.Delete Account")
        # print(Bank_account_object.accounts_list)
        user = int(input("Make decision: "))

        if user == 1:
            print("\nCreating new Bank")
            bank_name = input("\nEnter Bank name : ").lower()
            Bank_account_object.create_bank(bank_name)
            print(Bank_account_object.bank_list)

        elif user == 2:
            print("\nEnter User Name, Bank name and PIN for Login !")
            account_no = int(input("Enter your account Number : "))
            username = input("Enter User name : ")
            check = Bank_account_object.account_login(username,account_no)
            if check:

                while True:

                    if Bank_account_object.logedin:
                        print("\n1.Add amount")
                        print("2.Check Balcane")
                        print("3.Withdraw amount")
                        print("4.Show transactions history")
                        print("5.Logout")
                        login_user = int(input())
                        if login_user == 1:
                            print("\nEnter Your Amount ")
                            amount = int(input("Enter Amount : "))
                            Bank_account_object.add_amount(amount, account_no)
                        elif login_user == 2:
                            print("\nYour Bank Balance !")
                            Bank_account_object.show_balance(username)
                        elif login_user == 3:
                            print("\nEnter amount for Withdrawal !")
                            amount = int(input("Enter Amount : "))
                            Bank_account_object.withdraw_amount(amount, account_no)
                        elif login_user == 4:
                            print("Your transaction History !")
                            Bank_account_object.show_transaction(account_no)
                        elif login_user == 5:
                            break

        elif user == 3:
            print("\nPlease Enter details to create new Account.")
            username = input("\nEnter user Name :")
            pin = input("Enter PIN :")
            amount = int(input("Enter amount : "))
            bankname = input("Enter bank name : ")
            count += 1
            print("Your Account Number is : ", count)
            Bank_account_object.create_account(username,pin,amount,bankname,count)

        elif user == 4:
            print("Enter username and PIN for delete Account !")
            account_no = input("Enter your Account No : ")
            pin = input("Enter PIN : ")
            Bank_account_object.delete_account(account_no,pin)
