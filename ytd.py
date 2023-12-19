import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download()
        messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

# Set up the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create a label and entry widget for the URL
tk.Label(root, text="YouTube URL:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create a download button
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

# Run the application
root.mainloop()
