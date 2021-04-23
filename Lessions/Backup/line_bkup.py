from tkinter import *
import random
import threading

class A:
    def dark_mode(li, master,var1,dark):
        if (var1.get() == 1):
            dark.config(text='Light Mode',fg='black')
            master.config(bg='black')
            for i in range(10):
                li[i].config(bg='black', fg='white')


        else:
            dark.config(text='Dark Mode',fg='white')
            master.config(bg='white')
            for i in range(10):
                li[i].config(bg='white', fg='black')



    def line(a,b,var1):
        try:
            # l = Label(text="------------------------------------------------------------------------------------------"
            #                "------------------------------------------------------------------------------------------"
            #                "-----------------------------------------", font='Times 10', bg='black')
            # l.place(x=a, y=b)
            # wp = ['blue', 'green', 'red', 'gold2', 'midnight blue', 'brown4']
            #
            # l.config(fg=wp[random.randrange(0, 6)])
            # threading.Timer(0.4, lambda: (A.line(a, b))).start()
            print(var1.get())
            if (var1.get() == 1):
                print("QQQQQQQQQQQQQQQQQQQQQQQQ")
                l = Label(text="------------------------------------------------------------------------------------------"
                               "------------------------------------------------------------------------------------------"
                               "-----------------------------------------", font='Times 10', bg='black')
                l.place(x=a, y=b)
                wp = ['blue', 'green', 'red', 'gold2', 'midnight blue', 'brown4']

                l.config(fg=wp[random.randrange(0, 6)])
                threading.Timer(0.4, lambda :(A.line(a,b,1))).start()
            else:
                l = Label(
                    text="------------------------------------------------------------------------------------------"
                         "------------------------------------------------------------------------------------------"
                         "-----------------------------------------", font='Times 10', bg='white')
                l.place(x=a, y=b)
                wp = ['blue', 'green', 'red', 'gold2', 'midnight blue', 'brown4']

                l.config(fg=wp[random.randrange(0, 6)])
                threading.Timer(0.4, lambda: (A.line(a, b,1))).start()

        except Exception:
            pass
            # l = Label(text="------------------------------------------------------------------------------------------"
            #                            "------------------------------------------------------------------------------------------"
            #                            "-----------------------------------------", font='Times 10', bg='white').place(x=a, y=b)

