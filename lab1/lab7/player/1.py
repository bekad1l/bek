import os
import tkinter as tk
from tkinter import PhotoImage
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Мой плеер")

        # Загружаем фоновое изображение
        self.background_img = PhotoImage(file="image/background.png")
        self.background_label = tk.Label(root, image=self.background_img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Создаем панель с кнопками управления
        control_frame = tk.Frame(root, bg="white", bd=5)
        control_frame.place(relx=0.5, rely=1, anchor="s")

        # Создаем кнопки управления с использованием Canvas
        self.previous_img = PhotoImage(file="image/previous_icon.png").subsample(2, 2)  # уменьшаем размер изображения
        self.previous_button = tk.Button(control_frame, image=self.previous_img, command=self.previous_music, bd=0)
        self.previous_button.grid(row=0, column=0, padx=10)

        self.play_img = PhotoImage(file="image/play_icon.png").subsample(2, 2)  # уменьшаем размер изображения
        self.play_button = tk.Button(control_frame, image=self.play_img, command=self.play_music, bd=0)
        self.play_button.grid(row=0, column=1, padx=10)

        self.stop_img = PhotoImage(file="image/stop_icon.png").subsample(2, 2)  # уменьшаем размер изображения
        self.stop_button = tk.Button(control_frame, image=self.stop_img, command=self.stop_music, bd=0)
        self.stop_button.grid(row=0, column=2, padx=10)

        self.next_img = PhotoImage(file="image/next_icon.png").subsample(2, 2)  # уменьшаем размер изображения
        self.next_button = tk.Button(control_frame, image=self.next_img, command=self.next_music, bd=0)
        self.next_button.grid(row=0, column=3, padx=10)

        # Инициализируем pygame mixer
        mixer.init()

        # Путь к папке с музыкой
        self.music_folder = "music"
        self.music_files = [os.path.join(self.music_folder, file) for file in os.listdir(self.music_folder) if file.endswith(".mp3")]
        self.current_index = 0

    def play_music(self):
        if not mixer.music.get_busy():
            mixer.music.load(self.music_files[self.current_index])
            mixer.music.play()

    def stop_music(self):
        mixer.music.stop()

    def next_music(self):
        self.current_index = (self.current_index + 1) % len(self.music_files)
        self.play_music()

    def previous_music(self):
        self.current_index = (self.current_index - 1) % len(self.music_files)
        self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
