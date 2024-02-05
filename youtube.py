from pytube import YouTube

yt=YouTube('https://www.youtube.com/shorts/PVNuAtgRVJ0?feature=share')
yt.streams.filter(progressive=True,file_extension='mp4').first().download()
