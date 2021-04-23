from tkinter import messagebox
import tkinter.ttk
import mysql.connector as my
from datetime import datetime

import time
import datetime
from menubar import *
import random
import threading
from line import *
import tkinter as tk
from add_new import *


class main_box:
    dict = {1: 'empty', 2: 'empty', 3: 'empty', 4: 'empty', 5: 'empty', 6: 'empty', 7: 'empty', 8: 'empty'}
    global b
    b = 0

    def clock(counter, l3, count):
        global string
        tt = datetime.datetime.fromtimestamp(counter)
        string = tt.strftime("%H:%M:%S")
        # rt = string
        l3.config(text=string)
        l3.after(1000, lambda: [main_box.clock(counter, l3, count)])
        counter += 1

    def customer_in(t1, user_get_in):
        clist.destroy()
        global dict2
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
                main_box.clock(counter, l3, count)
                main_box.dict[count] = user_get_in
                break
            print("ASD")
            count = count + 1
            a = a + 50


    def users(id):
        global clist, user_listbox
        def user_login_info():
            t1 = time.strftime('%H:%M:%S', time.localtime())
            user_get_in = users_listbox.get(users_listbox.curselection())
            main_box.customer_in(t1, user_get_in)

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
        print(id)
        users_listbox.select_set(id)
        conn.close()

        add = Button(clist, text="Add", width=15, command=lambda: [user_login_info()])
        add.place(x=160, y=30)


        clist.mainloop()

    def a():
        global master
        master = Tk()
        master.title("Cyber Cafe Management System")
        master.geometry('900x700+500+10')
        master.config(bg='white')
        var1 = tk.IntVar()
        gg = str(var1.get())



        l11 = Label(master, text="Name", bg='white', font="times 12 bold")
        l11.place(x=50, y=74)
        l12 = Label(master, text="Entry_Time", bg='white', font="times 12 bold")
        l12.place(x=200, y=74)
        l13 = Label(master, text="Total_Time", bg='white', font="times 12 bold")
        l13.place(x=300, y=74)

        add = Button(master, width=15, height=3, font='times 20 bold', text="Customer List",
                     command=lambda: [main_box.users(0)])
        add.place(x=600, y=550)


        master.mainloop()


main_box.a()


