from tkinter import *
from tkinter import messagebox
import re
import math


def click():
    global a, b
    try:
        gg = v.get()
        print(gg)
        a = int(e1.get())
        b = int(e2.get())
        if gg == 1:
            c = a * b
            d.config(text=str(c))
            z.config(text='X')
        elif gg == 2:
            c = a + b
            d.config(text=str(c))
            z.config(text='+')
        elif gg == 3:
            c = a - b
            d.config(text=str(c))
            z.config(text='-')
        elif gg == 4:
            c = a / b
            d.config(text=str(c))
            z.config(text='÷')
        elif gg == 5:
            z.config(text='Fac')
            ans = 1
            li=[]
            for j in range(a, b + 1):
                for i in range(a, 1, -1):
                    ans = ans * i
                li.append(ans)
                d.config(text=str(li))
                a = a + 1
                ans = 1

        elif gg == 6:
            c = None
            d.config(text=str(c))
            z.config(text='X')
        elif gg == 7:
            c = None
            d.config(text=str(c))
            z.config(text='X')
        elif gg == 8:
            c = a % b
            d.config(text=str(c))
            z.config(text='%')

    except ValueError:
        messagebox.showerror("Show", "Enter Numbers First")


cal = Tk()
cal.geometry('500x650')
cal.title('Calculator')
v = IntVar()

l1 = Label(cal, text="NUMBER1", font="Helvetica 24 ").place(x=50, y=40)
e1 = Entry(cal, width=3, font="Helvetica 44 bold")
e1.place(x=80, y=90)

l2 = Label(cal, text="NUMBER2", font="Helvetica 24 ").place(x=300, y=40)
e2 = Entry(cal, width=3, font="Helvetica 44 bold")
e2.place(x=330, y=90)

r1 = Radiobutton(cal, text='X', font="Helvetica 44 bold", indicator=0, value=1, width=2, variable=v, command=click)
r1.place(x=70, y=200)
r2 = Radiobutton(cal, text='+', font="Helvetica 44 bold", indicator=0, value=2, width=2, variable=v, command=click)
r2.place(x=170, y=200)
r3 = Radiobutton(cal, text='-', font="Helvetica 44 bold", indicator=0, value=3, width=2, variable=v, command=click)
r3.place(x=270, y=200)
r4 = Radiobutton(cal, text='÷', font="Helvetica 44 bold", indicator=0, value=4, width=2, variable=v, command=click)
r4.place(x=370, y=200)

r5 = Radiobutton(cal, text='Fact', font="Helvetica 44 bold", indicator=0, value=5, width=2, variable=v, command=click)
r5.place(x=70, y=350)
r6 = Radiobutton(cal, text='cos', font="Helvetica 44 bold", indicator=0, value=6, width=2, variable=v, command=click)
r6.place(x=170, y=350)
r7 = Radiobutton(cal, text='tan', font="Helvetica 44 bold", indicator=0, value=7, width=2, variable=v, command=click)
r7.place(x=270, y=350)
r8 = Radiobutton(cal, text='%', font="Helvetica 44 bold", indicator=0, value=8, width=2, variable=v, command=click)
r8.place(x=370, y=350)

l3 = Label(cal, text='Answer: ', font="Helvetica 24 bold").place(x=1, y=500)
d = Label(cal, font="Helvetica 24 bold")
d.place(x=130, y=500)

z = Label(cal, font="Helvetica 44 bold")
z.place(x=220, y=90)

cal.mainloop()
