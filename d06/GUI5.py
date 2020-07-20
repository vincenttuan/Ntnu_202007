import tkinter
import d04.OpenWeatherDemo as w
from tkinter import messagebox

def msg():
    city = entry.get()
    temp, feels_like, humidity, description = w.getWeather(city)
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

entry = tkinter.Entry(win, justify=tkinter.CENTER, font=('Arial', 20))
entry.pack()

button1 = tkinter.Button(win, text="天氣", command=msg, font=('Arial', 20))
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="Cancel", command=quit, font=('Arial', 20))
button2.pack(side=tkinter.RIGHT)

win.mainloop()