"""
class bank : 
    acc_holder_name ="deyan"  # acc_holder_name , acc_no , balance ==> data member
    bank_name ="HDFC"
    acc_no =1234567890
    balance =30000
    pin=int(input("enter your pin for pin generation   : "))  # pin ==> data member

    def authentication(self):
        attempts =0
        while attempts <3 :
            pin_input =int(input("enter your pin : "))
            if pin_input==self.pin :  
                print("correct pin")
                return True 
            else :
                attempts +=1
                print("incorrect pin attempt is  over",3-attempts)
        return False
    
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

b=bank()  # b object   ==> bank ()

if b.authentication():  # only  pin correct ==> true 
    while True :
        print("MENU")
        print("1.deposit")
        print("2.withdraw")
        print("3.check balance")
        print("4.show details")
        print("5.exit")
        choice =int(input("enter your choice : "))

        if choice ==1 :
            b.deposit()
        elif choice ==2 :
            b.withdraw()
        elif choice ==3 :
            b.check_balance()
        elif choice ==4 :
            b.show()
        elif choice ==5 :
            print("thx for using our bank")
            break
        else :
            print("invalid choice")
"""

# emp management  system : 
"""
1. add 
2. delete
3. update 
4. search
5. display

1.  add == > list  or  dict 
name ==>salary  ==> id   1  deyaan 90000 
                

add : 
id   name  salary 
1    deyan  90000
2    kabir  8000

5 . display  ()

2 . delete :   enter the id you want  to delete  : 2 
3. update  : enter the id  you want  to  update  : 1  100000 

"""

class employee :
    d1={}

    def add_emp(self): 
        id =int(input("enter the  id  : "))
        name =input('enter the  name  : ')
        salary =int(input('enter the  salary  : '))
        self.d1[id]=[name,salary]
    
    def delete_emp(self):
        id =int(input("enter the  id you want  to delete  : "))
        if id in self.d1:
            del self.d1[id]
            print("deleted successfully")
        else :
            print("id not  found")
    
    def update_emp(self): 
        id =int(input("enter the  id you want  to update  : "))
        if id in self.d1:
            name =input('enter the  name  : ')
            salary =int(input('enter the  salary  : '))
            self.d1[id]=[name,salary]
            print("updated successfully")
        else :
            print("id not  found")

e=employee()
e.add_emp()
e.add_emp()
print(e.d1)

e.delete_emp()
print(e.d1)

e.update_emp()
print(e.d1)
