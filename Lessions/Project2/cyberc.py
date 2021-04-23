import mysql.connector as my
# from Project2.cyber_managem import *


def login():
    uid_l = e1.get()
    pas_l = e2.get()
    if str(e1.get()) == '' or str(e2.get()) == '':
        messagebox.showinfo("Incomplete detail", "Please Enter Username and Password!")
    else:
        conn = my.connect(username='root', password='root', host='localhost', database='admin_data')
        cur = conn.cursor()
        q = "select * from admins"
        cur.execute(q)
        records = cur.fetchall()
        for row in records:
            if uid_l == row[0] and pas_l == row[2]:
                f = open("admin_history.txt", "a")
                f.write(uid_l + "\n")
                f.close()
                ap.destroy()
                adm.admin_page()
                break
        else:
            messagebox.showinfo("Cannot Login", "Incorrect Username or Password")

        conn.close()


def register():
    def detail_fetch():
        uid = e3.get()
        mail = e4.get()
        pas = e5.get()
        add = e7.get()
        add = add.rstrip()
        li = [uid, mail, pas, add]
        T = tuple(li)
        gg = 0

        conn = my.connect(username='root', password='root', host='localhost', database='admin_data')
        cur = conn.cursor()
        q = "select * from admins"
        cur.execute(q)
        records = cur.fetchall()
        for row in records:
            if uid == row[0]:
                gg = 1
        # conn.commit()
        conn.close()

        correct_mail = re.findall("@", mail)
        if str(e3.get()) == '' or str(e4.get()) == '' or str(e5.get()) == '' or str(e6.get()) == '' or str(add) == '':
            messagebox.showinfo("Incomplete detail", "Please Fill all the Information", parent=w1)
        elif len(correct_mail) < 1:
            messagebox.showinfo("Invalid Email Address", "Please Enter Correct Email Address", parent=w1)
        elif e5.get() != e6.get():
            messagebox.showinfo("Mismatch!!", "Password doesnt match", parent=w1)
        elif gg == 1:
            messagebox.showinfo("Username Exists!", "Please provide new Username or login with existing one", parent=w1)
        else:
            conn = my.connect(username='root', password='root', host='localhost', database='admin_data')
            cur = conn.cursor()

            # q="create database datafile"
            # q = "create table users(Username varchar(20), Email varchar(20), Password varchar(20))"
            q1 = "insert into admins(Username,Email,Password,Contact) values(%s,%s,%s,%s)"

            cur.execute(q1, T)
            messagebox.showinfo("Success", "Registration Successful", parent=w1)
            w1.destroy()
            conn.commit()
            conn.close()

    w1 = Tk()
    w1.geometry('400x530')
    w1.title("Registration Form")
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

    l7 = Label(w1, text='Contact', font='Times 12 bold', bg='white').place(x=25, y=360)
    e7 = Entry(w1, width=25, font='Times 14 ', bg='cyan')
    e7.place(x=30, y=390)

    b2 = Button(w1, text='Register', bg='deep sky blue', width=15, command=detail_fetch)
    b2.place(x=30, y=450)

    w1.mainloop()


ap = Tk()
ap.geometry('400x350')
ap.title("Authentication Required")
ap.config(bg='white')

l = Label(ap, text="A d m i n   L o g i n", font='Times 12 bold', bg='white').place(x=5, y=2)
l = Label(ap, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                   "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font='Times 4 bold', bg='white').place(x=1, y=25)

l1 = Label(ap, text='Username ', font='Times 14 bold', bg='white').place(x=35, y=35+5)
e1 = Entry(ap, width=22, font='Times 20 ', bg='lightyellow')
e1.place(x=40, y=70+5)

l2 = Label(ap, text='Password ', font='Times 14 bold', bg='white').place(x=35, y=130+5)
e2 = Entry(ap, width=22, font='Times 20 bold', bg='lightyellow', show="*")
e2.place(x=40, y=165+5)

b1 = Button(ap, text="Login", font='Times 14 bold', bg='yellow', width=28, command=login)
b1.place(x=40, y=240+5)

b1 = Button(ap, text="Register?", font='Times 14 bold', bg='yellow', width=28, command=register)
b1.place(x=40, y=290+5)

ap.mainloop()
