from tkinter import *

import tkinter.messagebox
import sqlite3
conn=sqlite3.connect("attendance.db")
c=conn.cursor()
sqll = "SELECT * FROM attendance"
c.execute(sqll)
l=list(c)

us=[]
cs=[]
sc=[]        
for i in range(len(l)):
            
            u=l[i]
            #print(l[i])
            student_id=u[0]
            sub_code=u[3]
            classes_attended=u[1]
            cs.append(classes_attended)
            us.append(student_id)
            sc.append(sub_code)
r=((cs,us))
print(r)
class user():
    def __init__(self,master):
        self.master=master
        self.heading=Label(self.master,text="student attendance delete",font=("arial 20 bold"),bg="sky blue",fg="red")
        self.heading.place(x=500,y=10)
        self.heading1=Label(self.master,text="add new subject",font=("arial 20 bold"),bg="sky blue",fg="red")
        self.heading1.place(x=500,y=300)
        self.heading2=Label(self.master,text="sys_id:",font=("arial 20 bold"),bg="sky blue",fg="blue")
        self.heading2.place(x=500,y=340)
        self.heading12=Label(self.master,text="sub_code:",font=("arial 20 bold"),bg="sky blue",fg="blue")
        self.heading12.place(x=500,y=380)
        self.heading=Label(self.master,text="student attendance update",font=("arial 20 bold"),bg="sky blue",fg="red")
        self.heading.place(x=10,y=10)
        self.studentdel_id=Label(self.master,text="enter student_id :",font="arial 20",bg="sky blue",fg="red")
        self.studentdel_id.place(x=500,y=50)
        self.studentupd_id=Label(self.master,text="SET \n classattended: \nsemester:\n month:\nyear:",font="arial 20",bg="sky blue",fg="blue")
        self.studentupd_id.place(x=10,y=50)
        self.studentupdl_id=Label(self.master,text="where\n student id :\nsub_code:",font="arial 20",bg="sky blue",fg="blue")
        self.studentupdl_id.place(x=10,y=220)
        r=("JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC")
        #entry
       
        self.studentdel_id_entry=Entry(self.master,width=30)
        self.studentdel_id_entry.place(x=500,y=90)
        
        self.studentupd_cl_entry=Spinbox(self.master, from_=1, to=25)
        self.studentupd_cl_entry.place(x=210,y=90)
        self.wt = Spinbox(self.master, from_=2017, to=2030)
        self.wt.place(x=210,y=190)
        self.studentupd_sem_entry=Spinbox(self.master, from_=1, to=8)
        self.studentupd_sem_entry.place(x=210,y=120)
        self.studentupd_w=Spinbox(self.master, values=r)
        self.studentupd_w.place(x=210,y=150)
        self.studentupd_id_entry=Entry(self.master,width=30)
        self.studentupd_id_entry.place(x=210,y=260)
        self.studentupd_sc_entry=Entry(self.master,width=30)
        self.studentupd_sc_entry.place(x=210,y=300)
        self.studentadd_id_entry=Entry(self.master,width=30)
        self.studentadd_id_entry.place(x=700,y=340)
        self.studentsub_entry=Entry(self.master,width=30)
        self.studentsub_entry.place(x=700,y=380)
        #button
        self.add=Button(self.master,text="add",command=self.add,width=20,height=2,bg='red',fg="white")
        self.add.place(x=500,y=420)
        self.delete=Button(self.master,text="delete",command=self.delete,width=20,height=2,bg='red',fg="white")
        self.delete.place(x=500,y=120)
        self.update=Button(self.master,text="update",command=self.update,width=20,height=2,bg='green',fg="white")
        self.update.place(x=10,y=350)
        #defining fns
    def add(self):
        v1=self.studentadd_id_entry.get()
        v2=self.studentsub_entry.get()
        z=self.studentadd_id_entry.get()
        sqlt="INSERT INTO 'attendance'(student_id,sub_code)values(?,?)"
        f=1
        for j in us:
                

                #print(self.teacherdel_id_entry.get()==i)
                if(str(j)==(z)):
                            
                        self.result=c.execute(sqlt,(v1,v2))
                        conn.commit()
                        tkinter.messagebox.showinfo("congrats","sucessfully added")
                        f=0
                        break
               
        
        if(f==1):
                        tkinter.messagebox.showinfo("error","student_id not found")
    def delete(self):
            self.input=self.studentdel_id_entry.get()
            sql1="delete from attendance where student_id=?"
            i =self.studentdel_id_entry.get()
            f=1
            for j in us:
                

                #print(self.teacherdel_id_entry.get()==i)
                if(str(j)==i):
                            
                        self.result=c.execute(sql1,(self.input,))
                        conn.commit()
                        tkinter.messagebox.showinfo("congrats","sucessfully deleted")
                        f=0
                        break
            if(f==1):
                tkinter.messagebox.showinfo("error","student_id not found")
           

    def update(self):

            f=1
            self.val5=self.studentupd_cl_entry.get()
            
            self.val6=self.studentupd_sem_entry.get()
            self.val7=self.studentupd_w.get()
            self.val8=self.wt.get()
            t=self.studentupd_id_entry.get()
            s=self.studentupd_sc_entry.get()

            for i in range(len(us)) :
                
                if(str(us[i])==t) and (sc[i]==s):
                    sql2="UPDATE attendance SET classes_attended=?,semester=?,month=?,year=? WHERE student_id=? and sub_code=?;"
                    self.result1=c.execute(sql2,(self.val5,self.val6,self.val7,self.val8,t,s))
                    conn.commit()
                    f=0
                    
                    break
               

            if(f==0):
                tkinter.messagebox.showinfo("congrats","sucessfully updated")
            elif(f==1 or s==''):
                tkinter.messagebox.showinfo("oops"," user_id or sub code  doesnot match")
                print(us[i]==u,sc[i]==s)
            else:
                tkinter.messagebox.showinfo("oops","choose data to update")
                
root=Tk()
root.title("attendance enter update delete")
root.configure(background="skyblue")
#photo2=PhotoImage(file="download (1).gif")
#Label(root,image=photo2,bg="blue").place(x=900,y=50)
b=user(root)
root.geometry("900x700+0+0")
root.resizable(False,True)
