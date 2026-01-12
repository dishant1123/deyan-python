"""
1. graphis 
tk.tk() 

label() ==> display text
button() ==> clickable
entry ==> input sigline  input 
text  ==> multi  line  input  
checkbox ==> check box
checkbutton ==> check box
"""
import tkinter as tk 

root = tk.Tk()
root .title("my first window")
root .geometry("500x500")

label = tk.Label(root, text = "hello world",font=("times",20)).pack()

def say_hello():
    print("hello  deyaan")
button = tk.Button(root,text="click me",command=say_hello).pack()

root.mainloop()    # run  application 

