# class - object : 
"""
class ==>  blue print  of object 
object ==>  instance of class

default  ==>  public class  ==> access any where 
private  : within  class access  ==> not  accessible  outside  the class 
"""
#ex :1 
"""
class person :   # person  ===> class  name  
    def show(self):  # def  ==>  function  ==> show ==> func  name , self ==> keyword ==>current  object   ==>method  , data member ==> access 
        print("person class ")
p=person()   # p ==>  object  ==>  person()
p.show()
"""

# ex :2 

"""
class person : 
    name = "deyan"  # name  , age  ==> data member  
    age =19 

    def show(self):
        print("name is  : ",self.name)
        print("age is  : ",self.age)
p=person()
p.show()  # function  ==> print  data member  ==> name age 
print("name is  :",p.name)   # direct  object print data member  
print("age is  :",p.age)
"""

# ex :3 private  : 

class employee : 
    __name ="deyan" # __name ,__age ==>  private data member 
    __age =19 

    def show(self):
        print("name is  : ",self.__name)
        print("age is  : ",self.__age)
e=employee()
e.show()
# print("name is  : ",e.__name)# not  accessible  outside  the class
# print("age is  : ",e.__age)