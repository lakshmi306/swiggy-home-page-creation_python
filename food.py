from tkinter import *
from PIL import ImageTk,Image
import webbrowser
window =Tk()
window.geometry('1500x1000')
window.configure(background='white')
new = 1
def openwin1():
    url='https://www.swiggy.com/restaurants/thaqwa-biriyani-ambattur-chennai-34281'
    webbrowser.open(url,new=new)
def openwin2():
    url='https://www.swiggy.com/restaurants/burger-king-anna-nagar-annanagar-chennai-74037'
    webbrowser.open(url,new=new)
def openwin3():
    url='https://www.swiggy.com/restaurants/kfc-vavin-mogappair-chennai-17827'
    webbrowser.open(url,new=new)
def openwin4():
    url='https://www.swiggy.com/restaurants/hotel-sri-bhavan-mth-road-ambattur-chennai-85330'
    webbrowser.open(url,new=new)
def openwin5():
    url='https://www.swiggy.com/restaurants/mcdonalds-vr-mall-anna-nagar-annanagar-chennai-131599'
    webbrowser.open(url,new=new)
def openwin6():
    url='https://www.swiggy.com/restaurants/ganga-sweets-bazaar-road-mogappair-chennai-16616'
    webbrowser.open(url,new=new)
def openwin7():
    url='https://www.swiggy.com/restaurants/savoury-sea-shell-anna-nagar-annanagar-chennai-20391'
    webbrowser.open(url,new=new)
def openwin8():
    url='https://www.swiggy.com/restaurants/paradise-biryani-jj-nagar-mogappair-chennai-157426'
    webbrowser.open(url,new=new)
my_pic=ImageTk.PhotoImage(file='capture5.png')
my_label=Label(window,image=my_pic,bd=0)
my_label.place(x=60,y=140)
my_pic2=ImageTk.PhotoImage(file='C:\\Users\\Lakshmi\\Desktop\\image\\capture6.png')
my_labe2=Label(window,image=my_pic2,bd=0)
my_labe2.place(x=400,y=140)
my_pic3=ImageTk.PhotoImage(file='C:\\Users\\Lakshmi\\Desktop\\image\\capture1.png')
my_labe3=Label(window,image=my_pic3,bd=0)
my_labe3.place(x=760,y=140)
label1=Label(window,text='493 restaurants',bd=0,font=('arial',20,"bold"),bg='white')
label1.place(x=60,y=80)
my_pic4=ImageTk.PhotoImage(file='C:\\Users\\Lakshmi\\Desktop\\image\\capture7.png')
my_labe4=Label(window,image=my_pic4,bd=0)
my_labe4.place(x=1100,y=140)
img=ImageTk.PhotoImage(file='C:\\Users\\Lakshmi\\Desktop\\image\\capture8.png')
btn1=Button(window,image=img,bd=0,command=openwin1)
btn1.place(x=60,y=450)
img2=ImageTk.PhotoImage(file='C:\\Users\\Lakshmi\\Desktop\\image\\capture2.png')
btn2=Button(window,image=img2,bd=0,command=openwin2)
btn2.place(x=400,y=450)
img3=ImageTk.PhotoImage(file='C:\\Users\\Lakshmi\\Desktop\\image\\capture3.png')
btn3=Button(window,image=img3,bd=0,command=openwin3)
btn3.place(x=760,y=450)
img4=ImageTk.PhotoImage(file='C:\\Users\\Lakshmi\\Desktop\\image\\capture4.png')
btn4=Button(window,image=img4,bd=0,command=openwin4)
btn4.place(x=1100,y=450)
img5=ImageTk.PhotoImage(file='capture6.png')
btn5=Button(window,image=img5,bd=0,command=openwin5)
btn5.place(x=20,y=430)
img6=ImageTk.PhotoImage(file='capture7.png')
btn6=Button(window,image=img6,bd=0,command=openwin6)
btn6.place(x=320,y=430)
img7=ImageTk.PhotoImage(file='capture8.png')
btn7=Button(window,image=img7,bd=0,command=openwin7)
btn7.place(x=620,y=430)
img8=ImageTk.PhotoImage(file='capture9.png')
btn8=Button(window,image=img8,bd=0,command=openwin8)
btn8.place(x=920,y=430)

window.mainloop()
