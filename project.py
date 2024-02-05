from tkinter import Text,Tk
from tkinter.ttk import Button,Entry,Label

window=Tk()
window.config(width=500, height=500,bg='black')
window.geometry('700x700+500+200')
window.resizable(False,False)

ib_firstnumber=Label(text='first number',font=10,background='red')
txt_firstnumber=Entry()

ib_secondnumber=Label(text='second number',font=10,background='red')
txt_secondnumber=Entry()

def btn_add ():
    num=txt_firstnumber.get()
    num1=txt_secondnumber.get()
    num_result=int(num)+int(num1)
    result=Label(text=f'the result is {num_result}')
    result.place(x=10,y=300)
    
def btn_product():
    num=txt_firstnumber.get()
    num1=txt_secondnumber.get()
    num_result=int(num)*int(num1)
    result=Label(text=f'the result is {num_result}')
    result.place(x=0,y=300)

def btn_sub():
    num=txt_firstnumber.get()
    num1=txt_secondnumber.get()
    num_result=int(num)-int(num1)
    result=Label(text=f'the result is {num_result}')
    result.place(x=0,y=300)

def btn_divide():
    num=txt_firstnumber.get()
    num1=txt_secondnumber.get()
    num_result=int(num)-int(num1)
    result=Label(text=f'the result is {num_result}')
    result.place(x=0,y=300)

def btn_reminder():
    num=txt_firstnumber.get()
    num1=txt_secondnumber.get()
    num_result=int(num)%int(num1)
    result=Label(text=f'the result is {num_result}')
    result.place(x=0,y=300) 

def btn_exponent():
    num=txt_firstnumber.get()
    num1=txt_secondnumber.get()
    num_result=int(num)**int(num1)
    result=Label(text=f'the result is {num_result}')
    result.place(x=0,y=300) 
         
ib_add=Button(text='add ',command=btn_add)
ib_product=Button(text='product',command=btn_product)
ib_substraction=Button(text='substraction',command=btn_sub)
ib_division=Button(text='division',command=btn_divide)
ib_reminder=Button(text='reminder',command=btn_reminder)
ib_exponential=Button(text='exponenetial',command=btn_exponent)

ib_firstnumber.place(x=50,y=87)
txt_firstnumber.place(y=90,x=170)
ib_secondnumber.place(x=20,y=160)
txt_secondnumber.place(x=170,y=160)
ib_add.place(x=140,y=210)
ib_product.place(x=230,y=210)
ib_substraction.place(x=320,y=210)
ib_division.place(x=410,y=210)
ib_reminder.place(x=500,y=210)
ib_exponential.place(x=590,y=210)
window.mainloop()