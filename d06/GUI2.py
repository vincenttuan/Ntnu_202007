import tkinter
from tkinter import messagebox

def msg():
    str.set("Hello")

def quit():
    win.quit()

win = tkinter.Tk()
win.title('我的小視窗')
win.geometry("300x400")

str = tkinter.StringVar()
label = tkinter.Label(win, textvariable=str, font=('Arial', 20))
str.set("")
label.pack()

button1 = tkinter.Button(win, text="OK", command=msg, font=('Arial', 20))
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="Cancel", command=quit, font=('Arial', 20))
button2.pack(side=tkinter.RIGHT)

win.mainloop()