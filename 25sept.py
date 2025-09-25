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

class student :  # base class 
    def __init__(self):
        self.name = "deyan"  # non  parameterized constructor
        self.age = 18
    
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