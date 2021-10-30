from tkinter import *
from PIL import ImageTk,Image
import webbrowser
import pymysql
import tkinter.messagebox
window =Tk()
window.geometry('400x600')
window.configure(background='white')
window.title('login')
new=1
url='swiggysignup.py'
def signin():
    webbrowser.open(url,new=new)
def login():
    dbc=pymysql.connect(host='localhost',user='root',passwd='',db='swiggy')
    c=dbc.cursor()
    phone=entry.get()
    try:
        ans= "SELECT * From signup where phone number	='%s' "%phone
        c.execute(ans)
        result=c.fetchone()
        res=result[0]
        if res==phone:
            url='Slogin.py'
            webbrowser.open(url,new=new)          
        dbc.commit()
    except Exception as e:
        tkinter.messagebox.showinfo('Enter valid mobile number')
        print(e)
        dbc.rollback()
        dbc.close()    
label1=Label(window,text='Login',bd=0,font=('arial',20,"bold"),bg='white')
label1.place(x=20,y=40)
label2=Label(window,text='or',font=('arial',10),bg='white',bd=0)
label2.place(x=20,y=72)
button1=Button(window,text='create an account',font=('arial',10),fg='red',bg='white',bd=0,command=signin)
button1.place(x=35,y=70)
image1=ImageTk.PhotoImage(file='C:\\Users\\Lakshmi\\Desktop\\image\\img8.png')
label3=Label(window,image=image1,bd=0)
label3.place(x=250,y=4)
label4=Label(window,text='Phone number',font=('arial',9),fg='grey',bg='white',bd=0)
label4.place(x=30,y=150)
entry=Entry(window,width=45,font=('arial',10),fg='black' ,bg='white',highlightthickness=1,bd=0)
entry.place(x=30,y=170,height=40)
entry.config(highlightbackground = "grey", highlightcolor= "grey")
button2=Button(window,width=39,text='LOGIN',font=('callibri',10,'bold'),fg='white' ,bg='orange',command=login)
button2.place(x=30,y=230,height=50)
window.mainloop()
