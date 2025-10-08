# multi level  inheritance  : 
"""
class a 

class b (a)   : b ==> object ==> class a accessible

class c (b)  :  c ==> object ==> class a , b both  accessible 
"""

class employees :
    def __init__(self):
        self.name ="deyaan"
        self.salary = 900000 
        
class manager(employees):
    def __init__(self):
        self._manager_name ="manish"
        employees.__init__(self)

    def show(self):
        print("name is ",self.name)
        print("salary is ",self.salary)
        print("manager name is ",self._manager_name)

class company(manager):
    def __init__(self,c_name):
        self.c_name =c_name
        manager.__init__(self)
    
    def display(self):
        print("company name is ",self.c_name)
        print("manager name is ",self._manager_name)
        print("employees name is ",self.name)
        print("salary is ",self.salary)

c=company("TBZ")
c.display()

m=manager()
m.show()