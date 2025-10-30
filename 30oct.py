# encap + inheritance  : 

class person : 
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