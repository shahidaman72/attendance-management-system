from tkinter import *

import tkinter.messagebox
import sqlite3
import random
conn=sqlite3.connect("attendance.db")
c=conn.cursor()
sqll = "SELECT * FROM student"
c.execute(sqll)
l=list(c)

us=[]

        
for i in range(len(l)):
            
            u=l[i]
            #print(l[i])
            student_id=u[0]
            us.append(student_id)
class user():
    def __init__(self,master):
        self.master=master
        self.heading=Label(self.master,text="student insertion and information ",font=("arial 20 bold"),bg="sky blue",fg="white")
        self.heading.place(x=10,y=10)
        self.heading=Label(self.master,text="student delete or update",font=("arial 20 bold"),bg="sky blue",fg="white")
        self.heading.place(x=550,y=10)
        self.student_id=Label(self.master,text="student_id",font="arial 20",bg="sky blue",fg="red")
        self.student_id.place(x=50,y=300)
        self.student_name=Label(self.master,text="student_name",font="arial 20",bg="sky blue",fg="red")
        self.student_name.place(x=50,y=340)
        self.course=Label(self.master,text="course",font="arial 20",bg="sky blue",fg="red")
        self.course.place(x=50,y=380)
        self.semester=Label(self.master,text="semester",font="arial 20",bg="sky blue",fg="red")
        self.semester.place(x=50,y=420)
        self.sub_code=Label(self.master,text="sub_code",font="arial 20",bg="sky blue",fg="red")
        self.sub_code.place(x=50,y=460)
        self.studentdel_id=Label(self.master,text="enter student_id ",font="arial 20",bg="sky blue",fg="red")
        self.studentdel_id.place(x=550,y=450)
        self.studentupd_id=Label(self.master,text="update\n\tstudent name  course  semester",font="arial 20",bg="sky blue",fg="red")
        self.studentupd_id.place(x=450,y=50)
        self.studentupdl_id=Label(self.master,text="where s_id:",font="arial 20",bg="sky blue",fg="red")
        self.studentupdl_id.place(x=550,y=200)
        #entry
        self.student_id_entry=Entry(self.master,width=30)
        self.student_id_entry.place(x=240,y=310)
        self.student_name_entry=Entry(self.master,width=30)
        self.student_name_entry.place(x=240,y=350)
        
        self.course_entry=Entry(self.master,width=30)
        self.course_entry.place(x=240,y=390)
        self.semester_entry=Spinbox(self.master, from_=1, to=8)
        self.semester_entry.place(x=240,y=430)
        self.sub_code_entry=Entry(self.master,width=30)
        self.sub_code_entry.place(x=240,y=470)
        self.studentdel_id_entry=Entry(self.master,width=30)
        self.studentdel_id_entry.place(x=550,y=500)
        
        self.studentupd_name_entry=Entry(self.master,width=30)
        self.studentupd_name_entry.place(x=570,y=150)
        self.studentupd_course_entry=Entry(self.master,width=30)
        self.studentupd_course_entry.place(x=720,y=150)
        self.studentupd_sem_entry=Spinbox(self.master, from_=1, to=8)
        self.studentupd_sem_entry.place(x=870,y=150)
        self.studentupd_id_entry=Entry(self.master,width=30)
        self.studentupd_id_entry.place(x=550,y=250)
        #button
        self.login=Button(self.master,text="submit",command=self.submit,width=20,height=2,bg='green',fg="white")
        self.login.place(x=100,y=560)
        self.delete=Button(self.master,text="delete",command=self.delete,width=20,height=2,bg='red',fg="white")
        self.delete.place(x=550,y=550)
        self.update=Button(self.master,text="update",command=self.update,width=20,height=2,bg='green',fg="white")
        self.update.place(x=550,y=270)
        self.view=Button(self.master,text="view students",command=self.view,width=40,height=3,bg='green',fg="white")
        self.view.place(x=50,y=50)
    def submit(self):
        self.val1=self.student_id_entry.get()
        self.val2=self.student_name_entry.get()
        self.val3=self.course_entry.get()
        self.val4=self.semester_entry.get()
        self.val5=self.sub_code_entry.get()
        if self.val1=='':
                tkinter.messagebox.showinfo("warning","plese fill username and password")
        else:
            sql="INSERT INTO 'student'(student_id,student_name,course,semester) VALUES(?,?,?,?)"
            sql1="INSERT INTO 'admin'(username,password,usertype) VALUES(?,?,?)"
            sq2="INSERT INTO 'attendance'(student_id,semester,sub_code) VALUES(?,?,?)"
            #sql3="INSERT INTO 'student_subjects'(student_id,sub_code) VALUES(?,?)"
            c.execute ( sq2, (self.val1 , self.val4,self.val5))
            c.execute ( sql, (self.val1 , self.val2 , self.val3,self.val4))
            #c.execute ( sql3, (self.val1 ,self.val5))
            c.execute ( sql1, (self.val1 , (random.randint(00000000,99999999)), 'student'))
            conn.commit()
            tkinter.messagebox.showinfo("sucessfull","student added secessfully")
    def delete(self):
            self.input=self.studentdel_id_entry.get()    
            sql1="delete from student where student_id=?"
            sql00="delete from admin where username=?"
            sql01="delete from attendance where student_id=?"
            #sql102="delete from student_subjects where student_id=?"
            self.result=c.execute(sql1,(self.input,))
            self.result1=c.execute(sql00,(self.input,))
            self.result2=c.execute(sql01,(self.input,))
            #self.result=c.execute(sql102,(self.input,))
            i =self.studentdel_id_entry.get()
            f=1
            if (self.input==''):
                    tkinter.messagebox.showinfo("error"," enter student_id")
            for j in us:
                
                
                #print(self.teacherdel_id_entry.get()==i)
                if(int(j)==int(i)):
                            

                        conn.commit()
                        tkinter.messagebox.showinfo("congrats","sucessfully deleted")
                        f=0
                        break
            if(f==1):
                tkinter.messagebox.showinfo("error","student_id not found")
    def view(self):
        import stufile
        
    def update(self):


            self.val5=self.studentupd_name_entry.get()
            self.val6=self.studentupd_course_entry.get()
            self.val7=self.studentupd_sem_entry.get()
            self.val8=self.studentupd_id_entry.get()
            sql2="UPDATE student SET student_name=?,course=?,semester=? WHERE student_id=?;"
            sql0="update attendance SET semester=? where student_id=?"
            i =self.studentupd_id_entry.get()
            f=1
            if (self.val5=='' and self.val6=='' and self.val7=='' and self.val8==''):
                tkinter.messagebox.showinfo("error"," enter data to update")
            for j in us:
                

                #print(self.teacherdel_id_entry.get()==i)
                if(int(j)==int(i)):
                            
                        self.result=c.execute(sql2,(self.val5,self.val6,self.val7,self.val8))
                        self.r=c.execute(sql0,(self.val7,self.val8))
                        conn.commit()
                        tkinter.messagebox.showinfo("congrats","sucessfully updated")
                        f=0
                        break
                
            if(f==1):
                tkinter.messagebox.showinfo("error"," student_id not found")


            
                
root=Tk()
root.title("student enter update delete")
root.title("students")
root.configure(background="skyblue")
#photo2=PhotoImage(file="download (1).gif")
#Label(root,image=photo2,bg="blue").place(x=40,y=50)
b=user(root)
root.geometry("1200x700+0+0")
root.resizable(True,True)










