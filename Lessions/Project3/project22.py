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

def clock(counter, curr_time, count, i):
    global string
    tt = datetime.datetime.fromtimestamp(counter)
    string = tt.strftime("%H:%M:%S")
    # print(curr_time)
    curr_time[0].config(text=string)
    curr_time[0].after(1000, lambda: [clock(counter, curr_time, count,i)])
    counter += 1

def remo():
    bt.destroy()
    l.destroy()
    cust_queue = 'empty'
    # print(cust_queue)
    curr_time.destroy()


def cust_in(user_get_in):
    global i,a,count
    print(a)
    for i in range(no_of_pc):
        for j in range(no_of_pc):
            if cust_queue[j] == user_get_in:
                print(cust_queue)
                messagebox.showinfo("Exist!", "Customer already allotted seat!")
                return

        if cust_queue[i] == 'empty':
            clist.destroy()
            l = Label(master, text=user_get_in)
            l.place(x=50, y=a)
            print(curr_time)
            print(i)
            curr_time.append(Label(master))
            curr_time[i].place(x=150, y=a)
            print(curr_time)
            bt.append(Button(master, text='REMOVE', command=lambda: [remo()]))
            bt[i].place(x=800, y=a)
            counter = 66600
            clock(counter, curr_time, count, i)
            cust_queue[count] = user_get_in
            count = count + 1
            a = a + 50
            break



def customer_list(id):
    global clist

    def search():
        def name():
            global tofind, id
            tofind = str(task.get())
            conn = my.connect(username="root", password="root", host="localhost", database='user_data')
            cur = conn.cursor()
            cur.execute("select * from user")
            records = cur.fetchall()
            reversed_list = records[::-1]
            id = 0
            for row in records:
                if row[1] == tofind:
                    temp = str(row[1] + "'s ID IS " + str(row[0]))
                    messagebox.showinfo("Found", temp)
                    clist.destroy()
                    customer_list(id)
                    break
                elif row[0] != tofind and row[0] == reversed_list[0][0]:
                    messagebox.showinfo("", "Not Found")
                id = id + 1

        def idno():
            try:
                global tofind, id
                tofind = int(task.get())
                conn = my.connect(username="root", password="root", host="localhost", database='user_data')
                cur = conn.cursor()
                cur.execute("select * from user")
                records = cur.fetchall()
                id = 0
                reversed_list = records[::-1]
                for row in records:
                    if row[0] == tofind:
                        temp = str(str(row[0]) + "'s NAME IS " + str(row[1]))
                        messagebox.showinfo("Found", temp)
                        clist.destroy()
                        customer_list()
                        break
                    elif row[0] != tofind and row[0] == reversed_list[0][0]:
                        messagebox.showinfo("", "Not Found")
                    id = id + 1
            except Exception:
                messagebox.showinfo("", "Id should be in numbers")

        srch = Tk()
        srch.geometry("180x100+1200+300")
        srch.title("Search")

        task = Entry(srch, width=18, font="Times 12 bold")
        task.place(x=10, y=10)

        byname = Button(srch, text="By Name", width=8, command=name)
        byname.place(x=10, y=50)
        byid = Button(srch, text="By Id", width=8, command=idno)
        byid.place(x=80, y=50)
        srch.mainloop()

    def history():
        f = open("user_history.txt", "r")
        notepad.new(f.read())

    def detail():
        user_get_in = users_listbox.get(users_listbox.curselection())
        conn = my.connect(username="root", password="root", host="localhost", database='user_data')
        cur = conn.cursor()
        cur.execute("select * from user")
        records = cur.fetchall()
        for row in records:
            if str(user_get_in) == str(row[1]):
                d_id = str(row[0])
                d_name = row[1]
                d_contact = row[2]
                d_address = row[3]
        img = PhotoImage(file=d_address)
        w = str(img.width())
        h = str(img.height())
        conn.close()

        det = tkinter.Toplevel()
        det.geometry(str(int(w) + 400) + "x" + str(int(h) + 10) + "+0+0")
        det.config(bg='green')

        panel = Label(det, image=img)
        panel.place(x=0, y=0)

        l = Label(det, text="Customer ID:", font="Times 18 bold", bg='green')
        l.place(x=int(w) + 20, y=50)
        l = Label(det, text="Name:", font="Times 18 bold", bg='green')
        l.place(x=int(w) + 20, y=100)
        l = Label(det, text="Contact Number:", font="Times 18 bold", bg='green')
        l.place(x=int(w) + 20, y=150)

        l = Label(det, text=d_id, font="Times 20 bold", bg='green', fg='white')
        l.place(x=int(w) + 200, y=50)
        l = Label(det, text=d_name, font="Times 20 bold", bg='green', fg='white')
        l.place(x=int(w) + 200, y=100)
        l = Label(det, text=d_contact, font="Times 20 bold", bg='green', fg='white')
        l.place(x=int(w) + 200, y=150)

        det.mainloop()

    def user_login_info():
        # try:
        global t1
        t1 = time.strftime('%H:%M:%S', time.localtime())
        t2 = datetime.datetime.today().strftime('%d/%m/%Y')
        user_get_in = users_listbox.get(users_listbox.curselection())
        f = open("user_history.txt", "a")
        f.write(user_get_in + " (Time=" + str(t1) + ", Date=" + str(t2) + ")\n")
        cust_in(user_get_in)

        # except Exception:
        #     messagebox.showinfo("Error!", "Select Name from list first")

    clist = Tk()
    clist.geometry("300x350+900+300")
    clist.title("Customer List")

    conn = my.connect(username="root", password="root", host="localhost", database='user_data')
    cur = conn.cursor()
    cur.execute("select * from user")
    records = cur.fetchall()
    users_listbox = Listbox(clist, height="20")
    for row in records:
        users_listbox.insert(row[0], row[1])
    users_listbox.place(x=10, y=10)
    users_listbox.select_set(id)
    conn.close()

    add = Button(clist, text="Add", width=15, command=lambda: [user_login_info()])
    add.place(x=160, y=30)
    searchh = Button(clist, text="Search", width=15, command=lambda: [search()])
    searchh.place(x=160, y=60)
    hist = Button(clist, text="Customer History", width=15, command=lambda: [history()])
    hist.place(x=160, y=90)
    det = Button(clist, text="Detail", width=15, command=lambda: [detail()])
    det.place(x=160, y=120)

    clist.mainloop()


