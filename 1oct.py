# multi ple inheritance : 
"""
class a : 
class b : 

class c (a,b)
"""

"""class father :
    def skill(self):
        print("father skill : driving")
        
class mother :
    def skill(self):
        print("mother skill : cooking")
        
class child(father,mother):
    def skill(self):
        super().skill()  # first  method  calling   ==>  method  resoultion order  (MRO)
        print("child skill : playing")

c=child()
c.skill()
"""

# using  constructors: 

class student :
    def __init__(self):
        self.name="deyaan"
        self.age=19

class teacher :
    def __init__(self):
        self.t_name ="kabir"
        self.t_age=35 
        
class clg(student,teacher):
    def __init__(self,c_name):
        self.c_name =c_name
        student.__init__(self)  # student class consturctor  calling 
        teacher.__init__(self)  # teacher class consturctor  calling
        
    def display(self):
        print("=========CLG INFORMATION========")
        print("CLG name : ",self.c_name)
        print("******STUDENT INFORMATION*******")
        print("name : ",self.name)
        print("age : ",self.age)
        print("******TEACHER INFORMATION*******")
        print("teacher name : ",self.t_name)
        print("teacher age : ",self.t_age)

c=clg("RMIT")
c.display()