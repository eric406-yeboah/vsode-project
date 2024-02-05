from tkinter import Text, Tk
from tkinter.ttk import *
from pytube import YouTube,Search
from threading import Thread

window=Tk(className=' YOUTUBE VIDEO DOWNLOADER')
window.config(width=500, height=100,bg='black')
window.geometry('700x700+500+200')
window.resizable(False,False)

titile_label=Label(text='enter youtube URL')
txt_search=Entry(width=52)
selected_video=None
view=[]




def search_video():
    url=txt_search.get() 
    yt=YouTube(url)
    selected_video=yt
    return selected_video
    

def video(watch_video):
    # if selected_video:
    #    video_url=selected_video.watch_url()
    #    import webbrowser
    #    webbrowser.open(video_url)
   Thread(target=watch_video)
   return(watch_video)
   
   
def video_downloader(yt):
    
    yt.streams.filter(progressive=True,file_extension='mp4').first().download()
        
search_btn=Button(text='search',command=search_video)    
video_btn=Button(text='play video',command=video) 
download_video=Button(text='download')  
    
search_btn.place(x=520,y=50)
txt_search.place(x=200,y=50)
titile_label.place(x=97,y=50)
video_btn.place(x=300,y=100)
download_video.place(x=300,y=150)
window.mainloop()