import tkinter

win = tkinter.Tk()
win.title('我的小視窗')
win.geometry("300x400")

label = tkinter.Label(win, text="Hello")
label.pack()

button1 = tkinter.Button(win, text="OK")
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="Cancel")
button2.pack(side=tkinter.RIGHT)

win.mainloop()