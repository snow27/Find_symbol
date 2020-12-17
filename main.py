from tkinter import *
import random
import tkinter.font as font
from PIL import ImageTk, Image

tk = Tk()
tk.geometry('800x800')
tk.config()
img_smile = ImageTk.PhotoImage(Image.open("smile.png"))
img_sad = ImageTk.PhotoImage(Image.open("sad.png"))


def buttons():
    Button(tk, width=3, height=1, bg="white", text=el[0], font=myFont, command=default_buttons).grid(row=1, column=0, padx=30, pady=30)
    Button(tk, width=3, height=1, bg="green", text=el[1], font=myFont, command=default_buttons).grid(row=1, column=1)
    Button(tk, width=3, height=1, bg="red", text=el[2], font=myFont, command=default_buttons).grid(row=1, column=2, padx=30, pady=30)


def emoticon(element):
    if element == "1":
        Label(tk, image=img_smile).grid(row=2, column=1)
    else:
        Label(tk, image=img_sad).grid(row=2, column=1)


def but1():
    buttons()
    emoticon(el[0])


def but2():
    buttons()
    emoticon(el[1])


def but3():
    buttons()
    emoticon(el[2])


el = ['1', '0', '0']

random.shuffle(el)
myFont = font.Font(size=90)
Label(tk, text='Please click Button:').grid(row=0, column=1)


def default_buttons():
    Button(tk, width=3, height=1, bg="white", font=myFont, command=but1).grid(row=1, column=0, padx=30, pady=30)
    Button(tk, width=3, height=1, bg="green", font=myFont, command=but2).grid(row=1, column=1)
    Button(tk, width=3, height=1, bg="red", font=myFont, command=but3).grid(row=1, column=2, padx=30, pady=30)

    random.shuffle(el)


default_buttons()
tk.mainloop()

