# single  line  input  , multi line  input , check  box,  check button 

from  tkinter import *

"""
root = Tk() 
root.title("simple  form")

# single line  input  : 
Entry(root).pack()

# multi line  input  : 
Text(root,height=10,width=20).pack()

# check box : 
v=IntVar()
Checkbutton(root,text="i agree",variable=v).pack()  

# button  : 
Button(root,text="submit").pack()
root.mainloop()

"""

# login validation program : 

root = Tk() 
root.title("simple login  form")
root.geometry("500x500")

# username : 
Label(root,text="username").pack()
user= Entry(root) 
user.pack()

# password :
Label(root,text="password").pack()
password= Entry(root) 
password.pack()

# checkbox :
agree =IntVar()
Checkbutton(root,text="i agree",variable=agree).pack()

msg =Label(root,text=" ")
msg.pack()

# login  logic : 
def login():
    if user.get() == "deyan" and password.get() == "12345" and agree.get() == 1:
        msg.config(text="login  successful",fg="green")
    else :
        msg.config(text="login  failed",fg="red")

button = Button(root,text="login",command=login)
button.pack()

root.mainloop()
