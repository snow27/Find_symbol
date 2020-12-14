from tkinter import *
import random
import tkinter.font as font

tk = Tk()
tk.geometry('800x600')
tk.config()


def check_sym(tot, element):
    if element == "$":
        tot += 1
    else:
        tot -= 1
    return tot


total = 10


def but1():
    global total
    Button(tk, width=3, height=1, bg="white", text=el[0], font=myFont, command=default_buttons).grid(row=1, column=0,
                                                                                                     padx=30, pady=30)
    total = check_sym(total, el[0])
    Label(tk, text=str(total)).grid(row=2, column=1)


def but2():
    Button(tk, width=3, height=1, bg="green", text=el[1], font=myFont, command=default_buttons).grid(row=1, column=1)


def but3():
    Button(tk, width=3, height=1, bg="red", text=el[2], font=myFont, command=default_buttons).grid(row=1, column=2,
                                                                                                   padx=30, pady=30)


el = ['$', '0', '0']
random.shuffle(el)
myFont = font.Font(size=90)
Label(tk, text='Please click Button:').grid(row=0, column=1)


def default_buttons():
    Button(tk, width=3, height=1, bg="white", font=myFont, command=but1).grid(row=1, column=0, padx=30, pady=30)
    Button(tk, width=3, height=1, bg="green", font=myFont, command=but2).grid(row=1, column=1)
    Button(tk, width=3, height=1, bg="red", font=myFont, command=but3).grid(row=1, column=2, padx=30, pady=30)

    random.shuffle(el)


Label(tk, text=str(total)).grid(row=2, column=1)
Button(tk, text="Continued", bg='blue', command=default_buttons).grid(row=3, column=1)

default_buttons()
tk.mainloop()









