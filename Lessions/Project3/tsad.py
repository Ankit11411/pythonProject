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




def clock(counter, l3, count):
    global string
    tt = datetime.datetime.fromtimestamp(counter)
    string = tt.strftime("%H:%M:%S")
    l3.config(text=string)
    l3.after(1000, lambda: [clock(counter, l3, count)])
    counter += 1

def customer_in(t1, user_get_in):
    clist.destroy()
    a = 120
    count = 1
    for live in dict.values():
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
            clock(counter, l3, count)
            dict[count] = user_get_in
            break
        print("ASD")
        count = count + 1
        a = a + 50


def users():
    global clist, user_listbox
    def user_login_info():
        t1 = time.strftime('%H:%M:%S', time.localtime())
        user_get_in = users_listbox.get(users_listbox.curselection())
        customer_in(t1, user_get_in)

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
    conn.close()

    add = Button(clist, text="Add", width=15, command=lambda: [user_login_info()])
    add.place(x=160, y=30)


    clist.mainloop()

def a():
    # global master,dict
    # dict = {1: 'empty', 2: 'empty', 3: 'empty', 4: 'empty', 5: 'empty', 6: 'empty', 7: 'empty', 8: 'empty'}
    #
    # master = Tk()
    # master.title("Cyber Cafe Management System")
    # master.geometry('900x700+500+10')
    # master.config(bg='white')
    #
    # add = Button(master, width=15, height=3, font='times 20 bold', text="Customer List",
    #              command=lambda: [users()])
    # add.place(x=600, y=550)
    #
    #
    # master.mainloop()

    global master,dict
    # curr_time = []
    dict = {1: 'empty', 2: 'empty', 3: 'empty', 4: 'empty', 5: 'empty', 6: 'empty', 7: 'empty', 8: 'empty'}
    # cust_occupied = for i in value(cust_queue)
    id = 0
    master = Tk()
    master.title("Cyber Cafe Management System")
    master.geometry('900x700+500+10')
    master.config(bg='white')
    # layout()

    # f = open("C:/Users/AnkiT/PycharmProjects/pythonProject/Project3/admin_history.txt", "r")
    # for last_line in f: pass

    # l = Label(master, text="A N K I T' S   C Y B E R   C A F E", font="Times 20 bold", bg='white').place(x=230, y=1)
    # l = Label(master, text="Welcome: ", bg='white').place(x=780, y=5)
    # l = Label(master, text=last_line, bg='white').place(x=850, y=4)
    # l = Label(master, text="Name", bg='white', font="times 12 bold").place(x=50, y=74)
    # l = Label(master, text="Entry_Time", bg='white', font="times 12 bold").place(x=200, y=74)
    # l = Label(master, text="Total_Time", bg='white', font="times 12 bold").place(x=300, y=74)

    cust_list = Button(master, width=15, height=3, font='times 20 bold', text="Customer List",
                       command=lambda: [users()])
    cust_list.place(x=600, y=550)
    # new_cust = Button(master, width=15, height=3, font='times 20 bold', text="New Customer",
    #                   command=lambda: [reg.new()])
    # new_cust.place(x=10, y=550)
    master.mainloop()


a()









