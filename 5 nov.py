# override + loading  + inheritance : 
class bank  : 
    def __init__(self,name,balance):
        self.name =name 
        self.balance =balance 
        print("bank class constructor called for ",self.name)
        
    # method  overloading (using default arguments)    
    def deposit(self,amt=0,bonus =0 ):
        total  = amt +bonus 
        self .balance += total
        print(f"{self.name} deposited : {total} , new balance is : {self.balance}")

    def display(self):
        print(f"name : {self.name} , balance is : {self.balance}")   
        
    def calculation_interest(self) :
        print("no specific rate  decided") 
        
class savings(bank):
    def __init__(self, name, balance,int_rate):
        super().__init__(name, balance) 
        self.int_rate = int_rate
        print("savings class constructor called for ",self.name)
        
    # overriding
    def calculation_interest(self):
        interest = self.balance *self.int_rate /100
        print(f"interest for {self.name} at rate {self.int_rate}%  is : {interest}")
    
    #overriding
    def deposit(self, amt=0, bonus=0,cashback=0):
        total = amt + bonus + cashback
        self.balance += total
        print(f"{self.name} deposited : {total} , new balance is : {self.balance} including cashback")

class current(bank):
    def __init__(self, name, balance,overdraft_limit):
        super().__init__(name, balance) 
        self.overdraft_limit = overdraft_limit
        print("current class constructor called for ",self.name)
    
    def calculation_interest(self):
        print(f"{self.name} 's current account has no interest")
        
    def display(self):  # method  overriding   ==> base class method  
        print("current account :")
        print(f'name : {self.name}')
        print(f'balance : {self.balance}')
        print(f'overdraft limit : {self.overdraft_limit}')
        
def main(): 
    print("savings account :")
    s1=savings("deyan",90000,5)
    s1.display()
    s1.calculation_interest()
    
    # method  overloading : 
    s1.deposit(5000)
    s1.deposit(3000,1000,500)
    
    print("\ncurrent account :")
    
    c1=current("chiku",50000,20000)
    c1.display()
    c1.calculation_interest()
    
    print("run time")
    for i in [c1,s1]:
        i.calculation_interest()  # polymorphic behavior

main()