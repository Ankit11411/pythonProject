# from Pizzari import *
from tkinter import *
from tkinter import messagebox
import re
import mysql.connector as my
from tkinter import ttk
import threading
import time


class extfile:
    def fact():
        n = int(input("Enter a number: "))
        f = 1
        for i in range(1, n + 1):
            f = f * i
        print(f)

    def lock(l):
        l.acquire()
        extfile.fact()
        l.release()

    def detail_fetch(e3, e4, e5,  e6):
        uid = e3.get()
        mail = e4.get()
        pas = e5.get()

        li = [uid, mail, pas]
        T = tuple(li)
        gg = 0

        conn = my.connect(username='root', password='root', host='localhost', database='datafile')
        cur = conn.cursor()
        q = "select * from users"
        cur.execute(q)
        records = cur.fetchall()
        for row in records:
            if uid == row[0]:
                gg = 1
        # conn.commit()
        conn.close()

        correct_mail = re.findall("@", mail)
        if str(e3.get()) == '' or str(e4.get()) == '' or str(e5.get()) == '' or str(e6.get()) == '':
            messagebox.showinfo("Incomplete detail", "Please Fill all the Information")
        elif len(correct_mail) < 1:
            messagebox.showinfo("Invalid Email Address", "Please Enter Correct Email Address")
        elif e5.get() != e6.get():
            messagebox.showinfo("Mismatch!!", "Password doesnt match")
        elif gg == 1:
            messagebox.showinfo("Username Exists!", "Please provide new Username or login with existing one")
        else:
            conn = my.connect(username='root', password='root', host='localhost', database='datafile')
            cur = conn.cursor()

            # q="create database datafile"
            # q = "create table users(Username varchar(20), Email varchar(20), Password varchar(20))"
            q1 = "insert into users (Username,Email,Password,Address) values(%s,%s,%s,%s)"

            cur.execute(q1, T)
            messagebox.showinfo("Success", "Registration Successful", parent=w1)
            w1.destroy()
            conn.commit()
            conn.close()

    def login():
        uid_l = e1.get()
        pas_l = e2.get()
        if str(e1.get()) == '' or str(e2.get()) == '':
            messagebox.showinfo("Incomplete detail", "Please Enter Username and Password!")
        else:
            conn = my.connect(username='root', password='root', host='localhost', database='datafile')
            cur = conn.cursor()
            q = "select * from users"
            cur.execute(q)
            records = cur.fetchall()
            for row in records:
                if uid_l == row[0] and pas_l == row[2]:
                    f = open("login_history.txt", "a")
                    f.write(uid_l + "\n")
                    f.close()
            pizza_box()

            # conn.commit()
            conn.close()

    def register():

        w1 = Tk()
        w1.geometry('400x530')
        w1.config(bg='white')

        l3 = Label(w1, text='User Name', font='Times 12 bold', bg='white').place(x=25, y=50 - 10)
        e3 = Entry(w1, width=25, font='Times 14 ', bg='cyan')
        e3.place(x=30, y=80 - 10)

        l4 = Label(w1, text='Email Id', font='Times 12 bold', bg='white').place(x=25, y=110 - 10 + 20)
        e4 = Entry(w1, width=25, font='Times 14 ', bg='cyan')
        e4.place(x=30, y=140 - 10 + 20)

        l5 = Label(w1, text='Password', font='Times 12 bold', bg='white').place(x=25, y=170 - 10 + 40)
        e5 = Entry(w1, width=25, font='Times 14 ', bg='cyan', show="*")
        e5.place(x=30, y=200 - 10 + 40)

        l6 = Label(w1, text='Re-Enter Password', font='Times 12 bold', bg='white').place(x=25, y=60 + 230 - 10)
        e6 = Entry(w1, width=25, font='Times 14 ', bg='cyan', show="*")
        e6.place(x=30, y=260 - 10 + 60)

        l7 = Label(w1, text='Address', font='Times 12 bold', bg='white').place(x=25, y=360)
        e7 = Text(w1, width=25, height=2, font='Times 14 ', bg='cyan')
        e7.place(x=30, y=390)

        b2 = Button(w1, text='Register', bg='deep sky blue', width=15, command=detail_fetch)
        b2.place(x=30, y=450)

        w1.mainloop()

    def pizza_box():
        ap.destroy()
        global last_line

        def review():
            global pos
            for key in d2.keys():
                if key == cb2.get():
                    pos = list(d2).index(key)
            price = list(d2.values())[pos]
            l5 = Label(pz, text='Total:', bg='gold2', font='Times 14 bold').place(x=560, y=400)
            l6 = Label(pz, text=price, bg='gold2', font='Times 13 bold').place(x=610, y=402)

            try:
                qt = int(e8.get())
                l8.config(text='')
            except ValueError:
                l8.config(text='Please Enter in Numbers')

        pz = Tk()
        pz.geometry('700x700')
        pz.config(bg='gold2')

        f = open("login_history.txt", "r")
        for last_line in f:
            pass
        conn = my.connect(username='root', password='root', host='localhost', database='datafile')
        cur = conn.cursor()
        q = "select * from users"
        cur.execute(q)
        records = cur.fetchall()
        for row in records:
            if str(last_line) == str(row[0]):
                q1 = row[3]
                print(q1)
        # conn.commit()
        conn.close()

        d2 = {'Margherita': 300, 'Double Cheese Margherita': 350, 'Peppy Paneer': 450, 'PANEER MAKHANI': 450,
              'Paneer Special Pizza': 500}
        v = []
        for val in d2.keys():
            v.append(val)

        l1 = Label(pz, text="Welcome", bg='gold2').place(x=550, y=5)
        l2 = Label(pz, text=last_line, bg='gold2', font='Times 13 bold').place(x=610, y=5)
        l3 = Label(pz, text="Order Pizza Online", font='Times 18 bold', bg='gold2').place(x=5, y=5)
        b1 = Button(pz, text="Logout", bg='gold2', command=pz.destroy).place(x=610, y=30)
        l4 = Label(pz, text="Pizza Type: ", font='Times 16 bold', bg='gold2').place(x=50, y=100)
        # cb = ttk.Combobox(pz, width=15, font='Times 16 bold')
        # cb['value'] = d
        # cb.place(x=170, y=100)
        cb2 = ttk.Combobox(pz, width=15, font='Times 16 bold')
        cb2['value'] = v
        cb2.place(x=180, y=100)

        l5 = Label(pz, text="Extra Toppings: ", font='Times 16 bold', bg='gold2').place(x=50, y=150)
        r1 = Checkbutton(pz, text='Pepperoni', onvalue=1, offvalue=0, bg='gold2')
        r1.place(x=200, y=150)
        r2 = Checkbutton(pz, text='Mushrooms', onvalue=1, offvalue=0, bg='gold2')
        r2.place(x=300, y=150)
        r3 = Checkbutton(pz, text='Onions', onvalue=1, offvalue=0, bg='gold2')
        r3.place(x=200, y=180)
        r4 = Checkbutton(pz, text='Sausage', onvalue=1, offvalue=0, bg='gold2')
        r4.place(x=300, y=180)
        r5 = Checkbutton(pz, text='Extra cheese', onvalue=1, offvalue=0, bg='gold2')
        r5.place(x=200, y=210)
        r6 = Checkbutton(pz, text='Green peppers', onvalue=1, offvalue=0, bg='gold2')
        r6.place(x=300, y=210)

        l6 = Label(pz, text="Pizza Size: ", font='Times 16 bold', bg='gold2').place(x=50, y=240)
        r7 = Radiobutton(pz, text='Small', bg='gold2')
        r7.place(x=200, y=240)
        r8 = Radiobutton(pz, text='Medium', bg='gold2')
        r8.place(x=300, y=240)
        r9 = Radiobutton(pz, text='Large', bg='gold2')
        r9.place(x=400, y=240)

        l7 = Label(pz, text="Quantity: ", font='Times 16 bold', bg='gold2').place(x=50, y=290)
        l8 = Label(pz, text='', font='Times 16 bold', bg='gold2')
        l8.place(x=220, y=290)
        e8 = Entry(pz, font='Times 16 bold', width=5)
        e8.place(x=150, y=290)

        b2 = Button(pz, text='Review', command=review).place(x=10, y=450)

        # gg=str(cb[0])
        # l6=Label(pz,text=gg).place(x=200,y=500)
        pz.mainloop()
