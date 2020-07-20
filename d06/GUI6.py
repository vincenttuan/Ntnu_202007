import tkinter

def getValue(args):
    value = scale.get() # 或使用 args
    mystr.set(str(value/100) + ", " + args)

win = tkinter.Tk()
win.title('物聯網')
win.geometry("300x200")
# add Label
mystr = tkinter.StringVar()
label = tkinter.Label(win, textvariable=mystr)
mystr.set('LED')
label.config(fg='yellow', bg='red', font=('Arial', 30), width=15, height=2)
label.pack()
scale = tkinter.Scale(
    win,
    width=15,
    length=200,
    from_=0, to=100,
    orient=tkinter.HORIZONTAL,
    showvalue=True,
    command=getValue)

scale.pack()
win.mainloop()