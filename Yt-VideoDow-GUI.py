import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube

def download_video():
    link = entry.get()
    try:
        youtube = YouTube(link)
        video = youtube.streams.get_highest_resolution()
        file_path = filedialog.askdirectory()
        video.download(file_path)
        messagebox.showinfo("Məlumat", "Video müvəffəqiyətlə yükləndi.")
    except Exception as e:
        messagebox.showerror("Xəta", "Video yüklənmədi.\nXəta: {}".format(e))

root = tk.Tk()
root.title("YouTube Video Yüklə")
root.geometry("400x150")
root["bg"] = "lightblue"

label = tk.Label(root, text="YouTube video linki", bg="lightblue")
label.pack(pady=10)

entry = tk.Entry(root, bg="white")
entry.pack(pady=10)

download_button = tk.Button(root, text="Yüklə", command=download_video, bg="lightgreen")
download_button.pack(pady=10)

root.mainloop()
