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

def format_time(secs):
    mins = int(secs // 60)
    secs = int(secs % 60)
    return f"{mins:02d}:{secs:02d}"

def play_with_lyrics():
    pygame.mixer.music.load("Love Potions.mp3")
    pygame.mixer.music.play()

    lyrics = read_lyrics("lyrics.txt")
    start_time = time.time()
    i = 0

    while i < len(lyrics):
        if is_paused[0]:
            time.sleep(0.1)
            continue

        current_time = time.time() - start_time - paused_time[0]
        current_time_var.set(f"⏱ {format_time(current_time)} / {format_time(total_duration)}")

        if lyrics[i][0] is None or current_time >= lyrics[i][0]:
            type_text_gui(label, lyrics[i][1])
            next_line = lyrics[i+1][1] if i+1 < len(lyrics) else "---"
            next_lyric_var.set(f"Next: {next_line}")
            i += 1
        time.sleep(0.05)

    while pygame.mixer.music.get_busy():
        time.sleep(0.5)

def start():
    global start_timestamp
    start_timestamp = time.time()
    Thread(target=play_with_lyrics).start()

def toggle_pause():
    if not is_paused[0]:
        pygame.mixer.music.pause()
        pause_resume_button['text'] = "▶ Resume"
        is_paused[0] = True
        paused_timestamp[0] = time.time()
    else:
        pygame.mixer.music.unpause()
        pause_resume_button['text'] = "⏸ Pause"
        is_paused[0] = False
        paused_time[0] += time.time() - paused_timestamp[0]

# Inisialisasi pygame
pygame.mixer.init()
pygame.mixer.music.load("Love Potions.mp3")
total_duration = pygame.mixer.Sound("Love Potions.mp3").get_length()

# UI Tkinter
window = tk.Tk()
window.title("Love Potions Lyrics Player")
window.geometry("700x300")
window.configure(bg="black")

label = tk.Label(window, text="", font=("Courier", 16), fg="lime", bg="black", wraplength=650, justify="center")
label.pack(pady=10)

current_time_var = tk.StringVar()
current_time_label = tk.Label(window, textvariable=current_time_var, font=("Arial", 10), fg="white", bg="black")
current_time_label.pack()

next_lyric_var = tk.StringVar()
next_lyric_label = tk.Label(window, textvariable=next_lyric_var, font=("Arial", 10), fg="gray", bg="black")
next_lyric_label.pack()

control_frame = tk.Frame(window, bg="black")
control_frame.pack(pady=10)  # Tambahkan sedikit jarak dari atas

play_button = tk.Button(control_frame, text="▶ Play", font=("Arial", 12), command=start)
play_button.grid(row=0, column=0, padx=10)

pause_resume_button = tk.Button(control_frame, text="⏸ Pause", font=("Arial", 12), command=toggle_pause)
pause_resume_button.grid(row=0, column=1, padx=10)

# Frame tombol tambahan tepat di bawah control_frame
extra_control_frame = tk.Frame(window, bg="black")
extra_control_frame.pack(pady=10)  # Tidak perlu side="bottom"

resume_button = tk.Button(extra_control_frame, text="▶ Resume", font=("Arial", 12))
resume_button.grid(row=0, column=0, padx=10)

restart_button = tk.Button(extra_control_frame, text="⏮ Restart", font=("Arial", 12))
restart_button.grid(row=0, column=1, padx=10)

skip_button = tk.Button(extra_control_frame, text="⏭ Skip to Verse...", font=("Arial", 12))
skip_button.grid(row=0, column=2, padx=10)

is_paused = [False]
paused_timestamp = [0]
paused_time = [0]

window.mainloop()
