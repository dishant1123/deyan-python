# encapsulation  : 
"""
use  ==> private  variable  direct access 

2 method  :  1. get  ==> data  print  
             2. set  ==>  new value set 
"""

# without using  encap : 

"""class emp :
    __name ="deyaan"  # name , salary  ==> private 
    __salary =90000
    
    # function  /  method  
    def show(self):
        print("name is  : ",self.__name)
        print("salary is  : ",self.__salary)
        
e=emp()
e.show()
print(e.__name)  # not  accessible  outside  the class
"""
# using  encap : 

class emp : 
    def __init__(self):
        self.__name ="deyaan"  # name , salary  ==> private
        self.__salary =90000
        
    # def get_name(self):
    #     return self.__name

    # def get_salary(self):
    #     return self.__salary

    # def set_name(self,new_name):
    #     self.__name =new_name
    
    # def set_salary(self,new_salary):
    #     self.__salary =new_salary
        
e=emp()
"""print("without using set method:")

print("name is  : ",e.get_name())
print("salary is  : ",e.get_salary())

print("using set method:")

e.set_name("kabir")
e.set_salary(8000)
print("name is  : ",e.get_name())
print("salary is  : ",e.get_salary())
"""
setattr(e,"name","kabir")  # set attr 
setattr(e,"salary",8000)

print("name is : ",getattr(e,"name"))  # get attr 
print("salary is  :",getattr(e,"salary"))

