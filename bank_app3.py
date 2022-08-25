BANKS = []
customers = []
customer_detail = dict()


class UserAccount:

    def __int__(self):
        print('Welcome to Banking System !')

    def create_bank(self):
        new_bank = input('Enter Bank name :')
        if new_bank.lower() in BANKS:
            print('Bank is already created')
        else:
            BANKS.append(new_bank)
            print('Created Bank successfully !')

    def create_account(self):

        enter_bankname = input('Enter bank name for create bank account :')

        while enter_bankname.lower() in BANKS:


            username = input('Enter user name :')

            pin = int(input('Enter PIN number :'))

            amount = int(input('Enter amount :'))

            count = 0
            for i in BANKS:
                count += 1
                print(f"{count}) {i}")
            bank = input('In which bank do you want to create an account? ')

            while bank.lower() not in BANKS:

                print('Please enter a valid bank name')
                bank = input('In which bank do you want to create an account? ')
            else:
                if len(customers) == 0:
                    customer_detail['username'] = username
                    customer_detail['pin'] = pin
                    customer_detail['amount'] = amount
                    customer_detail['bank_name'] = bank
                    customers.append(customer_detail.copy())

                else:
                    for i in customers:
                        if i['username'] == username and i['bank_name'] == bank:
                            print('Your account is already created')
                            break

                        else:
                            customer_detail['username'] = username
                            customer_detail['pin'] = pin
                            customer_detail['amount'] = amount
                            customer_detail['bank_name'] = bank
                            customers.append(customer_detail.copy())
                            break
            break
        else:
            print('Please Enter valid bank name')
            UserAccount.create_account(self)

    def show_balance(self):
        username = input('Enter your user name :')
        pin = int(input('Enter your PIN :'))

        for i in customers:

            if username == i['username']:
                if pin == i['pin']:
                    print("Your Current Balance:", end=" ")
                    print(i['amount'])

    def withdraw_amount(self):

        username = input('Enter your user name :')

        pin = int(input('Enter your PIN :'))

        for i in customers:
            if username == i['username']:
                if pin == i['pin']:

                    wd_amount = int(input('Enter amount for withdrawal :'))

                    if wd_amount > i['amount']:
                        print('Enter amount is higher then your current amount')

                    else:
                        i['amount'] -= wd_amount
                        print('Your current balance is ', i['amount'])

    def deposit_amount(self):
        username = input('Enter your user name :')
        pin = int(input('Enter your PIN :'))

        for i in customers:

            if username == i['username']:
                if pin == i['pin']:
                    dp_amount = int(input('Enter amount for Deposit :'))
                    if dp_amount < 0:
                        print('Please enter a valid amount')
                    else:
                        i['amount'] += dp_amount
                        print('Your current balance is ', i['amount'])

    def show_bankdetail(self):
        username = input('Enter your user name :')
        pin = int(input('Enter your PIN :'))
        for i in customers:

            if username == i['username']:
                if pin == i['pin']:
                    print('Your user name is : ', i['username'])
                    print('Your PIN is : ', i['pin'])
                    print('Your Balance is : ', i['amount'])
                    print('Your Bank name is : ', i['bank_name'])

    def Bank_accounts(self):
        bank_name = input('Enter bank name :')
        for i in customers:
            if i['bank_name'] == bank_name:
                print(i)

bank = UserAccount()

condition = True

while condition:

    choice = int(input('1) Create Bank \n2) create account \n3) Show account balance \n4) Withdraw amount \n5) '
                       'Deposit amount \n6) Show bank details \n7) Bank accounts \n8) Exit \n'))

    if choice == 1:
        bank.create_bank()
    if choice == 2:
        bank.create_account()

    elif choice == 3:
        bank.show_balance()

    elif choice == 4:
        bank.withdraw_amount()

    elif choice == 5:
        bank.deposit_amount()
    # exit = input('Press E if you want to exit or press enter to continue ')

    elif choice == 6:
        bank.show_bankdetail()

    elif choice == 7:
        bank.Bank_accounts()

    elif choice == 8:
        condition = False
