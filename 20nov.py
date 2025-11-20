"""
1.read +  : read write  exiting file  . 
2.write +
3.append + 
"""

#r+ : 

"""with  open("deyaan.txt","r+") as f :
    
    f.seek(0)      
    f.write("love aus.") 
    f.seek(0)
    t =f.read()
    print(t)
"""

# w+ : 
"""with  open("deyaan.txt1","w+") as f :
    f.write("my best friend name is  kabir.\n")
    f.write("my cousin name is hitansh.\n")
    f.seek(0)
    cont =f.read()
    print(cont)
    f.close()
"""

"""with  open("deyaan.txt","w+") as f :
    f.write("my best friend name is  kabir.\n")
    f.write("my cousin name is hitansh.\n")
    f.seek(0)
    cont =f.read()
    print(cont)
    f.close()
"""

# a+ : 

with  open("deyaan.txt1","a+") as f :
    f.write("my best friend name is  jiyaan.\n")
    f.write("my cousin name is harsh.\n")
    f.seek(0)
    cont =f.read()
    print(cont)
    f.close()
