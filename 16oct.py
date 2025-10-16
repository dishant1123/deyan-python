#hybrid level  of inheritance :  it is  combination  of  more than one  inheritance .
"""
class a  : 

class b(a) :   # single  level 

class c : 

class d : 

class e (c,d)   # multi ple  : 

"""

class employee : 
    def __init__(self):
        self.name ="deyaan"
        self.salary =900000
        
class manager(employee):
    def __init__(self):
        super().__init__()  # based class constructor  called
        self.manager_name ="manish"

class senior_manager:
    def __init__(self):
        self.sr_name ="dhiren"

class CEO :
    def __init__(self):
        self.c_name ="jagdish"

class company(senior_manager,CEO,manager):
    def __init__(self, com_name):
        self.com_name =com_name
        senior_manager.__init__(self)
        CEO.__init__(self)
        manager.__init__(self)
    
    def display(self):
        print("company name is ",self.com_name)
        print("CEO name is ",self.c_name)
        print("senior manager name is ",self.sr_name)
        print("manager name is ",self.manager_name)
        print("employee name is ",self.name)
        print("employee salary is ",self.salary)

c=company("TBZ")
c.display()
 

