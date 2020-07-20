import tkinter

win = tkinter.Tk()
win.title('登入畫面')
win.geometry("500x300")

label   = tkinter.Label(win, text="帳號", font=('Arial', 20))
label2  = tkinter.Label(win, text="密碼", font=('Arial', 20))
entry   = tkinter.Entry(win, font=('Arial', 20))
entry2  = tkinter.Entry(win, font=('Arial', 20))
button  = tkinter.Button(win, text="登入", font=('Arial', 20))
button2 = tkinter.Button(win, text="取消", font=('Arial', 20))

# 登入配置
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
button.grid(row=2, column=0)
button2.grid(row=2, column=1)

win.mainloop()