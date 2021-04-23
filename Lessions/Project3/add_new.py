from tkinter import *
from tkinter import messagebox, filedialog
import mysql.connector as my


class reg:
    def delete():
        pass
    def new():
        def opens():
            global idproof
            l7 = Label(w1, text="                                 ", font='Times 12 bold', bg='white').place(x=80, y=310)
            idproof = filedialog.askopenfilename()
            x = idproof.rsplit("/", 1)[1]
            l7 = Label(w1, text=x, font='Times 12 bold', bg='white').place(x=80, y=310)

        def detail_fetch2():
            global ggg
            n_id = str(e3.get())
            name = e4.get()
            contact = e5.get()

            li = [n_id, name, contact, idproof]
            T = tuple(li)
            gg = 0

            conn = my.connect(username='root', password='root', host='localhost', database='user_data')
            cur = conn.cursor()
            q = "select * from user"
            cur.execute(q)
            records = cur.fetchall()

            for row in records:
                if name == row[1] or n_id == str(row[0]):
                    gg = 1
            # conn.commit()
            conn.close()

            if str(n_id) == '' or str(name) == '' or str(contact) == '' or str(idproof) == "":
                messagebox.showinfo("Incomplete detail", "Please Fill all the Information", )
            elif gg == 1:
                messagebox.showinfo("Name or ID Exists!", "Please provide new ID and Name or login with existing one", )
            else:
                pass
                conn = my.connect(username='root', password='root', host='localhost', database='user_data')
                cur = conn.cursor()

                # # q="create database user_data"
                # # q = "create table users(Username varchar(20), Email varchar(20), Password varchar(20))"
                q1 = "insert into user(Id,Name,Contact,ID_Proof) values(%s,%s,%s,%s)"
                # q2="select * from user"
                cur.execute(q1, T)

                messagebox.showinfo("Success", "Registration Successful")
                conn.commit()
                conn.close()

        conn = my.connect(username='root', password='root', host='localhost', database='user_data')
        cur = conn.cursor()
        q = "select * from user"
        cur.execute(q)
        records = cur.fetchall()
        for roww in records:
            ggg=roww[0]

        conn.close()

        w1 = Tk()
        w1.geometry('400x530')
        w1.title("Update New Customer")
        w1.config(bg='white')

        l3 = Label(w1, text='Id Number', font='Times 12 bold', bg='white').place(x=25, y=50 - 10)
        e3 = Entry(w1, width=25, font='Times 14 ', bg='cyan')
        e3.insert(END, str(ggg+1))
        e3.place(x=30, y=80 - 10)

        l4 = Label(w1, text='Name', font='Times 12 bold', bg='white').place(x=25, y=110 - 10 + 20)
        e4 = Entry(w1, width=25, font='Times 14 ', bg='cyan')
        e4.place(x=30, y=140 - 10 + 20)

        l5 = Label(w1, text='Contact', font='Times 12 bold', bg='white').place(x=25, y=170 - 10 + 40)
        e5 = Entry(w1, width=25, font='Times 14 ', bg='cyan')
        e5.place(x=30, y=200 - 10 + 40)

        l6 = Label(w1, text='ID Proof', font='Times 12 bold', bg='white').place(x=25, y=60 + 230 - 10)
        e6 = Button(w1, text="Select", command=opens)
        e6.place(x=30, y=260 - 10 + 60)

        b2 = Button(w1, text='Register', bg='deep sky blue', width=15, command=detail_fetch2)
        b2.place(x=30, y=450)

        w1.mainloop()


# reg.new()
