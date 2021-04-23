from Lessions.Project22.main import *
from line import *
import tkinter as tk


# from tkinter import *


class main_box:
    def customer_in(t1,user_get_in):
        # l=Label(master,text="ASD").place(x=200,y=200)
        pass
    def a():
        master = Tk()
        master.geometry('900x900+500+10')
        master.config(bg='white')
        var1 = tk.IntVar()
        gg = str(var1.get())


        def heading():
            try:
                q1 = Label(master, text="A N K I T' S   C Y B E R   C A F E", font="Times 20 bold", bg='white')
                q1.place(x=1, y=1)
                wp = ['blue', 'green', 'red', 'gold2', 'midnight blue', 'brown4']
                q1.config(fg=wp[random.randrange(0, 6)])
                threading.Timer(0.4, heading).start()
            except Exception:
                pass

        heading()
        f = open("/Lessions/Project2/admin_history.txt", "r")
        for last_line in f: pass
        l1 = Label(master, text="Welcome: ",bg='white')
        l1.place(x=780, y=5)
        l2 = Label(master, text=last_line,bg='white')
        l2.place(x=850, y=4)
        l3 = Label(master, text="PC01: ",bg='white')
        l3.place(x=5, y=120)
        l4 = Label(master, text="PC02: ",bg='white')
        l4.place(x=5, y=170)
        l5 = Label(master,text="PC03: ",bg='white')
        l5.place(x=5, y=220)
        l6 = Label(master, text="PC04: ",bg='white')
        l6.place(x=5, y=270)
        l7 = Label(master, text="PC05: ",bg='white')
        l7.place(x=5, y=320)
        l8 = Label(master, text="PC06: ",bg='white')
        l8.place(x=5, y=370)
        l9 = Label(master, text="PC07: ",bg='white')
        l9.place(x=5, y=420)
        l10 = Label(master, text="PC08: ",bg='white')
        l10.place(x=5, y=470)
        l11 = Label(master, text="Name", bg='white',font="times 12 bold")
        l11.place(x=50, y=74)
        l12 = Label(master, text="Entry_Time", bg='white',font="times 12 bold")
        l12.place(x=200, y=74)
        l13 = Label(master, text="Total_Time", bg='white',font="times 12 bold")
        l13.place(x=300, y=74)
        l14 = Label(master, text=" ", bg='white',font="times 12 bold")
        l14.place(x=5, y=74)
        l15 = Label(master, text=" ", bg='white',font="times 12 bold")
        l15.place(x=5, y=74)
        l16 = Label(master, text=" ", bg='white',font="times 12 bold")
        l16.place(x=5, y=74)

        # li = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]

        A.line(1, 95)
        A.line(1, 145)
        A.line(1, 195)
        A.line(1, 245)
        A.line(1, 295)
        A.line(1, 345)
        A.line(1, 395)
        A.line(1, 445)
        A.line(1, 495)

        add = Button(master, text="Users List", command=lambda: [elements.users(0)])
        add.place(x=10, y=700)

        master.mainloop()

if __name__=="__main__":
    main_box.a()
