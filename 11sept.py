# class - object : 
"""
class ==>  blue print  of object 
object ==>  instance of class

default  ==>  public class  ==> access any where 
private  : within  class access  ==> not  accessible  outside  the class 
"""
#ex :1 
"""
class person :   # person  ===> class  name  
    def show(self):  # def  ==>  function  ==> show ==> func  name , self ==> keyword ==>current  object   ==>method  , data member ==> access 
        print("person class ")
p=person()   # p ==>  object  ==>  person()
p.show()
"""

# ex :2 

"""
class person : 
    name = "deyan"  # name  , age  ==> data member  
    age =19 

    def show(self):
        print("name is  : ",self.name)
        print("age is  : ",self.age)
p=person()
p.show()  # function  ==> print  data member  ==> name age 
print("name is  :",p.name)   # direct  object print data member  
print("age is  :",p.age)
"""

# ex :3 private  : 

"""class employee : 
    __name ="deyan" # __name ,__age ==>  private data member 
    __age =19 

    def show(self):
        print("name is  : ",self.__name)
        print("age is  : ",self.__age)
e=employee()
e.show()
# print("name is  : ",e.__name)# not  accessible  outside  the class
# print("age is  : ",e.__age)
"""

# bank  : 

class bank : 
    acc_holder_name ="deyan"  # acc_holder_name , acc_no , balance ==> data member
    bank_name ="HDFC"
    acc_no =1234567890
    balance =30000 

    def deposit(self):
        amt =int(input("enter the  amount  you want  to deposit : "))  # 10000
        self.balance +=amt 
        print("your deposit amt is  : ",amt)
        print("your balance after  deposit :",self.balance)   # 40000 

    def withdraw(self):  # 40000 -33000 ==>7000 
        amt =int(input("enter the  amount  you want  to withdraw : ")) 
        if self.balance -amt >=10000 :  # 40000 -3300  >=10000 
            self.balance -=amt
            print("your withdraw amt is  : ",amt)
            print("your balance after  withdraw :",self.balance)  # 30000
        else :
            print("not  enough  balance  to  withdraw bcz you have to maintain  minimum  of  10000")
    
    def check_balance(self):
        print("your balance is  : ",self.balance)

    def show(self):
        print("NAME OF BANK IS  : ",self.bank_name)
        print("ACC NO IS  : ",self.acc_no)
        print("ACC HOLDER NAME IS  : ",self.acc_holder_name)
        print("BALANCE IS  : ",self.balance)

b=bank()
b.show()
b.deposit()
b.withdraw()
b.check_balance()

"""
task  :1 

1. pin generate ===>  enter your pin  : 1211  ==> correct  ==> deposit withdraw check balance 
2 . max attempt 3    ==> thank you. 

"""