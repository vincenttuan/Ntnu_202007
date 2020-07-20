import tkinter
import tkinter.messagebox
def show_info():
    r = tkinter.messagebox.showinfo('對話框', 'This is [info] dialog')
    print(r) # 按下Ok --> ok
def show_askokcancel():
    r = tkinter.messagebox.askokcancel('對話框', 'This is [okcancel] dialog')
    print(r) # 按下ok --> True, cancel --> False
def show_askyesno():
    r = tkinter.messagebox.askyesno('對話框', 'This is [yesno] dialog')
    print(r) # 按下yes --> True, no --> False
def show_askyesnocancel():
    r = tkinter.messagebox.askyesnocancel('對話框', 'This is [yesnocancel] dialog')
    print(r) # 按下yes --> True, no --> False, cancel --> None
win = tkinter.Tk()
win.geometry("300x400")
button1 = tkinter.Button(win, text="Click me", command=show_info)
button1.pack(side=tkinter.LEFT)
button2 = tkinter.Button(win, text="Click me", command=show_askokcancel)
button2.pack(side=tkinter.LEFT)
button3 = tkinter.Button(win, text="Click me", command=show_askyesno)
button3.pack(side=tkinter.LEFT)
button4 = tkinter.Button(win, text="Click me", command=show_askyesnocancel)
button4.pack(side=tkinter.LEFT)
win.mainloop()