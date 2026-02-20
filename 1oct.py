# multiple inheritance : 
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

"""class student :
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
c.display()"""

#=======================# 
"""variable ="Welcome to Python"
print(variable)
print(variable[0])

"""

v = ["smeet","kabir","deyan","deepak","deep","meet"]
# print(v[2:4])
# print(v*4)

# d={"name":"smeet","age":19,"gender":"male",78:90}  # dict -> mutable  

# t1 =(1,2,3,4,5,6,7,8,9)   # immutable 

"""
if : 

elif () :

else : 
"""

"""s1="my name is ram."


for i in range(1,21):
    print(i)
    
"""

"""a=int(input("enter a number : "))
b=int(input("enter a number : "))
c=int(input("enter a number : "))
d=int(input("enter a number : "))
e=int(input("enter a number : "))

avg =(a+b+c+d+e)/5
print("average : ",avg)
"""

"""a=12
print(a)
print(type(a))
b=float(a)
print(b)
print(type(b))
"""

"""s1="Hello WorlD"

print(s1.count("l"))

print(s1.swapcase())

s2="welcome in gls university"

print(s2.index("uni"))
print(s2.index("u"))

print(s2[2:6])
print(s2[2:8:2])
print(s2[: : -1])

"""

# using  while  : 

"""i=1 
while i<=50 : 
    if i % 2==0 :
        print(i)
    i+=1
"""

# break : 

"""for i in range(1,10): 
    if i==4 :
        break 
    print(i)
"""

"""for i in range(1,10): 
    if i==4 :
        continue 
    print(i)
"""
"""n=int(input("enter a number : "))
for i in range(1,11):
    # print(f"{n} X {i} = {n*i}")
    print(n,"X",i,"=",n*i)
"""
"""v = ["smeet","kabir","deyan","deepak","deep","meet"]

for i in v :
    print(i)
"""

l1=[1,2,3,4,5,6,7,8,9]
l2=["smeet","kabir","deyan","deepak","deep","meet"]

# l1.extend(l2)
# print(l1)

"""t1=(1,2,3,4,5,6,7,8,9)   # immutable
t2=("smeet","kabir","deyan","deepak","deep","meet")

print(t1)
t3=t1+t2
print(t3)
"""

"""d={"name":"smeeta","age":19,"gender":"male"}  # dict -> mutable  

d["city"] ="surat"
print(d)

d.update({"age":20,"gender":"female"})
print(d)

d.pop("age")
print(d)

"""

"""s1={1,2,4,7,8}
s2={2,45,8,90}

print(s1.union(s2))
print(s1.intersection(s2))


fz =frozenset({1,2,4,7,8})
print(fz)
print(type(fz))

"""
"""for i in range(0,5):
    for  k in range(5,i,-1):
        print(" ",end="")
    for j in range(0,i + 1):
        print(chr(65 + j), end=" ")
    print()
"""
# 
"""
          *
        * *
      * * *
    * * * * 
  * * * * * 
"""

"""for  i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""

# prime using def : 

"""def check_prime(n):
    count =0
    for i in range(1,n+1):
        if n % i ==0 :
            count +=1 
    if count ==2 :
        return True
    else :
        return False
n=int(input("enter a number : "))
if check_prime(n) ==1:
    print(" prime")
else :
    print(" not prime")
"""

l1=[10,826,432,84,59,633,71,28,79]

"""
print(l1[3])
print(l1[-2])
"""

# l1.append(1345)
# print(l1)

# l1.insert(3,"yashvi")
# print(l1)

"""l1[2]="yashvi"
print(l1)

l1.remove("yashvi")
print(l1)
"""

# as 3  que 1 : 

"""def calculate (b,a=10,c=20):
    return a+b+c

print(calculate(10))
print(calculate(12,14,16))

"""

# *args : 

# def d(*args):
    # print(max(args))
    # sum =0 
    # for i in args:
        # sum =sum +i 
    # print(sum)
# d(1,2,3,4,5,6,7,8,9)

# **kwargs :

"""def d1(**kwargs):
    for i,j in kwargs.items():
        print(i,"=",j)
d1(name="deyan",age=19,gender="male")
"""

# lambda : 

"""
l1= lambda x : x*x*x
print(l1(2))
"""

# local  :

"""def f():
    x=100   # local variable  : it is access only inside the function  not outside the function
    print(x)
f()
"""
# print(x) # bcz  of local  variable you can't access it outside the function

# global :

"""x=100   # golbal variable  : it is access outside the function  also inside the function
def g():
    print(x)
g()
print(x)
"""

# modify global variable : using  global key word 

"""x=100 

def g():
    global x  
    x=900
    print(x)
g()
print(x)

"""

# class object : 

"""class student :   # student class 
    name ="yashvi"   # name  age   ==> data  member
    age =20 
    
    def show(self):
        print("name is : ",self.name)
        print("age is : ",self.age)
        
s1=student()  # s1 ==> object of class student 
print("name is  :",s1.name)
print("age is  :",s1.age)
s1.show()
"""

# constructor  : automatically called when object is created

"""class student : 
    def __init__(self,name,age):  # def ==> function   ==> __init__ () ==>constructor  /  special method
        self.name =name 
        self.age =age
        
    def show(self):
        print("name is : ",self.name)
        print("age is : ",self.age)
        
l1=[] 

for i in range(3):
    name =input("enter name : ")
    age =int(input("enter age : "))
    s=student(name ,age)
    l1.append(s)
    
for s in l1:
    s.show()
"""

# inheritance  : 

"""
class a : 
class b(a) 

multiple  : 

class a : 
class b: 
class c(a,b) 

multi level : 

class a : 
class b(a):
class c(b)
 

"""