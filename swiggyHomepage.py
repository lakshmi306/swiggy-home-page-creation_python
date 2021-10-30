from tkinter import *
from PIL import ImageTk,Image
import webbrowser 
import time
import pymysql
root=Tk()
root.title('Swiggy Home page')
root.geometry('1500x1000')
root.configure(background='white')
iconimage=ImageTk.PhotoImage(file='C:\\Users\\Lakshmi\\Desktop\\image\\img11.png')
root.iconphoto(False,iconimage)
new=0
url='swiggysignup.py'
def signup():
   webbrowser.open(url,new=new)
url1='login.py'
def login():
   webbrowser.open(url1,new=new)
my_pic=ImageTk.PhotoImage(file='C:\\Users\\Lakshmi\\Desktop\\image\\img6.png')
my_label=Label(root,image=my_pic,bd=0)
my_label.place(x=20,y=4)
jkbtn1=Button(root,text='Login',font=('arial',13,"bold"),bg='white',bd=0,command=login)
btn1.place(x=500,y=40)
btn2=Button(root,text='Sign up',font=('arial',13,"bold"),fg='white',bg='black',bd=0,command=signup)
btn2.place(x=570,y=40)
my_pic2=ImageTk.PhotoImage(file='C:\\Users\\Lakshmi\\Desktop\\image\\img9.png')
my_label2=Label(root,image=my_pic2,bd=0)
my_label2.place(x=700,y=5)
my_label3=Label(root,text='Unexpected Guests?',font=('arial',20,"bold"),fg='black',bg='white',bd=0)
my_label3.place(x=30,y=150)
my_label4=Label(root,text='Order food from favourite restaurants near you.',font=('arial',18),fg='grey',bg='white')
my_label4.place(x=30,y=190)
entry=Entry(root,width=50,font=('arial',12,"bold"),fg='grey' ,bg='white',highlightthickness=2,bd=0)
entry.insert(0, "Enter your delivery location")
entry.place(x=30,y=250,height=60)
entry.configure(highlightbackground = "orange", highlightcolor= "darkorange")
btn3=Button(root,text='FIND FOOD',font=('arial',13,"bold"),fg='white',bg='orange',bd=0)
btn3.place(x=455,y=250,height=60)
my_label5=Label(root,text='POPULAR CITIES IN INDIA',font=('arial',13),fg='grey',bg='white')
my_label5.place(x=30,y=350)
new = 1
url1 = "https://www.swiggy.com/ahmedabad"
def openweb1():
    webbrowser.open(url1,new=new)
Btn4 = Button(root, text = "Ahmedabad",command=openweb1,fg='black',bg='white',bd=0,font=('arial',10,'bold'))
Btn4.place(x=30,y=380)
url2='https://www.swiggy.com/bangalore'
def openweb2():
    webbrowser.open(url2,new=new)
Btn5 = Button(root, text = "Bangalore",command=openweb2,fg='grey',bg='white',bd=0,font=('arial',10,'bold'))
Btn5.place(x=120,y=380)
url3='https://www.swiggy.com/chennai'
def openweb3():
    webbrowser.open(url3,new=new)
Btn6 = Button(root, text = "Chennai",command=openweb3,fg='black',bg='white',bd=0,font=('arial',10,'bold'))
Btn6.place(x=197,y=380)
url4='https://www.swiggy.com/Delhi'
def openweb4():
    webbrowser.open(url4,new=new)
Btn7 = Button(root, text = "Delhi",command=openweb4,fg='grey',bg='white',bd=0,font=('arial',10,'bold'))
Btn7.place(x=260,y=380)
url5='https://www.swiggy.com/gurgaon'
def openweb5():
    webbrowser.open(url5,new=new)
Btn8 = Button(root, text = "gurgaon",command=openweb5,fg='black',bg='white',bd=0,font=('arial',10,'bold'))
Btn8.place(x=300,y=380)
url6='https://www.swiggy.com/hyderabad'
def openweb6():
    webbrowser.open(url6,new=new)
Btn9 = Button(root, text = "Hyderabad",command=openweb6,fg='grey',bg='white',bd=0,font=('arial',10,'bold'))
Btn9.place(x=370,y=380)
url7='https://www.swiggy.com/kolkata'
def openweb7():
    webbrowser.open(url7,new=new)
Btn10 = Button(root, text = "Kolkata",command=openweb7,fg='black',bg='white',bd=0,font=('arial',10,'bold'))
Btn10.place(x=460,y=380)
url8='https://www.swiggy.com/mumbai'
def openweb8():
    webbrowser.open(url8,new=new)
Btn11 = Button(root, text = "Mumbai",command=openweb8,fg='grey',bg='white',bd=0,font=('arial',10,'bold'))
Btn11.place(x=520,y=380)
url9='https://www.swiggy.com/pune'
def openweb9():
    webbrowser.open(url9,new=new)
Btn12 = Button(root, text = "Pune & More",command=openweb9,fg='black',bg='white',bd=0,font=('arial',10,'bold'))
Btn12.place(x=30,y=400)
my_pic3=ImageTk.PhotoImage(file='C:\\Users\\Lakshmi\\Desktop\\image\\img7.png')
my_label6=Label(root,image=my_pic3,bd=0)
my_label6.place(x=5,y=500)
root.mainloop()
