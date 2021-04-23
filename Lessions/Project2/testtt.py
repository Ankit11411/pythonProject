from tkinter import *

class A:
    def qqq():
        def destroyy():
            win.destroy()
            A.window()

        win2=Tk()
        win2.geometry('200x200')
        b2 = Button(win2, text="QQQQQQQQQQQQQQ", command=destroyy)
        b2.place(x=10, y=100)
        win2.mainloop()

    def window():
        global win
        win=Tk()
        win.geometry('400x400')
        b=Button(win,text="DES",command=A.qqq)
        b.place(x=10,y=100)
        win.mainloop()

A.window()