def layout():
    global no_of_pc, a
    a = 120
    A.line(1, 495)
    no_of_pc = 8
    for i in range(0, no_of_pc):
        pc_n = "PC" + str(i + 1)
        l = Label(master, text=pc_n, bg='white')
        l.place(x=5, y=a)
        A.line(1, a - 25)
        a = a + 50
    a = 120


def windows():
    global master, id, cust_queue, counter, curr_time,bt,a,count
    # curr_time = []
    a = 120
    count = 1
    curr_time = []
    bt=[]
    cust_queue = {0: 'empty', 1: 'empty', 2: 'empty', 3: 'empty', 4: 'empty', 5: 'empty', 6: 'empty', 7: 'empty'}
    id = 0
    master = Tk()
    master.title("Cyber Cafe Management System")
    master.geometry('900x700+500+10')
    master.config(bg='white')
    layout()
    f = open("/Lessions/Project3/admin_history.txt", "r")
    for last_line in f: pass

    l = Label(master, text="A N K I T' S   C Y B E R   C A F E", font="Times 20 bold", bg='white').place(x=230, y=1)
    l = Label(master, text="Welcome: ", bg='white').place(x=780, y=5)
    l = Label(master, text=last_line, bg='white').place(x=850, y=4)
    l = Label(master, text="Name", bg='white', font="times 12 bold").place(x=50, y=74)
    l = Label(master, text="Entry_Time", bg='white', font="times 12 bold").place(x=200, y=74)
    l = Label(master, text="Total_Time", bg='white', font="times 12 bold").place(x=300, y=74)

    cust_list = Button(master, width=15, height=3, font='times 20 bold', text="Customer List",
                       command=lambda: [customer_list(0)])
    cust_list.place(x=600, y=550)
    new_cust = Button(master, width=15, height=3, font='times 20 bold', text="New Customer",
                      command=lambda: [reg.new()])
    new_cust.place(x=10, y=550)
    master.mainloop()


windows()
