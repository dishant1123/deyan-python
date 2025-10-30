# encap + inheritance  : 

"""class person : 
    def __init__(self):
        self.__name ="deyaan"
        self.__age =20
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        self.__age =new_age
        
class activity(person):
    def __init__(self):
        super().__init__()
        self.__activity ="coding"
    
    def display(self):
        print("name is : ",self.get_name())
        print("age is : ",self.get_age())
        print("activity is : ",self.__activity)

a=activity()
print("without using set method:")
a.display()

a.set_age(21)
print("using set method:")
a.display()
"""

# polymorphism  :  many forms  ==>  same function / method  can behave diffrently based on the  object or number of arguments. 

"""
1.method  overloading 
2.method  overriding 
"""

# method  overloading  with default arguments : 

"""class calculation : 
    def add(self,a,b=10,c=20):
        print("a + b + c = ",a+b+c)
        
    def mul(self,x,y=20,z=30):
        print("a * c = ",x*y*z)

c=calculation()
c.add(10)  # 2 arg ==> default value  ==> b=10 c=20 
c.add(12,13)  # 2 a=12 b=13  c =20 
c.add(1,2,3)  # 3 arg ==> default value  ==> a=1 b=2 c=3

c.mul(12)
c.mul(12,13)  # 2 arg ==> default value  ==> y=20 z=30
c.mul(12,13,14)  # 3 arg ==> default value  ==> x=12 y=13 z=14
"""

# method  overriding  : 

class animal : 
    def speak(self):
        print("animal can speak")

class dog(animal):
    def speak(self):  # override  base class method 
        print("dog can speak")

class cat(animal):
    def speak(self):  # override  base class method
        print("cat can speak")
        
c=cat()
c.speak()

d=dog()
d.speak()