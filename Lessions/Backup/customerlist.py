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
# from menubar import *
from tkinter import ttk
from PIL import Image, ImageTk


class elements:

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
                    temp=str(row[1]+"'s ID IS "+str(row[0]))
                    messagebox.showinfo("Found",temp)
                    clist.destroy()
                    elements.users(id)
                    break
                elif row[0]!=tofind and row[0]==reversed_list[0][0]:
                    messagebox.showinfo("", "Not Found")
                id=id+1


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
                        elements.users(id)
                        break
                    elif row[0] != tofind and row[0] == reversed_list[0][0]:
                        messagebox.showinfo("", "Not Found")
                    id = id + 1
            except Exception:
                messagebox.showinfo("", "Id should be in numbers")

        srch = Tk()
        srch.geometry("200x120+1200+300")

        en = Entry(srch, width=18, font="Times 12 bold")
        en.place(x=10, y=10)

        byname = Button(srch, text="By Name", width=8, command=name)
        byname.place(x=10, y=50)
        byid = Button(srch, text="By Id", width=8, command=idno)
        byid.place(x=80, y=50)
        # show = Button(srch, text="Find", width=8, command=take)
        # show.place(x=30, y=80)
        srch.mainloop()

    def history():
        f = open("user_history.txt", "r")
        notepad.new(f.read())



    def users(id):
        global clist,user_listbox

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
                if str(user_get_in)==str(row[1]):
                    d_id=str(row[0])
                    d_name=row[1]
                    d_contact=row[2]
                    d_address=row[3]
            img = PhotoImage(file=d_address)
            img = img.zoom(7)
            img = img.subsample(10)
            panel = Label(det, image=img)
            panel.place(x=1, y=1)
            conn.close()

            label11 = Label(det, text="Customer ID:", font="Times 18 bold")
            label11.place(x=950, y=50)
            label22 = Label(det, text="Name:" , font="Times 18 bold")
            label22.place(x=950, y=100)
            label33 = Label(det, text="Contact Number:", font="Times 18 bold")
            label33.place(x=950, y=150)

            label1=Label(det,text=d_id,font="Times 20 bold")
            label1.place(x=1200,y=50)
            label2 = Label(det, text=d_name, font="Times 20 bold")
            label2.place(x=1200, y=100)
            label3 = Label(det, text=d_contact, font="Times 20 bold")
            label3.place(x=1200, y=150)

            det.mainloop()

        def user_login_info():
            try:
                t1 = time.strftime('%H:%M:%S', time.localtime())
                t2 = datetime.datetime.today().strftime('%d/%m/%Y')
                user_get_in = users_listbox.get(users_listbox.curselection())
                f = open("user_history.txt", "a")
                f.write(user_get_in + " (Time=" + str(t1) + ", Date=" + str(t2) + ")\n")
            except Exception:
                messagebox.showinfo("Error!", "Select Name from list first")

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

        add = Button(clist, text="Add", width=15, command=lambda: [user_login_info()])
        add.place(x=160, y=30)

        searchh = Button(clist, text="Search", width=15, command=lambda: [elements.search(), ])
        searchh.place(x=160, y=60)

        hist = Button(clist, text="Customer History", width=15, command=lambda: [elements.history()])
        hist.place(x=160, y=90)

        det = Button(clist, text="Detail", width=15, command=lambda: [detail()])
        det.place(x=160, y=120)

        clist.mainloop()


elements.users(0)
