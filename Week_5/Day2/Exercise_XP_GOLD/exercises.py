# Exercise 1: Bank Account

class BankAccount:
    def __init__(self,username, password, balance, authenticated=False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authentification = authenticated

    def authenticated(self, username, password):
        if self.username == username and self.password == password:
            self.authentification = True
    
    def deposit(self,deposit_amount):
        if self.authentification == True:
            if deposit_amount>0:
                self.balance +=deposit_amount
                print(f'The balance of your account is {self.balance}')
            else:
                raise Exception('The deposit has to be positive')
        else:
            raise Exception("You did not being authenticated")
        
    def withdraw(self,withdraw_amount):
        if self.authentification == True:
            if 0<withdraw_amount<=self.balance:
                self.balance -= withdraw_amount
                print(f'The balance of your account is {self.balance}')
            elif withdraw_amount>=self.balance:
                print('You don\'t have enough money')
            else:
                raise Exception('The deposit has to be positive')
        else:
            raise Exception("You did not being authenticated")


class MinimumBalanceAccount(BankAccount):
    def __init__(self,username, password, balance, authenticated=False,minimum_balance=0):
        super().__init__(username, password, balance, authenticated=False)
        self.minimum_balance = minimum_balance
    
    def withdraw(self,withdraw_amount):
        if self.balance>self.minimum_balance:
            super().withdraw(withdraw_amount)
        else:
            raise Exception('You can\'t withdraw')

class ATM():
    def __init__(self,account_list,try_limit):
        for account in account_list:
            if isinstance(account, BankAccount)==True or isinstance(account,MinimumBalanceAccount)==True:
                self.account_list = account_list
            else:
                print(f'the account {account} is unvailable')
        
        try:
            assert try_limit>0
        except:
            print("It is not a positive number")
            self.try_limit = 2
        else:
            self.try_limit = try_limit

        self.current_tries = 0
    
    def show_main_menu(self):
        ans = True
        while ans:
            print(''' 
            1. Log in
            2. Exit
            ''')
            ans = input('What would you like to do?')
            if ans =='1':
                return self.log_in()
            elif ans=="":
                print("\n Not Valid Choice Try again") 
                return self.show_main_menu()
            elif ans=='2':
                print("\n Goodbye")
                return 
    
    def log_in(self):
        username = input('Enter the username')
        password = input('Enter password')
        for account in self.account_list:
            if account.username == username and account.password == password:
                return self.show_account_menu(account)
        else:
            self.current_tries +=1
            while self.current_tries < self.try_limit:
                return self.log_in()
            else:
                print('You reached max tries')
                return 
    
    def show_account_menu(self,account):
        if isinstance(account, BankAccount)==True or isinstance(account,MinimumBalanceAccount)==True:
                self.account = account
        account.authentification = True
        ans = True
        while ans:
            print(''' 
            1. Deposit
            2. Withdraw
            3. Exit
            ''')
            ans = input('What would you like to do?')
            if ans =='3':
                print("\n Goodbye")
                return
            elif ans=='1':
                deposit = int(input("Enter the amount"))
                return account.deposit(deposit)
            elif ans=='2':
                withdraw = int(input('Enter the amount'))
                return account.withdraw(withdraw)
            
     
    

account1 = BankAccount('yona','1234',500)
account2 =BankAccount('lea','134',800) 
accounts = [account1,account2]

atm = ATM(accounts,2)
atm.show_main_menu()

