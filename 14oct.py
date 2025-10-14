# hierarchy  level of inheritance :  multiple  derived  classes  can  inherit  from  a  single/ same   base  class.

"""
class parent  : 
class child(parent) : 
class child2(parent) : 
"""

"""class parent : 
    def display(self):
        print("parent class")
        
class child(parent):
    def display1(self):
        print("child1 class")
        
class child2(parent):
    def display2(self):
        print("child2 class")
        
print("child 2 object : ")
c=child2()
c.display2()   #  child2 method 
c.display()  # parent  method 

print("child object : ")
c1=child()
c1.display1()  # child1 method 
c1.display()  # parent  method 
"""

# using  constrcutor  : 

class vehicle : 
    def __init__(self):
        self.type="two wheeler"
        self.max_speed=140 

class bike(vehicle):
    def __init__(self,model,color):
        super().__init__()  # base  class constructor called 
        self.model =model 
        self.color=color
    
    def show(self):
        print("type  of  vehicle : ",self.type)
        print("max speed : ",self.max_speed)
        print("bike model : ",self.model)
        print("bike color : ",self.color)
                
class activa(vehicle):
    def __init__(self,model,color):
        super().__init__()
        self.model =model
        self.color=color
    
    def show(self):
        print("type  of  vehicle : ",self.type)
        print("max speed : ",self.max_speed)
        print("activa model : ",self.model)
        print("activa color : ",self.color)
        
b=bike("splendor","black")
b.show()

a=activa("honda","white")
a.show()