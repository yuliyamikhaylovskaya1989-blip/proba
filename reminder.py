from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import pygame
import time


t = None


def set():
    global t
    rem = sd.askstring("Время напоминания", "Введите время в формате ЧЧ:ММ (24-часовой формат)")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            if 0<=hour>=23 or 0<=minute>=59:
                mb.showerror("Ошибка", "Не вводите время с часами меньше 0 и больше 23, а минутами больше 59 и меньше 0.")
            #print(now)
            dt = now.replace(hour=hour, minute=minute)
            #print(dt)
            t = dt.timestamp()
            #print(t)
            label.config(text=f"Напоминание установлено на:{hour:02}:{minute:02}")
        except ValueError:
            mb.showerror("Ошибка", "Неверный формат времени")
        except Exception as e:
            mb.showerror("Ошибка", f"Неизвестная ошибка {e}")


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = None
    window.after(10000, check)


def play_snd():
    global music
    music=True
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()

def stop_music():
    global music
    music=True

window = Tk()
window.title("Напоминание")
label = Label(text="Установите напоминание", font=("Arial", 14))
label.pack(pady=10)
set_button = Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)
stop_button=Button(text="Остановить музыку", command=stop_music)
stop_button.pack(pady=10)

check()
window.mainloop()