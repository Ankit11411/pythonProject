from tkinter import *

w = Tk()
w.geometry('300x300')
w.title('`EasyMath')


def Factorial():
    ans = 1
    sr = int(e.get())
    for i in range(sr):
        while sr != 0:
            ans = ans * sr
            sr = sr - 1
    ol.config(text=str(ans))


def Square():
    sq = int(e.get())
    sq1 = sq * sq
    ol.config(text=str(sq1))


def SquareRoot():
    sr = int(e.get())
    sr1 = sr ** 0.5
    ol.config(text=str(sr1))


v1 = IntVar()

b3 = Button(w, text="Find", width=5, command=Factorial)
b3.place(x=110, y=100)

l1 = Label(w, text='Select Which operation you want to perform')
l1.place(x=30, y=50)

r1 = Radiobutton(w, text='Factorial', value=1, variable=v1, command=b3)
r1.place(x=30, y=70)

r2 = Radiobutton(w, text='Square', value=2, variable=v1, command=b3)
r2.place(x=120, y=70)

r3 = Radiobutton(w, text='SquareRoot', value=3, variable=v1, command=b3)
r3.place(x=210, y=70)

e = Entry(w, width=10)
e.place(x=35, y=105)

ol = Label(w)
ol.place(x=100, y=200)

w.mainloop()
