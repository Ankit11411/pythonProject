from tkinter import *
import mysql.connector as my
import tkinter as tk
from tkinter import ttk

class select:
    def users():
        def Addd():
            global user_get_in
            user_get_in=users.get(users.curselection())
            print(user_get_in)
            f=open("user_history.txt", "a")
            f.write(user_get_in +"\n")


        ulist=Tk()
        ulist.geometry("300x400")

        conn=my.connect(username="root",password="root",host="localhost",database='user_data')
        cur=conn.cursor()

        q="select * from user"

        cur.execute(q)
        records=cur.fetchall()

        users = Listbox(ulist, height="20")
        for row in records:
            users.insert(row[0], row[1])
        users.place(x=10, y=10)
        # gg = users.get()
        # print(gg)

        conn.close()

        add=Button(ulist,text="Add",width=15,command=Addd)
        add.place(x=160,y=30)
        ulist.mainloop()




# select.users()