class Bank:
    def __init__(self, balance):
        self.balance = balance
        
    def debit(self, amount):
       self.balance-=amount
       print(f"debit amount is {amount}")
       print("current balance after debit =",self.total_amount())
       
    def credit(self, amount):
       self.balance+=amount
       print(f"credit amount is {amount}")
       print("current balance after credit =",self.total_amount())
       
    def total_amount(self):
        return self.balance
    
    
b1 = Bank(5000)
print("total amount is =",b1.total_amount())
b1.credit(200)
b1.debit(1000)
    
    