# inheritance :  to inherit the properties of a class. 
"""
5 type inheritance  : 

1. single  level inheritance 
2. multiple level inheritance
3. multi level inheritance
4. hirearchy inheritance
5. hybrid inheritance

"""
# single level inheritance : 

"""class student :  # base class 
    def __init__(self):
        self.name = "deyan"  # non  parameterized constructor
        self.age = 18        # name  , age ==> public 
    
class clg(student):  # derived class
    def __init__(self):
        super().__init__()  # student constructor calling  / base class constructor calling
        self.clg_name = "GLS"
    
    def show(self):
        print("name is :",self.name)
        print("age is ",self.age)
        print("clg name is ",self.clg_name)

c=clg()
c.show()
print(c.name)
print(c.age)
print(c.clg_name)
print("===========change using object=========== ")
c.name="kabir"
c.age=19
c.clg_name="JG"
c.show()
"""
# private  : 

"""class vehicle : 
    def __init__(self,type,speed):
        self.__type =type 
        self.__speed =speed  # type  , speed ==> private   + parameterized constructor
        
    def show(self):
        print("type is ",self.__type)
        print("speed is ",self.__speed)

class car(vehicle):
    def __init__(self,type,speed,color):
        super().__init__(type,speed)  # calling the constructor of the base class
        self.color =color  # color ==> private
        
    def display(self):
        self.show()   # vehicle show method calling
        print("color is ",self.color)

c=car("4-wheelar",180,"red")
c.display()
# print(c.__type) # beacuse car type is private , so we can't access it
c.__type="5-wheelar"
c.display()
"""


class employees :
    def __init__(self):
        self.name ="deyaan"
        self.salary =90000
    def show(self):
        print("name is ",self.name)
        print("salary is ",self.salary)

class manager(employees):
    def __init__(self,manager_name):
        super().__init__()
        self.manager_name =manager_name
    
    def display(self):
        self.show()
        print("manager name is ",self.manager_name)

m=manager("kabir")
m.display()