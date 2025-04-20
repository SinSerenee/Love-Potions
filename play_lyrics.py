import time
import pygame
import os
import tkinter as tk
from threading import Thread

def read_lyrics(file_path):
    lyrics = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip() and line.startswith('['):
                time_str, text = line.strip().split('] ')
                time_str = time_str[1:]
                mins, secs = time_str.split(':')
                total_seconds = int(mins) * 60 + float(secs)
                lyrics.append((total_seconds, text))
            else:
                lyrics.append((None, line.strip()))
    return lyrics

def type_text_gui(label, text, delay=0.03):
    label['text'] = ''
    for i in range(len(text)):
        label['text'] += text[i]
        time.sleep(delay)

def play_with_lyrics():
    pygame.mixer.music.load("Love Potions.mp3")
    pygame.mixer.music.play()

    lyrics = read_lyrics("lyrics.txt")
    start_time = time.time()
    i = 0

    while i < len(lyrics):
        current_time = time.time() - start_time
        if lyrics[i][0] is None or current_time >= lyrics[i][0]:
            type_text_gui(label, lyrics[i][1])
            i += 1
        time.sleep(0.05)

    while pygame.mixer.music.get_busy():
        time.sleep(0.5)

def start():
    Thread(target=play_with_lyrics).start()

# Inisialisasi pygame
pygame.mixer.init()

# UI Tkinter
window = tk.Tk()
window.title("Love Potions Lyrics")
window.geometry("600x200")
window.configure(bg="black")

label = tk.Label(window, text="", font=("Courier", 16), fg="lime", bg="black", wraplength=550, justify="center")
label.pack(pady=50)

button = tk.Button(window, text="Play", font=("Arial", 12), command=start)
button.pack()

window.mainloop()