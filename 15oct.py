# emp  manag  app  : 
"""
1. single level , 2.multi level ,3. multi ple 
"""
class employee :
    def __init__(self):
        self.data ={}
        print("base  class constructor called")
        
class employeesDB(employee):   # single level 
    def add(self):
        id =int(input("enter the  emp  id :"))
        name =input("enter the  emp name  : ")
        salary =int(input("enter the  emp salary :"))
        self.data[id] =[name,salary]
        print("emp succesfully added.")

class employeesoperation(employeesDB):  # multi level  : 
    def delete_emp(self):
        id =int(input("enter the  emp  id :"))
        if id in self.data:
            del self.data[id]
            print("emp succesfully deleted.")
        else :
            print("emp  id is not  found.")
    
    def update_emp(self):
        id =int(input("enter the  emp  id :"))
        if id in self.data:
            name =input("enter the  new emp name  : ")
            salary =int(input("enter the  new emp salary :"))
            self.data[id] =[name,salary]
            print("emp succesfully updated.")
        else :
            print("emp  id is not  found.")

class serach_display:
    def serach_emp(self):
        id =int(input("enter the  emp  id :"))
        if id in self.data:
            print("emp  id is found.")
            print("emp name is ",self.data[id][0])
            print("emp salary is ",self.data[id][1])
        else :
            print("emp  id is not  found.")
            
    def display_emp(self):
        if self.data:
            print("\n ======== Employee Records ======== \n")
            for  i ,j in self.data.items():
                print(f"id  : {i} , name  : {j[0]} , salary  : {j[1]}")
        else :
            print("no  employee  found")
            
class emp_management(employeesoperation,serach_display):  # multi level  :
    
    def __init__(self):
        super().__init__()  # base  class constructor  called  ==>employees 
        print("emp manage system  is  up and running")
        
obj =emp_management()

while True:
    print("\n ======== emp manage system ======== \n")
    print("1. add emp")
    print("2. delete emp")
    print("3. update emp")
    print("4. serach emp")
    print("5. display emp")
    print("6. exit")
    
    choice =int(input("enter your choice : "))
    if choice ==1:
        obj.add()
    elif choice ==2:
        obj.delete_emp()
    elif choice ==3:
        obj.update_emp()
    elif choice ==4:
        obj.serach_emp()
    elif choice ==5:
        obj.display_emp()
    elif choice ==6 :
        print("exit for emp manag system")
        break
    else :
        
        print("invalid choice")
           
        
"""
id    name    salary
1     deyaan   9000000  key ==> 1  ==>values   [deyaan,9000000]
2     kabir    8000     key ==> 2  ==>values   [kabir,8000]

vehicle manag system  : 

id/srno/chasis number  name  ,  model,  speed, color 

1. add vehicle
2. delete vehicle
3. update vehicle
4. serach vehicle
5. display vehicle
6.exit   
"""