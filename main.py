import tkinter as tk
from tkinter.ttk import Button
window=tk.Tk(className='pella tech')
window.config(width=500, height=500,bg='green')
window.geometry('500x500+500+200')
window.iconbitmap('pellatech.ico')

# adding control/widget
btn_click=Button(text='click me')
btn_click_2=Button(text='second click me')
# btn_click.pack(ipadx=80,ipady=20,pady=10)

btn_click.place(x=40,y=40)
btn_click_2.pack()

window.mainloop()