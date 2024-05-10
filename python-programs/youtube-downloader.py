import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

def download_video():
    try:
        video_url = url_entry.get()
        yt = YouTube(video_url)
        video = yt.streams.first()
        save_path = filedialog.askdirectory()
        if save_path:  # Если пользователь выбрал папку
            video.download(save_path)
            messagebox.showinfo("Success", "Video successfully downloaded!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_paste(event):
    text = root.clipboard_get()
    url_entry.insert(tk.INSERT, text)

# Создаем главное окно
root = tk.Tk()
root.title("YouTube Video Downloader")

# Создаем и размещаем виджеты на главном окне
url_label = tk.Label(root, text="Enter YouTube Video URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

# Добавляем обработчик событий для вставки из буфера обмена по нажатию Ctrl+V
url_entry.bind('<Control-v>', on_paste)

# Запускаем главный цикл обработки событий
root.mainloop()
