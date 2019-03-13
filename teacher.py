from tkinter import *

import tkinter.messagebox
import sqlite3
import random
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
print(us)


class user():
    def __init__(self,master):
        self.master=master
        self.heading=Label(self.master,text="teacher insertion  ",font=("arial 20 bold"),bg="sky blue",fg="red")
        self.heading.place(x=10,y=10)
        self.headings=Label(self.master,text="subjects insertion  ",font=("arial 20 bold"),bg="sky blue",fg="red")
        self.headings.place(x=10,y=350)
        self.heading=Label(self.master,text="teacher delete or update",font=("arial 20 bold"),bg="sky blue",fg="red")
        self.heading.place(x=700,y=10)
        self.teacher_id=Label(self.master,text="teacher_id",font="arial 20",bg="sky blue",fg="blue")
        self.teacher_id.place(x=50,y=100)
        self.teacher_id=Label(self.master,text="teacher_id",font="arial 20",bg="sky blue",fg="blue")
        self.teacher_id.place(x=50,y=400)
        self.teacher_name=Label(self.master,text="teacher_name",font="arial 20",bg="sky blue",fg="blue")
        self.teacher_name.place(x=50,y=140)

        self.teacherdel_id=Label(self.master,text="enter teacher_id ",font="arial 20 bold",bg="sky blue",fg="red")
        self.teacherdel_id.place(x=700,y=450)
        self.teacherupd_name=Label(self.master,text="update \n     teacher name:",font="arial 20",bg="sky blue",fg="blue")
        self.teacherupd_name.place(x=650,y=50)
        self.teacherupd1_id=Label(self.master,text="where teacher_id is",font="arial 20",bg="sky blue",fg="blue")
        self.teacherupd1_id.place(x=700,y=200)
        self.teachers=Label(self.master,text="sub_code:",font="arial 20",bg="sky blue",fg="blue")
        self.teachers.place(x=700,y=150)
        self.entry=Label(self.master,text='sub_code',font="arial 20",bg="sky blue",fg="blue")
        self.entry.place(x=50,y=430)
        self.entry=Label(self.master,text='sub_name',font="arial 20",bg="sky blue",fg="blue")
        self.entry.place(x=50,y=460)
        #entry
        self.teacher_id_entry=Entry(self.master,width=30)
        self.teacher_id_entry.place(x=240,y=110)
        self.teachera_id_entry=Entry(self.master,width=30)
        self.teachera_id_entry.place(x=240,y=410)
        self.teacher_name_entry=Entry(self.master,width=30)
        self.teacher_name_entry.place(x=240,y=150)
        self.sub_code_entry=Entry(self.master,width=30)
        self.sub_code_entry.place(x=240,y=440)
        self.sub_code1_entry=Entry(self.master,width=30)
        self.sub_code1_entry.place(x=700,y=190)
        self.sub_name_entry=Entry(self.master,width=30)
        self.sub_name_entry.place(x=240,y=480)
        self.teacherdel_id_entry=Entry(self.master,width=30)
        self.teacherdel_id_entry.place(x=700,y=500)
        
        self.teacherupd_name_entry=Entry(self.master,width=30)
        self.teacherupd_name_entry.place(x=700,y=120)
      
        self.teacherupd_id_entry=Entry(self.master,width=30,fg="green")
        self.teacherupd_id_entry.place(x=700,y=250)
        
        #button
        self.login=Button(self.master,text="submit",command=self.submit,width=20,height=2,bg='green',fg="white")
        self.login.place(x=100,y=270)
        self.logind=Button(self.master,text="add",command=self.add,width=20,height=2,bg='green',fg="white")
        self.logind.place(x=100,y=510)
        self.delete=Button(self.master,text="delete",command=self.delete,width=20,height=2,bg='green',fg="white")
        self.delete.place(x=700,y=550)
        self.update=Button(self.master,text="update",command=self.update,width=20,height=2,bg='green',fg="white")
        self.update.place(x=700,y=280)
        self.input=self.teacherdel_id_entry.get()
        i =self.input 
        #defining fns
    def submit(self):
        self.val1=self.teacher_id_entry.get()
        self.val2=self.teacher_name_entry.get()
        self.val3=self.sub_code_entry.get()
        self.val4=self.sub_name_entry.get()
        if self.val1=='' or self.val2==''  :
                tkinter.messagebox.showinfo("warning","please fill all entries ")
        else:
            sql="INSERT INTO 'teachers'(teacher_id,teacher_name) VALUES(?,?)"
            sql2="INSERT INTO 'admin'(username,password,usertype) VALUES(?,?,?)"
            sql3="INSERT INTO'subject'(teacher_id,sub_code,sub_name) values(?,?,?)"
            c.execute(sql3,(self.val1,self.val3,self.val4))
            c.execute ( sql, (self.val1 , self.val2))
            c.execute ( sql2, (self.val1 , (random.randint(00000000,99999999)), 'teacher'))
            conn.commit()
            tkinter.messagebox.showinfo("sucessfull","teacher added secessfully")
    def delete(self):
            self.input=self.teacherdel_id_entry.get()
            sql1="delete from teachers where teacher_id=?"
            sql00="delete from admin where username=?"
            self.result=c.execute(sql1,(self.input,))
            self.result1=c.execute(sql00,(self.input,))
            
            i =self.teacherdel_id_entry.get()
            f=1
            if (self.input==''):
                    tkinter.messagebox.showinfo("error"," enter teacher_id")
            for j in us:
                
                
                #print(self.teacherdel_id_entry.get()==i)
                if(int(j)==int(i)):
                            

                        conn.commit()
                        tkinter.messagebox.showinfo("congrats","sucessfully deleted")
                        f=0
                        break
            if(f==1):
                tkinter.messagebox.showinfo("error","teacher_id not found")
           
            
           
    def update(self):

            q=self.sub_code1_entry.gest()
            self.val5=self.teacherupd_name_entry.get()
            self.val9=self.teacherupd_id_entry.get()
            sql4="UPDATE teachers SET teacher_name=? WHERE teacher_id=?"
            sql34="UPDATE subject SET sub_code=? WHERE teacher_id=?"
            i =self.teacherupd_id_entry.get()
            if (self.val5=='' and self.val9=='' ):
                    tkinter.messagebox.showinfo("error"," enter data to update")
            f=1
            for j in us:
                

                #print(self.teacherdel_id_entry.get()==i)
                if(int(j)==int(i)):
                            
                        self.result=c.execute(sql4,(self.val5,self.val9))
                        self.result1=c.execute(sql34,(q,self.val9))
                        conn.commit()
                        tkinter.messagebox.showinfo("congrats","sucessfully updated")
                        f=0
                        break
            if(f==1):
                tkinter.messagebox.showinfo("error"," teacher_id not found")
    def add(self):
            v1=self.teachera_id_entry.get()
            v2=self.sub_code_entry.get()
            v3=self.sub_name_entry.get()
            z=self.teachera_id_entry.get()
            print(v1,v2,v3)
            sql3="INSERT INTO'subject'(teacher_id,sub_code,sub_name) values(?,?,?)"
            f=1
            for j in us:
                    

                    #print(self.teacherdel_id_entry.get()==i)
                    if(str(j)==(z)):
                                
                            self.result=c.execute(sql3,(v1,v2,v3))
                            conn.commit()
                            tkinter.messagebox.showinfo("congrats","sucessfully added")
                            f=0
                            break
                   
            
            if(f==1):
                tkinter.messagebox.showinfo("error","student_id not found")
                
                    
root=Tk()
root.configure(background="skyblue")
root.title("teachers")
#photo2=PhotoImage(file="download (1).gif")
#Label(root,image=photo2,bg="blue").place(x=40,y=50)
b=user(root)
root.geometry("1200x700+0+0")
root.resizable(True,True)

