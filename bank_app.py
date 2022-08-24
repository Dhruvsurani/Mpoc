users = []
accounts = {}
class BankSystem:
    def __init__(self):
        """
        cust_name is the name of customer 
        balance is customer account balance 
        Mobile number for contact with customer for any query
        PIN number is account pin number
        """
        self.cust_name = input('Enter user name :')
        self.balance = float(input('Enter amount :'))
        self.mobile_no = int(input('Enter mobile number :'))
        self.pin = int(input('Enter PIN :'))

        accounts['username'] = self.cust_name
        accounts['balance'] = self.balance
        accounts['mobile_no'] = self.mobile_no
        accounts['pin'] = self.pin

        users.append(accounts)
    def account_detail(self):
        
        print('Customer name is :',self.cust_name,'\nAccount balance is :',
        self.balance,'\nMobile number is :',self.mobile_no,'\nPIN is :',self.pin)

    def deposit_amount(self):
        dp = float(input('Enter the amount for deposit:'))
        self.balance += dp
        for i in users:
            i['balance']=self.balance
        

    def withdraw_amount(self):
        pin_no = int(input('Enter your pin number :'))

        for i in users:
            while i['pin']!=pin_no:
                print('Enter valid pin number')
                pin_no = int(input('Enter your pin number :'))
            else:
                wa = int(input('Enter amount :'))
                if self.balance >= wa:
                    self.balance -= wa
                else:
                    print('you balance is :',self.balance,'please enter valid ammount for withdrawl')
                for i in users:
                    i['balance']=self.balance
                



class option(BankSystem):
    def __init__(self):
        super().__init__()
    
    def options(self):
        number = int(input('1) Show account detail \n2) Show account balance \n3) Widrow amount \n4) Deposit amount \n'))
        if number == 1:
            print(self.account_detail()) 
        elif number == 2:
            print(self.balance) 
        elif number == 3:
            print(self.withdraw_amount())
            print('Available balance :',self.balance)
        else:
            print(self.deposit_amount())
            print('Available balance :',self.balance)

customer1 = option()

customer1.options()
print(users)