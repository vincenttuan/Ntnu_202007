import tkinter
import d04.OpenWeatherDemo as w
from tkinter import messagebox

def msg():
    temp, feels_like, humidity, description = w.getWeather('taipei')
    mystr.set("氣溫: %.2f C\n體感: %.2f C\n濕度: %d %%\n%s" % (temp-273.15, feels_like-273.15, humidity, description))

def msg2():
    temp, feels_like, humidity, description = w.getWeather('taoyuan')
    mystr.set("氣溫: %.2f C\n體感: %.2f C\n濕度: %d %%\n%s" % (temp-273.15, feels_like-273.15, humidity, description))

def quit():
    win.quit()

win = tkinter.Tk()
win.title('現在天氣預報')
win.geometry("300x400")

mystr = tkinter.StringVar()
label = tkinter.Label(win, textvariable=mystr, font=('Arial', 20))
mystr.set("")
label.pack()

button1 = tkinter.Button(win, text="台北", command=msg, font=('Arial', 20))
button1.pack(side=tkinter.LEFT)

button3 = tkinter.Button(win, text="桃園", command=msg2, font=('Arial', 20))
button3.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="Cancel", command=quit, font=('Arial', 20))
button2.pack(side=tkinter.RIGHT)

win.mainloop()