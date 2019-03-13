from tkinter import *

import tkinter.messagebox
import sqlite3
conn=sqlite3.connect("attendance.db")
c=conn.cursor()
sqll = "SELECT * FROM admin"
c.execute(sqll)
l=list(c)
us=[]
ps=[]
for i in range(len(l)):
            
            u=l[i]
            student_id=u[0]
            password=u[1]
            us.append(student_id)
            ps.append(password)
class user():
    def __init__(self,master):
        self.master=master
        self.heading=Label(self.master,text=" enter student_id and password",font=("arial 20 bold"),bg="sky blue",fg="white")
        self.heading.place(x=10,y=10)
        self.u=Label(self.master,text="student_id",font=("arial 20 bold"),bg="sky blue",fg="white")
        self.u.place(x=10,y=40)
        self.p=Label(self.master,text="password",font=("arial 20 bold"),bg="sky blue",fg="white")
        self.p.place(x=10,y=80)
        #entry
        self.student_id_entry=Entry(self.master,width=30)
        self.student_id_entry.place(x=170,y=50)
        self.student_p_entry=Entry(self.master,width=30,show='*')
        self.student_p_entry.place(x=170,y=90)
        #button
        self.login=Button(self.master,text="get",command=self.search,width=20,bg='green',fg="white")
        self.login.place(x=50,y=150)
        self.box2=Text(self.master,height=60,width=60,bg='white',fg='black')
        self.box2.place(x=20,y=200)


            
    def search(self):
        self.val1=self.student_id_entry.get()
        u=self.student_id_entry.get()
        self.val2=self.student_p_entry.get()
        p=self.student_p_entry.get()
       
        u=self.val1
        p=self.val2


        f=0
        for i in range(len(us)):
            if(us[i]==u and int(ps[i])==int(p)):
                
                f=1
                break
        if(f==1):
            sql88="select * from student s,attendance a where s.student_id=? and a.student_id=?"
            self.result2=c.execute(sql88,(u,u))
            conn.commit()
            
            for h in self.result2:
                l=h
                break

            self.box2.insert(END,('student_name',l[1]))
            self.box2.insert(END,('\n'))
            self.box2.insert(END,('student_course',l[2]))
            self.box2.insert(END,('\n'))
            self.box2.insert(END,('student_semester',l[3]))
            self.box2.insert(END,('\n'))
            self.box2.insert(END,('classes_attended_in',l[7],'are',l[5]))
            self.box2.insert(END,('\n'))
            self.box2.insert(END,('in_month_of',l[8],l[9]))
        elif(f==0):     
            
            tkinter.messagebox.showinfo("warning","please fill correct details")

                
                
root=Tk()
root.configure(background="skyblue")
#photo2=PhotoImage(file="download (1).gif")
#Label(root,image=photo2,bg="blue").place(x=40,y=50)
b=user(root)
root.geometry("1200x700+0+0")
root.resizable(1,1)
