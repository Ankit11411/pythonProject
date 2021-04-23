from tkinter import *


def square():
    sq = int(e1.get())
    sq1 = sq * sq
    ol.config(text=str(sq1))


def squareroot():
    sr = int(e1.get())
    sr1 = sr ** 0.5
    ol.config(text=str(sr1))


def Factorial():
    ans = 1
    sr = int(e1.get())
    for i in range(sr):
        while sr != 0:
            ans = ans * sr
            sr = sr - 1
    ol.config(text=str(ans))


def Primeno():
    n = int(e1.get())
    if n % 2 == 0 or n % 3 == 0:
        ol.config(text='NotPrime')
    else:
        ol.config(text='Prime')


w = Tk()
w.title("Math")
w.geometry('300x300')

l1 = Label(w, text="Find Square, Square root,factorial, \nand prime number of a number")
l1.place(x=50, y=40)

l2 = Label(w, text="Enter no.")
l2.place(x=50, y=100)

e1 = Entry(w, width=15)
e1.place(x=120, y=100)

b1 = Button(w, text="Square", command=square)
b1.place(x=60, y=160)

b2 = Button(w, text="Squareroot", command=squareroot)
b2.place(x=120, y=160)

b3 = Button(w, text="Factorial", command=Factorial)
b3.place(x=200, y=160)

b4 = Button(w, text="PrimeNo", command=Primeno)
b4.place(x=10, y=160)

ol = Label(w)
ol.place(x=100, y=200)

w.mainloop()
