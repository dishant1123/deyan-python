# abstraction :  to hide the implementation details and only show the relevant details. 
"""
class ==> abstract  ==> abc ==> abstract base class 
method  ==> abstract method ==>

class ==> from abc import ABC 
method  ==> @abstractmethod 

abstract class ==> no define in the class and also  method if it is declare abstract method. 

"""
from abc import ABC ,abstractmethod

"""class animal(ABC):
    def show(self):
        pass 
class dog(animal):
    def show(self):  
        print("dog class")
class cat(animal):
    def show(self):
        print("cat class")

c=cat()
d=dog()

c.show()
d.show()
"""

class bank (ABC):
    def __init__(self,name,balance):
        self.name =name 
        self.balance =balance 
        print("bank class constructor called for ",self.name)
    
    @abstractmethod
    def deposit(self,amt):
        pass 
    
    @abstractmethod
    def withdraw(self,amt):
        pass  
    
class savings(bank):
    def __init__(self, name, balance,accnumber):
        super().__init__(name, balance)
        self.accnumber = accnumber
        print("savings class constructor called for ",self.name)
        
    def deposit(self, amt):
        self.balance += amt
        print(f"{self.name} deposited : {amt} , new balance is : {self.balance}") 
    
    def withdraw(self, amt):
        self.balance -= amt
        print(f"{self.name} withdrawn : {amt} , new balance is : {self.balance}")
        
    def display(self):
        print(f"name : {self.name} , balance is : {self.balance}")
        print(f"acc number : {self.accnumber}")
    
s=savings("deyan",90000,1234567890)
s.deposit(10000)
s.withdraw(50000)
s.display()