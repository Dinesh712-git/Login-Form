from tkinter import *
from tkinter import messagebox

def exit():
     root.quit()
    

 




def login():
    username=entry1.get()
    password=entry2.get()

    if(username=="" and password==""):
        messagebox.showinfo("","Blank Not Allowed")
        

    elif(username=="Parvat" and password=="admin"):
        messagebox.showinfo("","login Success")

    else:
        messagebox.showinfo("","Incorrect username and password")
   
        

root=Tk()
root.title("Login")
root.geometry("300x200",)

global entry1
global entry2


Label(root,text="username").place(x=20,y=20)
Label(root,text="password",show("*").place(x=20,y=70)

entry1=Entry(root,bd=5)
entry1.place(x=140,y=20)

entry2=Entry(root,bd=5)
entry2.place(x=140,y=70)


Button(root,text="Login",command=login,height=2,width=8,bd=3).place(x=100,y=120)
Button(root,text="Exit",command=exit,height=2,width=8,bd=3).place(x=200,y=120)
root.mainloop()
