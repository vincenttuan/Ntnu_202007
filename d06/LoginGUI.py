import tkinter

win = tkinter.TK()
win.title('登入畫面')
win.geometry("300x400")

label   = tkinter.Label(win, text="帳號", font=('Arial', 20))
label2  = tkinter.Label(win, text="密碼", font=('Arial', 20))
entry   = tkinter.Entry(win)
entry2  = tkinter.Entry(win)
button  = tkinter.Button(win, text="登入")
button2 = tkinter.Button(win, text="取消")

win.mainloop()