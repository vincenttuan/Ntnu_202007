import tkinter
import d04.OpenWeatherDemo as w
from tkinter import messagebox

def msg():
    temp, feels_like, humidity, description = w.getWeather('taipei')
    mystr.set("%.2f C" % (temp-273.15))

def quit():
    win.quit()

win = tkinter.Tk()
win.title('現在天氣預報')
win.geometry("300x400")

mystr = tkinter.StringVar()
label = tkinter.Label(win, textvariable=mystr, font=('Arial', 20))
mystr.set("")
label.pack()

button1 = tkinter.Button(win, text="OK", command=msg, font=('Arial', 20))
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="Cancel", command=quit, font=('Arial', 20))
button2.pack(side=tkinter.RIGHT)

win.mainloop()