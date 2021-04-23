from tkinter import *
from tkinter import messagebox
import re
import mysql.connector as my



def store():
    global cn, em
    fn = e1.get()
    ln = e2.get()
    add = e3.get("1.0", "end")
    add = add.rstrip()

    try:
        cn = int(e4.get())
    except ValueError:
        messagebox.showerror("Show", "Contact should be in numbers")
        cn = None

    ql = e5.get()
    x = re.findall('@', e6.get())
    if len(x) >= 1:
        em = e6.get()
    else:
        messagebox.showerror("Show", "Invalid email address")
    rv = v1.get()
    gg = 0
    wp = ''
    if rv == 1:
        gg = 'Male'
    elif rv == 2:
        gg = 'Female'
    elif rv == 3:
        gg = 'Other'
    if cv2.get() == 1:
        wp = ' Reading'
    if cv3.get() == 1:
        wp = wp + ' Singing'
    if cv4.get() == 1:
        wp = wp + ' Dancing'
    if cv5.get() == 1:
        wp = wp + ' Playing'

    li = []
    li = [fn, ln, add, cn, em, gg, wp, ql]
    t = tuple(li)
    print(t)
    print("FName= ", fn, "\nLName= ", ln, "\nAddress= ", add, "Contact= ", cn, "\nQualification= ", ql,
          "\nE-mail= ", em, "\nGender= ", gg, "\nHobbies= ", wp)
    if gg == 0:
        messagebox.showerror("Show", "Choose Gender")
    if len(wp) == 0:
        messagebox.showerror("Show", "Choose Hobbies")

    conn = my.connect(username='root', password='root', host='localhost', database='regform2')
    cur = conn.cursor()

    # q="create database regform2"
    # q = "create table detail(FName varchar(20),LName varchar(20),Address varchar(30),contact int,email varchar(20)" \
    #     ",gender varchar(20),hobbies varchar(30),qualification varchar(20))"
    q = "insert into detail (FName,Lname,Address,contact,email,gender,hobbies,qualification) " \
        "values(%s,%s,%s,%s,%s,%s,%s,%s)"

    cur.execute(q, t)
    conn.commit()
    conn.close()


f = Tk()
f.title('Registration Form')
f.geometry('500x250')

v1 = IntVar()
cv2 = IntVar()
cv3 = IntVar()
cv4 = IntVar()
cv5 = IntVar()

l1 = Label(f, text='Name: ')
l1.place(x=10, y=10)
e1 = Entry(f, width=15)
e1.place(x=60, y=10)

l2 = Label(f, text='Surname: ')
l2.place(x=180, y=10)
e2 = Entry(f, width=15)
e2.place(x=240, y=10)

l3 = Label(f, text='Address: ').place(x=10, y=30)
e3 = Text(f, height=2, width=30)
e3.place(x=60, y=30)

l4 = Label(f, text='Contact_No: ')
l4.place(x=10, y=70)
e4 = Entry(f, width=15)
e4.place(x=90, y=70)

l7 = Label(f, text='E-mail: ').place(x=200, y=70)
e6 = Entry(f, width=15)
e6.place(x=250, y=70)

l5 = Label(f, text='Gender: ')
l5.place(x=10, y=90)
r1 = Radiobutton(f, text='Male', value=1, variable=v1)
r1.place(x=70, y=90)
r2 = Radiobutton(f, text='Female', value=2, variable=v1)
r2.place(x=150, y=90)
r3 = Radiobutton(f, text='Other', value=3, variable=v1)
r3.place(x=230, y=90)

l6 = Label(f, text='Hobbies: ')
l6.place(x=10, y=110)
r1 = Checkbutton(f, text='Reading', variable=cv2, onvalue=1, offvalue=0)
r1.place(x=70, y=110)
r2 = Checkbutton(f, text='Singing', variable=cv3, onvalue=1, offvalue=0)
r2.place(x=150, y=110)
r3 = Checkbutton(f, text='Dancing', variable=cv4, onvalue=1, offvalue=0)
r3.place(x=230, y=110)
r3 = Checkbutton(f, text='Playing', variable=cv5, onvalue=1, offvalue=0)
r3.place(x=310, y=110)

l8 = Label(f, text='Qualification: ').place(x=10, y=130)
e5 = Entry(f, width=15)
e5.place(x=90, y=130)

b1 = Button(f, text='Submit', command=store).place(x=10, y=170)

f.mainloop()

# CALCULATOR+-factoraila sincostan
