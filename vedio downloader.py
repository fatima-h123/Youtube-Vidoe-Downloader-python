from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube


def select_path():
    
    #path of folder
    path = filedialog.askdirectory()
    path_label.configure(text=path)
    
def download_file():
    #user folder
    get_link = link_field.get()
    #to get selected folder
    user_path = path_label.cget("text")
    #download vedio
    YouTube(get_link ).streams.get_highest_resolution().download()
    mp4_vedio = YouTube(get_link ).streams.get_highest_resolution().download()
    clip = VideoFileClip(mp4_vedio)
    clip.close()
    
screen = Tk()
title = screen.title ('YT DOWNLOADER')
canvas = Canvas(screen, width = 500, height = 500)
canvas.pack()

#image logo 
logo_img = PhotoImage(file = 'youtube.png')

#resize
logo_img = logo_img.subsample(7, 7)

canvas.create_image(150, 80, image=logo_img)

#link feild
link_field = Entry(screen, width=50)
link_lable = Label(screen, text="Enter Link", font=('Times New Roman', 15))


#Select folder
path_label = Label(screen, text="SELECT FOLDER", font=('Times New Roman', 15))
select_button = Button(screen, text="SELECT", command=select_path)
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_button)

#Add widgets
canvas.create_window(250, 170, window=link_lable)
canvas.create_window(250, 220, window=link_field)

#Download button
download_button = Button(screen, text= "DOWNLOAD FILE", command=download_file)
#add to canvas
canvas.create_window(250, 390, window=download_button)

screen.mainloop()