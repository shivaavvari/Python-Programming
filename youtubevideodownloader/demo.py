from tkinter import * 
from tkinter import filedialog
from pytubefix import YouTube
from moviepy.editor import  * 
import shutil

def download():
    try:

        video_path = url_entry.get()
        file_path = path_label.cget("text")
        if not video_path.startswith("https://www.youtube.com/"):
            print("Invalid YouTube URL")
            return
        mp4 = YouTube(video_path).streams.get_highest_resolution().download(output_path=file_path)
        videoclip = VideoFileClip(mp4)
        # code for MP3
        audio_file = videoclip.audio
        audio_file.write_audiofile('audio.mp3')
        shutil.move(audio.mp3,file_path)
        audio_file.close()
        videoclip.close()
        shutil.move(mp4,file_path)
        print("Download Complete")
    except Exception as e:
        print(f"An error occurred:{e}")       
 

  
def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


root= Tk()
root.title('Video Downloader')
canvas = Canvas(root,width=400, height=300)

canvas.pack()

app_label = Label(root,text="Video Downloader",fg="blue",font=("Arial",30))
canvas.create_window(200,20,window=app_label)
#entry to accept video url

url_entry = Entry(root)
url_label = Label(root, text="Enter video url:")
canvas.create_window(200,80,window=url_label)
canvas.create_window(200,100,window=url_entry)

#path to download videos
path_label = Label(root, text="Select path to download")
path_button = Button(root,text="Select", command = get_path)
canvas.create_window(200,150,window=path_label)
canvas.create_window(200,170,window=path_button)

#downloadbutton 
download_button = Button(root,text="Download", command=download)

canvas.create_window(200,250,window=download_button)

root.mainloop()