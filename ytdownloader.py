import tkinter
import customtkinter  # to make the UI nicer
from pytube import YouTube

#Function to download the youtube video
def startDownload():
    try:
        ytLink = link.get()
        ytObject =  YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        print("Youtube Video downloaded!")
    except:
        print("Youtube link invalid")


# App appearance
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube-Downloader")

#Adding UI elements
title = customtkinter.CTkLabel(app,text="Insert a Youtube Link")
title.pack(padx= 10, pady= 10)

# Adding an input for link
url_Variable= tkinter.StringVar()
link=customtkinter.CTkEntry(app, width = 350,height = 40, textvariable=url_Variable)
link.pack(padx= 10, pady= 10)

#Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx= 10, pady= 10)


# To run app continuously
app.mainloop()