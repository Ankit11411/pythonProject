from tkinter import messagebox
import tkinter.ttk
import mysql.connector as my
from datetime import datetime

import time
import datetime
# from menubar import *
import random
import threading
# from line import *
from tkinter import *
# from add_new import *


class main_box:
    dict = {1: 'empty', 2: 'empty', 3: 'empty', 4: 'empty', 5: 'empty', 6: 'empty', 7: 'empty', 8: 'empty'}

    def clock(counter, l3):
        tt = datetime.datetime.fromtimestamp(counter)
        string = tt.strftime("%H:%M:%S")
        display = string
        l3.config(text=display)
        l3.after(1000, lambda: [main_box.clock(counter, l3)])
        counter += 1

    def customer_in(t1, user_get_in, master):

        a = 120
        count = 1
        for live in main_box.dict.values():
            if live == user_get_in:
                break

            if live == 'empty':
                l = Label(master, text=user_get_in, bg='yellow')
                l.place(x=50, y=a)
                l2 = Label(master, text=t1, bg='yellow')
                l2.place(x=200, y=a)
                l3 = Label(master, bg='yellow')
                l3.place(x=300, y=a)
                counter = 66600
                main_box.clock(counter, l3)
                b1 = Button(master, text="Stop Session", command=lambda: [stop(master)])
                b1.place(x=500, y=a)

                def stop(master):
                    b2 = Button(master, text="Print Bill", command=lambda: [])
                    b2.place(x=650, y=a)
                    b3 = Button(master, text="Remove", command=lambda: [])
                    b3.place(x=800, y=a)

                main_box.dict[count] = user_get_in
                print(main_box.dict.values())
                print(count)
                break
            count = count + 1
            a = a + 50
        # else:
        #     messagebox.showinfo("Exist!","Customer already allocated!")

    def history():
        f = open("user_history.txt", "r")
        notepad.new(f.read())

    def search():
        def name():
            global tofind
            tofind = str(en.get())
            conn = my.connect(username="root", password="root", host="localhost", database='user_data')
            cur = conn.cursor()
            q = "select * from user"
            cur.execute(q)
            records = cur.fetchall()
            id = 0
            reversed_list = records[::-1]
            for row in records:
                if row[1] == tofind:
                    temp = str(row[1] + "'s ID IS " + str(row[0]))
                    messagebox.showinfo("Found", temp)
                    clist.destroy()
                    main_box.users(id, 0)
                    break
                elif row[0] != tofind and row[0] == reversed_list[0][0]:
                    messagebox.showinfo("", "Not Found")
                id = id + 1

        def idno():
            try:
                global tofind
                tofind = int(en.get())
                conn = my.connect(username="root", password="root", host="localhost", database='user_data')
                cur = conn.cursor()
                q = "select * from user"
                cur.execute(q)
                records = cur.fetchall()
                id = 0
                reversed_list = records[::-1]
                for row in records:
                    if row[0] == tofind:
                        temp = str(str(row[0]) + "'s NAME IS " + str(row[1]))
                        messagebox.showinfo("Found", temp)
                        clist.destroy()
                        main_box.users(id, 0)
                        break
                    elif row[0] != tofind and row[0] == reversed_list[0][0]:
                        messagebox.showinfo("", "Not Found")
                    id = id + 1
            except Exception:
                messagebox.showinfo("", "Id should be in numbers")

        srch = Tk()
        srch.geometry("180x100+1200+300")
        srch.title("Search")

        en = Entry(srch, width=18, font="Times 12 bold")
        en.place(x=10, y=10)

        byname = Button(srch, text="By Name", width=8, command=name)
        byname.place(x=10, y=50)
        byid = Button(srch, text="By Id", width=8, command=idno)
        byid.place(x=80, y=50)
        srch.mainloop()

    def users(id, master):
        global clist, user_listbox

        def detail():
            det = tkinter.Toplevel()
            det.geometry("1500x440")
            user_get_in = users_listbox.get(users_listbox.curselection())

            conn = my.connect(username="root", password="root", host="localhost", database='user_data')
            cur = conn.cursor()
            q = "select * from user"
            cur.execute(q)
            records = cur.fetchall()
            for row in records:
                if str(user_get_in) == str(row[1]):
                    d_id = str(row[0])
                    d_name = row[1]
                    d_contact = row[2]
                    d_address = row[3]
            img = PhotoImage(file=d_address)
            img = img.zoom(7)
            img = img.subsample(10)
            panel = Label(det, image=img)
            panel.place(x=1, y=1)
            conn.close()

            label11 = Label(det, text="Customer ID:", font="Times 18 bold")
            label11.place(x=950, y=50)
            label22 = Label(det, text="Name:", font="Times 18 bold")
            label22.place(x=950, y=100)
            label33 = Label(det, text="Contact Number:", font="Times 18 bold")
            label33.place(x=950, y=150)

            label1 = Label(det, text=d_id, font="Times 20 bold")
            label1.place(x=1200, y=50)
            label2 = Label(det, text=d_name, font="Times 20 bold")
            label2.place(x=1200, y=100)
            label3 = Label(det, text=d_contact, font="Times 20 bold")
            label3.place(x=1200, y=150)

            det.mainloop()

        def user_login_info(master):
            # try:
            t1 = time.strftime('%H:%M:%S', time.localtime())
            t2 = datetime.datetime.today().strftime('%d/%m/%Y')
            user_get_in = users_listbox.get(users_listbox.curselection())
            f = open("user_history.txt", "a")
            f.write(user_get_in + " (Time=" + str(t1) + ", Date=" + str(t2) + ")\n")
            main_box.customer_in(t1, user_get_in, master)

            # except Exception:
            #     messagebox.showinfo("Error!", "Select Name from list first")

        clist = Tk()
        clist.geometry("300x350+900+300")
        clist.title("Customer List")

        conn = my.connect(username="root", password="root", host="localhost", database='user_data')
        cur = conn.cursor()
        q = "select * from user"
        cur.execute(q)
        records = cur.fetchall()
        users_listbox = Listbox(clist, height="20")
        for row in records:
            users_listbox.insert(row[0], row[1])
        users_listbox.place(x=10, y=10)
        users_listbox.select_set(id)
        conn.close()

        add = Button(clist, text="Add", width=15, command=lambda: [user_login_info(master)])
        add.place(x=160, y=30)

        searchh = Button(clist, text="Search", width=15, command=lambda: [main_box.search(), ])
        searchh.place(x=160, y=60)

        hist = Button(clist, text="Customer History", width=15, command=lambda: [main_box.history()])
        hist.place(x=160, y=90)

        det = Button(clist, text="Detail", width=15, command=lambda: [detail()])
        det.place(x=160, y=120)

        clist.mainloop()

    def a():
        global master
        master = Tk()
        master.title("Cyber Cafe Management System")
        master.geometry('900x700+500+10')
        master.config(bg='white')
        # var1 = tk.IntVar()
        gg = str(var1.get())

        def heading():
            try:
                q1 = Label(master, text="A N K I T' S   C Y B E R   C A F E", font="Times 20 bold", bg='white')
                q1.place(x=230, y=1)
                wp = ['blue', 'green', 'red', 'gold2', 'midnight blue', 'brown4']
                q1.config(fg=wp[random.randrange(0, 6)])
                threading.Timer(0.4, heading).start()
            except Exception:
                pass

        heading()
        f = open("/Project3/admin_history.txt", "r")
        for last_line in f: pass
        l1 = Label(master, text="Welcome: ", bg='white')
        l1.place(x=780, y=5)
        l2 = Label(master, text=last_line, bg='white')
        l2.place(x=850, y=4)
        l3 = Label(master, text="PC01: ", bg='white')
        l3.place(x=5, y=120)
        l4 = Label(master, text="PC02: ", bg='white')
        l4.place(x=5, y=170)
        l5 = Label(master, text="PC03: ", bg='white')
        l5.place(x=5, y=220)
        l6 = Label(master, text="PC04: ", bg='white')
        l6.place(x=5, y=270)
        l7 = Label(master, text="PC05: ", bg='white')
        l7.place(x=5, y=320)
        l8 = Label(master, text="PC06: ", bg='white')
        l8.place(x=5, y=370)
        l9 = Label(master, text="PC07: ", bg='white')
        l9.place(x=5, y=420)
        l10 = Label(master, text="PC08: ", bg='white')
        l10.place(x=5, y=470)
        l11 = Label(master, text="Name", bg='white', font="times 12 bold")
        l11.place(x=50, y=74)
        l12 = Label(master, text="Entry_Time", bg='white', font="times 12 bold")
        l12.place(x=200, y=74)
        l13 = Label(master, text="Total_Time", bg='white', font="times 12 bold")
        l13.place(x=300, y=74)
        l14 = Label(master, text=" ", bg='white', font="times 12 bold")
        l14.place(x=5, y=74)
        l15 = Label(master, text=" ", bg='white', font="times 12 bold")
        l15.place(x=5, y=74)
        l16 = Label(master, text=" ", bg='white', font="times 12 bold")
        l16.place(x=5, y=74)

        # li = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]

        A.line(1, 95)
        A.line(1, 145)
        A.line(1, 195)
        A.line(1, 245)
        A.line(1, 295)
        A.line(1, 345)
        A.line(1, 395)
        A.line(1, 395)
        A.line(1, 445)
        A.line(1, 495)

        add = Button(master, width=15, height=3, font='times 20 bold', text="Customer List",
                     command=lambda: [main_box.users(0, master)])
        add.place(x=600, y=550)

        regn = Button(master, width=15, height=3, font='times 20 bold', text="New Customer",
                      command=lambda: [reg.new()])
        regn.place(x=10, y=550)

        deln = Button(master, width=15, height=3, font='times 20 bold', text="Delete Customer",
                      command=lambda: [reg.delete()])
        deln.place(x=315, y=550)

        master.mainloop()


main_box.a()

# *******************************************************************************
'''
from tkinter import messagebox
from tkinter import *
# from line import *
import tkinter.ttk
# from add_new import *
# from select_user import *
import random
import threading
import mysql.connector as my
import time
import datetime
from menubar import *
from tkinter import ttk
from PIL import Image, ImageTk











# elements.users(0)
'''
