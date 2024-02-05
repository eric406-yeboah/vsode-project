from customtkinter import CTk
from customtkinter import CTkEntry,CTkButton
from tkinter import messagebox
from pytube import YouTube

def button_callback():
    print("button clicked")

app = CTk()
app.geometry("500x410")
app.resizable(False,False)
# button = customtkinter.CTkButton(app, text="my button", command=button_callback)
# button.pack(padx=20, pady=20)
# entry=w.CTkEntry(app,placeholder_text="type here")
# entry.pack()


def downloadvid():
    url=txt_url.get()
    if len(url.stip())<1:
      messagebox.showerror('invalid URL','plrase provide valid URL') 
    else:
        yt =YouTube(url=url)
        yt.strems.first().download()
       
txt_url= CTkEntry(app,placeholder_text="enter video url",width=350) 
txt_url.place(x=30,y=30)

btn_download=CTkButton(app, text='download', command=downloadvid)
btn_download.place(x=120,y=80)


app.mainloop()