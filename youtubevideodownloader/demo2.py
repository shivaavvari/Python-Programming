from tkinter import *
from tkinter import filedialog
from pytubefix import YouTube
from moviepy.editor import *
import shutil
def download():
    try:
        video_path = entry.get()
        file_path= entry2.get()
        yt =YouTube(video_path)
        mp4 = yt.streams.get_highest_resolution().download(output_path=file_path)
        videoclip = VideoFileClip(mp4)
        audio_file = videoclip.audio
        audio_file.write_audiofile('audio.mp3')
        shutil.move(audio.mp3,file_path)
        audio_file.close()
        videoclip.close()
        shutil.move(mp4,file_path)
        print("Download Complete")
    except Exception as e:
        print(f"An error occurred:{e}")



root = Tk()
root.title('VideoDownloader')
canvas = Canvas(root,width=300,height=400)
canvas.pack()

label= Label(root,text='VideoDownloader Link',fg="blue",font=("Arial",18))
canvas.create_window(180,20,window=label)
entry = Entry(root)
canvas.create_window(180,80,window=entry)
label2= Label(root,text='Enter the Download Location')
canvas.create_window(180,120,window=label2)
entry2 = Entry(root)
canvas.create_window(180,150,window=entry2)
button =Button(root,text='Browse',command=lambda: entry2.insert(0,filedialog.askdirectory()))
canvas.create_window(180,180,window=button)

button2 =Button(root,text='download',command = download)
canvas.create_window(180,220,window=button2)

root.mainloop()