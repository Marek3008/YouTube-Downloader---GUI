from tkinter import *
from pytube import YouTube


window = Tk()
window.title("YT Downloader")
window.geometry("500x500")


def potvrdit():
    global nazov
    global yt
    global streams
    url = str(entry1.get())
    yt = YouTube(url)
    nazov = yt.title
    streams = yt.streams.filter(only_audio=True)
    label2.config(text=nazov)
    for _stream in streams:
        i = 0
        listbox1.insert(i, _stream)
        
def stiahni():
    itag = int(entry2.get())
    stream = yt.streams.get_by_itag(itag)
    stream.download()


label1 = Label(window, text="Zadaj URL", padx=40, font=("Arial", 15))
label1.grid(row=0, column=0)

button1 = Button(window, text="Potvrdiť", command=potvrdit)
button1.grid(row=1, column=1, pady=10)

label2 = Label(window, text=" ")
label2.grid(row=2, column=1)

label3 = Label(window, text="ITAG:", font=("Arial", 15))
label3.grid(row=4, column=0)

entry1 = Entry(window)
entry1.grid(row=0, column=1)

entry2 = Entry(window)
entry2.grid(row=4, column=1, pady=20)

button2 = Button(window, text="Stiahni", command=stiahni)
button2.grid(row=5, column=1, pady=10)

listbox1 = Listbox(window)
listbox1.grid(row=3, column=1, padx=20, pady=5)



window.mainloop()