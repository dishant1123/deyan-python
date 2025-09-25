# constructor  : automatically  called  when  object  is  created. 
"""
1. default  constructor  :
2. parameterized  constructor  :
3. non-parameterized  constructor  :
4. constructor over  loading  :
"""
# defualt  constructor  : 
"""class deyaan : 
    def __init__(self):  # def ==>  keyword  ==> __init __ ==> special method / constructor 
        print("deyaan class and it is  default constuctor")
        print("live in ahm.")
        
d=deyaan()
"""

# non - parameterized  constructor  :

"""class deyaan : 
    def __init__(self):   # name  age salary  ==> public 
        self.name ="deyan"
        self.age =19
        self.salary =90000 
    def show(self):
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("salary is  :",self.salary)

d=deyaan()
# print("name is  :",d.name)
# print("age is  :",d.age)
# print("salary is  :",d.salary)
d.show()
"""

# parameterized  constructor  :
"""class deyaan : 
    def __init__(self,name ,age,salary):
        self.name =name 
        self.age =age
        self.salary =salary
    
    def show(self):
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("salary is  :",self.salary)
        

d=deyaan("chiku",10,100000)
d1=deyaan("kabir",19,9000)
print(d.name)
print(d.age)
print(d1.name)
# d.show()
# d1.show()
for i in d,d1: 
    i.show()
"""

# constructor over loading  : 

"""
class deyaan : 
    def __init__(self):
        print("deyaan class and it is  default constuctor")
    
    def __init__(self):
        print("chiku class")

    def __init__(self,name):
        print("kabir class")
        self.name =name
d=deyaan("deyaan")
"""

