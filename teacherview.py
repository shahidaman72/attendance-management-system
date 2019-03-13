from tkinter import *

import tkinter.messagebox
import sqlite3
conn=sqlite3.connect("attendance.db")
c=conn.cursor()
sqll = "SELECT * FROM teachers"
c.execute(sqll)
l=list(c)

us=[]

        
for i in range(len(l)):
            
            u=l[i]
            #print(l[i])
            teacher_id=u[0]
            teacher_name=u[1]
            #print(teacher_id)
            us.append(teacher_id)
class user():
    def __init__(self,master):
        self.master=master
        self.heading=Label(self.master,text="teacher information ",font=("arial 20 bold"),bg="sky blue",fg="white")
        self.heading.place(x=10,y=10)
      
        self.teacher_id=Label(self.master,text="click on getbutton to get list of teachers",font="arial 20",bg="white",fg="red")
        self.teacher_id.place(x=10,y=50)
        self.teacher_name=Label(self.master,text="search for the teacher",font="arial 20",bg="sky blue",fg="red")
        self.teacher_name.place(x=600,y=20)

        self.teacherdel_id=Label(self.master,text="enter teacher_id ",font="arial 20",bg="sky blue",fg="red")
        self.teacherdel_id.place(x=600,y=50)

        #entry
        self.teacher_id_entry=Entry(self.master,width=30)
        self.teacher_id_entry.place(x=600,y=150)

      

        #button
        self.login=Button(self.master,text="get",command=self.submit,width=20,bg='green',fg="white")
        self.login.place(x=50,y=100)
        self.box=Text(self.master,height=60,width=60,bg='white',fg='black')
        self.box.place(x=20,y=200)
        self.box2=Text(self.master,height=20,width=40,bg='white',fg='black')
        self.box2.place(x=600,y=230)
        #button
        self.login1=Button(self.master,text="search",command=self.search,width=20,bg='green',fg="white")
        self.login1.place(x=600,y=200)
        #defining fns
    def submit(self):
        self.box.delete(1.0,END)
        sql="select * from teachers t,subject S where S.teacher_id=T.teacher_id"
        self.result1=c.execute(sql)
        for i in self.result1:
            j=i
            self.box.insert(END,("teacher_id=",j[0]))
            self.box.insert(END,('\n'))
            self.box.insert(END,("teacher_name=",j[1]))
            self.box.insert(END,('\n'))
            self.box.insert(END,("sub_code=",j[2]))
            self.box.insert(END,('\n'))
            self.box.insert(END,("sub_name=",j[3]))
            self.box.insert(END,('\n'))
    def search(self):
        self.box2.delete(1.0,END)
        self.val55=self.teacher_id_entry.get()
        s=self.teacher_id_entry.get()
        sql88="select S.sub_code from teachers t,subject S where S.teacher_id=T.teacher_id group by sub_code having s.teacher_id=?" 
        self.result2=c.execute(sql88,(self.val55,))
        
        conn.commit()

        p=[]
        for h in self.result2:
            l=h
            p.append(l)
        print(p)

        f=1
        for j in us:
            
            if(str(j)==str(s)):

                self.box2.insert(END,('teacher teaches the subject with subcodes:'))
                self.box2.insert(END,('\n'))
                self.box2.insert(END,(p[0:]))
                self.box2.insert(END,('\n'))
               
                f=0
                break
        if(f==1 ):
               self.box2.insert(END,('techer_id is not found \n'))
        
               
root=Tk()
root.configure(background="skyblue")
#photo2=PhotoImage(file="download (1).gif")
#Label(root,image=photo2,bg="blue").place(x=40,y=50)
b=user(root)
root.geometry("1200x700+0+0")
root.resizable(0,0)
