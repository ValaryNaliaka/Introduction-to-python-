#bank account
class BankAccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name,amount_withdrawn,deposit):
        self.account=account_number
        self.bal=balance
        self.date=date_of_opening
        self.customer=customer_name
        self.amount=amount_withdrawn
        self.dep=deposit
    def deposit(self):
        return("amount deposited",self.dep)
    def  withdraw(self):
       if (self.bal <= self.amount):
        print("insufficient balance")
       else:
        print("amount withdrawn",self.amount)
    def check_balance(self):
        print("current balance",self.bal)
    def customer_details(self):
        print("customer name",self.customer,"account number",self.account,"date of account opening",self.date,"balance",self.bal)
bank=BankAccount(23145,5250,3,"VALARY",500,1000)
bank.deposit()
bank.withdraw()
bank.check_balance()
bank.customer_details()