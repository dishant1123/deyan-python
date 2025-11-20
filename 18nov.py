# file handling : 
"""
1.read :  exiting open  
2.write : write + exiting  open  ==> overwrite  
3.append :write  + append ==> exiting open  ==> last add 
"""
# write  : 

"""
with  open("deyaan.txt","w") as f :
    f.write("my name is  deyaan shah.\n")
    f.write("my age is 18.\n")
    f.write("my hobby is  playing game.")
    f.close()
"""
# write  mode  exiting file  : 

"""with open("deyaan.txt","w") as f :
    f.write("love india.\n")
    f.write("dream to meet messi.\n")
    f.close()
"""

# append : 

"""with  open("riva.txt","a") as f :
    f.write("my name is  riva shah.\n")
    f.write("my age is 11.\n")
    f.write("my hobby is watching you tube shorts.")
    f.close()
"""

# append  mode  exiting file  :

"""with open("deyaan.txt","a") as f :
    f.write("my best friend name is kabir.\n")
    f.write("my cousin name is hitansh.\n")
"""

# read: 

"""with  open("deyaan.txt","r") as f :
    # context =f.read()
    # context =f.readline()
    context =f.readlines()
    print(context)
"""