# bank  : 

class bank : 
    def __init__(self,name,branch):  # parameter con 
        self.name =name   # 2 parameter constructor
        self.branch =branch
        self.balance =25000   # non parameter constructor
        
    def deposit(self,amount):
        self.balance +=amount
        print("deposited  :",amount)
        print("balance is  :",self.balance)
        
    def withdraw(self,amount):
        self.balance -=amount
        print("withdrawed  :",amount)
        print("balance is  :",self.balance)
    
    def show(self):
        print("name is  :",self.name)   
        print("branch is  :",self.branch)
        print("balance is  :",self.balance)

b=bank("deyaan","axis")
print("===========BANK INFORMATION===========") 
b.show()
print("===========DEPOSIT AND WITHDRAW===========")
b.deposit(1000)
b.withdraw(500)
   
        
        