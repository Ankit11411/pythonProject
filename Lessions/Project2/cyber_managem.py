from tkinter import messagebox
from tkinter import *
from line import *
import tkinter.ttk
from add_new import *
# from select_user import *
import random
import threading


class adm:
    def search():
        def find1():
            pass

        def find2():
            pass

        def take():
            global m
            ulist.destroy()
            adm.users()
            m = 1

        sr = Tk()
        sr.geometry("200x120")
        en = Entry(sr, width=18, font="Times 12 bold")
        en.place(x=10, y=10)

        byname = Button(sr, text="By Name", width=8, command=find1)
        byname.place(x=10, y=50)
        byid = Button(sr, text="By Id", width=8, command=find2)
        byid.place(x=80, y=50)
        show = Button(sr, text="Find", width=8, command=take)
        show.place(x=30, y=80)
        sr.mainloop()

    def users():
        global ulist
        def aaa():
            f = open("user_history.txt", "r")
            for last_line2 in f:
                pass
            print("AAA", last_line2)
            adm.admin_page()

        def Addd():
            global user_get_in
            user_get_in = users.get(users.curselection())
            # print(user_get_in)
            f = open("user_history.txt", "a")
            f.write(user_get_in + "\n")



        ulist = Tk()
        ulist.geometry("300x400")

        conn = my.connect(username="root", password="root", host="localhost", database='user_data')
        cur = conn.cursor()

        q = "select * from user"

        cur.execute(q)
        records = cur.fetchall()

        users = Listbox(ulist, height="20")

        for row in records:
            users.insert(row[0], row[1])
        users.place(x=10, y=10)
        try:
            users.select_set(m)
        except Exception:
            pass
        # gg = users.get()
        # print(gg)
        def qqqq():
            print(m)
        conn.close()
        add = Button(ulist, text="Add", width=15, command=lambda: [Addd(), master.destroy(), aaa(), ])
        add.place(x=160, y=30)
        qqq = Button(ulist, text="qqq", width=15, command=lambda: [qqqq()])
        qqq.place(x=160, y=90)

        searchh = Button(ulist, text="Search", width=15, command=lambda: [adm.search(), ])
        searchh.place(x=160, y=60)

        ulist.mainloop()

    def admin_page():

        global master
        master = Tk()
        master.geometry('900x900+500+10')
        master.config(bg='white')
        f = open("admin_history.txt", "r")
        for last_line in f:
            pass
        last_line = str(last_line)

        f1 = open("user_history.txt", "r")
        for last_line2 in f1:
            pass

        def Z():
            try:
                q1 = Label(master, text="A N K I T' S   C Y B E R   C A F E", font="Times 20 bold", bg='white')
                q1.place(x=1, y=1)
                wp = ['blue', 'green', 'red', 'gold2', 'midnight blue', 'brown4']
                q1.config(fg=wp[random.randrange(0, 6)])
                threading.Timer(0.4, Z).start()
            except Exception:
                pass

        Z()
        A.line(1, 30)
        A.line(1, 65)

        l1 = Label(master, text="Welcome: ", bg='white').place(x=780, y=5)
        l2 = Label(master, text=last_line, bg='white').place(x=850, y=4)

        l3 = Label(master, text=last_line2, bg="white").place(x=10, y=100)

        no = Label(master, text="PC Number", bg='white').place(x=5, y=50)
        pcno = Label(master, text="Id.No", bg='white').place(x=75, y=50)
        Name = Label(master, text="Name", bg='white').place(x=140, y=50)
        Contact = Label(master, text="Contact", bg='white').place(x=275, y=50)
        ID = Label(master, text="ID Proof", bg='white').place(x=375, y=50)

        # BUTTON
        add = Button(master, text="Users List", command=lambda: [adm.users()])
        add.place(x=10, y=700)
        new = Button(master, text="Add New", command=reg.new)
        new.place(x=100, y=700)

        master.mainloop()


try:
    adm.admin_page()
except Exception:
    messagebox.showinfo("Something's Wrong","Please Restart")
finally:
    f1 = open("user_history.txt", "w")
    f1.write("None\n")
