from tkinter import Text, Tk
from tkinter.ttk import *

# CREATE A WINDOW
window=Tk()
# setting the bg
window.config(bg='black')
# setting the geometry of window
window.geometry('500x500+90+90')

# creating  controls
ib_title=Label(text='sign in',font=10,)
ib_username=Label(text='username',font=10,background='red')
ib_password=Label(text='password',font=100,background='red')

# creating text controls
txt_username=Text(height=1,width=20)
txt_password=Text(height=1,width=20)


# creating button control
btn_sign_in=Button(text='sign in')
btn_sign_in_2=Button(text='sign in')


# display widgit using geometry
ib_title.pack()
ib_username.place(x=50,y=90)
txt_username.place(y=90,x=150)
ib_password.place(x=50,y=160)
txt_password.place(x=150,y=160)
btn_sign_in_2.place(x=180,y=200)

window.mainloop()