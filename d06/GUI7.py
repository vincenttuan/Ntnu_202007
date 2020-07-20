import tkinter
from tkinter import font
# using grid
# +------+-------------+
# | btn1 |     btn2    |
# +------+------+------+
# | btn3 | btn3 | btn4 |
# +-------------+------+
win = tkinter.Tk()
# tkFont.BOLD == 'bold'
myfont = font.Font(family='Helvetica', size=36, weight='bold')

btn1 = tkinter.Button(text='btn1', font=myfont)
btn2 = tkinter.Button(text='btn2', font=myfont)
btn3 = tkinter.Button(text='btn3', font=myfont)
btn4 = tkinter.Button(text='btn4', font=myfont)
btn5 = tkinter.Button(text='btn5', font=myfont)

win.rowconfigure((0,1), weight=1) # 列0, 列1 同步放大縮小
win.columnconfigure((0,1,2), weight=1) # 欄0, 欄1, 欄2 同步放大縮小

btn1.grid(row=0, column=0, columnspan=1, sticky='EWNS') # sticky='EWNS' 無縫填滿
btn2.grid(row=0, column=1, columnspan=2, sticky='EWNS')
btn3.grid(row=1, column=0, columnspan=1, sticky='EWNS')
btn4.grid(row=1, column=1, columnspan=1, sticky='EWNS')
btn5.grid(row=1, column=2, columnspan=1, sticky='EWNS')

win.mainloop()