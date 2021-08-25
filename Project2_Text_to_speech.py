import tkinter as tk
from gtts import gTTS
import os

window = tk.Tk()
window.title("Text to Speech")
window.config(bg="Antiquewhite1")
window.geometry('500x250')

message = tk.StringVar()

tk.Label(window,text="Text to Speech Converter",font= '"times new roman" 16 bold ', bg="salmon1").pack()

tk.Label(window, text = "Enter Message", font = '"times new roman" 12 bold').place(x=100,y=60)
tk.Entry(window, font = '"times new roman" 12', textvariable = message).place(x=240,y=60)

def play():
    language = "en"
    myobj = gTTS(text = message.get(), lang = language, slow = False)
    myobj.save("audio.mp3")
    os.system("audio.mp3")

tk.Button(window, text = "SUBMIT", font = '"times new roman" 12 bold', command=play, width=10, bg="cyan2").place(x=190,y=160)

window.mainloop()


