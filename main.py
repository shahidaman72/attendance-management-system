from tkinter import *
#import attendance.py
import tkinter.messagebox
import sqlite3
conn=sqlite3.connect("attendance.db")
c=conn.cursor()
sqll = "SELECT * FROM admin"
c.execute(sqll)
l=list(c)
us=[]
ps=[]
ut=[]
st=[1234,5678,0000]
t=('teacher','student','admin')

for i in range(len(l)):
            u=l[i]
            username=u[0]
            password=u[1]
            usertype=u[2]
            
            us.append(username)
            ps.append(password)
            ut.append(usertype)
class user():
    def __init__(self,master):
        self.master=master
        self.heading=Label(self.master,text="attendance portal",font=("arial 20 bold"),bg="sky blue",fg="white")
        self.heading.place(x=10,y=10)
        self.username=Label(self.master,text="username",font="arial 20",bg="sky blue",fg="red")
        self.username.place(x=50,y=300)
        self.password=Label(self.master,text="password",font="arial 20",bg="sky blue",fg="red")
        self.password.place(x=50,y=340)
        self.usertype=Label(self.master,text="usertype",font="arial 20",bg="sky blue",fg="red")
        self.usertype.place(x=50,y=380)
        #entry
        self.username_entry=Entry(self.master,width=30)
        self.username_entry.place(x=200,y=310)
        self.password_entry=Entry(self.master,width=30,show='*')
        self.password_entry.place(x=200,y=350)
        self.usertype_entry=Spinbox(self.master, values=t, width=20)
        self.usertype_entry.place(x=200,y=390)
        #button
        self.login=Button(self.master,text="login",command=self.login,width=20,height=2,bg='green',fg="white")
        self.login.place(x=400,y=300)
        #defining fns
    def login(self):
        self.val1=self.username_entry.get()
        self.val2=self.password_entry.get()
        self.val3=self.usertype_entry.get()
        u=self.val1
        p=self.val2
        r=self.val3
        f=0
        for i in range(len(us)):
                if(str(us[i])==u and int(ps[i])==int(p) and str(ut[i])==r):
                    f=1
                    print('n',us[i],u,ps[i],p,ut[i],r)
                    print("s")
                    break       
        if (f==0):
            tkinter.messagebox.showinfo("warning","please fill username and password")
        
        elif (f==1 and self.usertype_entry.get()=='teacher'):
                import teacherview
        elif(f==1 and self.usertype_entry.get()=="student"):
                    import stufile
        elif(f==1 and self.usertype_entry.get()=="admin"):
                
                import studenttable,teacher,attendance
        else:
          
           
            tkinter.messagebox.showinfo("warning","please fill correct username and password")
            #print(self.username_entry.get(),self.password_entry.get(),self.val3)"""
                            
                     
root=Tk()
root.title("admin page")
root.configure(background="skyblue")
photo2=PhotoImage(file="download (1).gif")
Label(root,image=photo2,bg="blue").place(x=40,y=50)
b=user(root)
root.geometry("1200x700+0+0")
root.resizable(False,False)

