from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as my


def login():
    global w1
    w1 = Tk()
    w1.title("Cafe Management System")
    w1.geometry("800x600")
    w1.resizable(False, False)
    w.destroy()
    w1.config(background="#6f4e37")

    def place_order():
        frame_place = Frame(w1, bg="#696969")
        frame_place.place(x=200, y=0, height=600, width=600)

        lf = Label(frame_place, text="Place Order")
        lf.place(x=20, y=40)

        lf1 = Label(frame_place, text="Category")
        lf1.place(x=20, y=80)

        list1 = ["Andhra Pradesh", "Assam", "Arunachal Pradesh", "Bihar", "Goa",
                 "Gujarat", "Jammu and Kashmir"]
        cb1 = ttk.Combobox(frame_place, width=20)
        cb1['value'] = list1
        cb1.place(x=20, y=110)
        cb1.set("Select Item")

        search = Entry(frame_place, width=20)
        search.place(x=30, y=140)

        t = Text(frame_place, height=25, width=20)
        t.place(x=20, y=170)

        frame3 = Frame(frame_place, bg="#696969", highlightbackground="black", highlightthickness=3)
        frame3.place(x=200, y=80, height=200, width=350)

        Item_name = Label(frame3, text="Item Name")
        Item_name.place(x=20, y=20)

        Item_entry = Entry(frame3, width=20)
        Item_entry.place(x=20, y=45)

        price = Label(frame3, text="Price")
        price.place(x=180, y=20)

        price_entry = Entry(frame3, width=20)
        price_entry.place(x=180, y=45)

        quantity = Label(frame3, text="Quantity")
        quantity.place(x=20, y=80)

        e_quntity = Spinbox(frame3, width=15, from_=0, to_=32)
        e_quntity.place(x=20, y=110)

        total = Label(frame3, text="Total")
        total.place(x=180, y=80)

        total_entry = Entry(frame3, width=20)
        total_entry.place(x=180, y=110)

        b_cart = Button(frame3, text="Add to Cart")
        b_cart.place(x=210, y=160)

        remove = Button(frame_place, text="Remove")
        remove.place(x=230, y=500)

        gt = Label(frame_place, text="Grand Total")
        gt.place(x=350, y=500)

        t = Text(frame_place, height=1, width=10)
        t.place(x=340, y=525)

        print_ = Button(frame_place, text="Print")
        print_.place(x=480, y=500)

    def additem():

        def add():

            catogory = cb1.get()
            ItemName = Item_entry.get()
            ItemPrice = price_entry.get()

            t = [catogory, ItemName, ItemPrice]
            print(t)

            if catogory == "" or ItemName == "" or ItemPrice == "":
                messagebox.showerror("Show", "Please fill all Details")

            else:
                conn = my.connect(user="root", password='root', host='localhost', database='cafe')
                cur = conn.cursor()
                q = "insert into cdata (category,Item_Name,Item_Price)values(%s,%s,%s)"
                cur.execute(q, t)
                conn.commit()
                conn.close()
                messagebox.showinfo("Show", "The Item insert successfully")

        frame_place = Frame(w1, bg="#696969")
        frame_place.place(x=200, y=0, height=600, width=600)

        title = Label(frame_place, text="New Item")
        title.place(x=260, y=20)

        lf1 = Label(frame_place, text="Category")
        lf1.place(x=180, y=80)

        list1 = ["Andhra Pradesh", "Assam", "Arunachal Pradesh", "Bihar", "Goa",
                 "Gujarat", "Jammu and Kashmir"]
        cb1 = ttk.Combobox(frame_place, width=20)
        cb1['value'] = list1
        cb1.place(x=180, y=110)
        cb1.set("Select Item")

        Item_name = Label(frame_place, text="Item Name")
        Item_name.place(x=180, y=170)

        Item_entry = Entry(frame_place, width=20)
        Item_entry.place(x=180, y=200)

        price = Label(frame_place, text="Price")
        price.place(x=180, y=260)

        price_entry = Entry(frame_place, width=20)
        price_entry.place(x=180, y=290)

        b_add = Button(frame_place, text="Add Items", command=add)
        b_add.place(x=250, y=400)

    def updateitems():

        def update():

            # t=[catogory,ItemName,ItemPrice]
            # print(t)

            conn = my.connect(user="root", password='root', host='localhost', database='cafe')
            cur = conn.cursor()
            # q = "insert into cdata (category,Item_Name,Item_Price)values(%s,%s,%s)"
            q1 = "select * from cdata"
            # cur.execute(q)
            cur.execute(q1)
            # messagebox.showinfo("Show", "The Item insert successfully")
            i = 0
            for row in cur:
                my_tree.insert('', i, text="", values=(row[0], row[1], row[2]))
                i = i + 1
            conn.commit()
            conn.close()



        def getrow(event):


            item = my_tree.item(my_tree.focus())

            g1=item['values'][0]
            g2 = item['values'][1]
            # Item_entry.insert(END, str(g2))
            g3 = item['values'][2]

            cat.set(item['values'][0])
            IName.set(item['values'][1])
            IPrice.set(item['values'][2])



        frame_place = Frame(w1, bg="#696969")
        frame_place.place(x=200, y=0, height=600, width=600)

        title = Label(frame_place, text="Update Items")
        title.place(x=260, y=20)

        Item_name = Label(frame_place, text="Item Name")
        Item_name.place(x=380, y=100)

        Item_entry = Entry(frame_place, width=20)
        Item_entry.place(x=380, y=130)

        cols = ("category", "Item Name", "Price")
        my_tree = ttk.Treeview(frame_place, height=8, show='headings', columns=cols)

        my_tree.heading("category", text="Category", anchor=CENTER)
        my_tree.heading("Item Name", text="Item Name", anchor=CENTER)
        my_tree.heading("Price", text="Price", anchor=CENTER)

        my_tree.column("category", width=110, minwidth=25, anchor=CENTER)
        my_tree.column("Item Name", width=110, minwidth=25, anchor=CENTER)
        my_tree.column("Price", width=110, minwidth=25, anchor=CENTER)

        conn = my.connect(user="root", password='root', host='localhost', database='cafe')
        cur = conn.cursor()
        q1 = "select * from cdata"
        cur.execute(q1)

        i = 0
        for row in cur:
            my_tree.insert('', i, text="", values=(row[0], row[1], row[2]))
            i = i + 1

        my_tree.bind('<Double 1>', getrow)
        my_tree.place(x=100, y=200)

        lf1 = Label(frame_place, text="Category")
        lf1.place(x=100, y=420)

        list1 = ["Warm Coffee", "Cold Coffee", "Tea", "Childed Drinks", "Hot Drinks",
                 "Sandwich", "Non-veg Snack", "Veg Snack", "Mo Mo", "Burgers", "Hot Soup"]
        cb1 = ttk.Combobox(frame_place, width=20, textvariable=cat)
        cb1['value'] = list1
        cb1.place(x=100, y=450)
        cb1.set("Select Item")
        cb1.bind("<<ComboboxSelected>>")

        Item_name = Label(frame_place, text="Item Name")
        Item_name.place(x=100, y=500)

        Item_entry = Entry(frame_place, width=20, textvariable=IName)
        Item_entry.place(x=100, y=530)


        price = Label(frame_place, text="Price")
        price.place(x=400, y=420)

        price_entry = Entry(frame_place, width=20, textvariable=IPrice)
        price_entry.place(x=400, y=450)

        b_up = Button(frame_place, text="Update Items", command=update)
        b_up.place(x=400, y=500)

    def removeitem():
        frame_place = Frame(w1, bg="#696969")
        frame_place.place(x=200, y=0, height=600, width=600)

        title = Label(frame_place, text="Update Items")
        title.place(x=260, y=20)

        Item_name = Label(frame_place, text="Item Name")
        Item_name.place(x=270, y=100)

        Item_entry = Entry(frame_place, width=20)
        Item_entry.place(x=270, y=130)

        cols = ("Item Name", "category", "Price")
        my_tree = ttk.Treeview(frame_place, height=8, show='headings', columns=cols)

        my_tree.heading("Item Name", text="Item Name", anchor=CENTER)
        my_tree.heading("category", text="Category", anchor=CENTER)
        my_tree.heading("Price", text="Price", anchor=CENTER)

        my_tree.column("Item Name", width=110, minwidth=25, anchor=CENTER)
        my_tree.column("category", width=110, minwidth=25, anchor=CENTER)
        my_tree.column("Price", width=110, minwidth=25, anchor=CENTER)

        conn = my.connect(user="root", password='root', host='localhost', database='cafe')
        cur = conn.cursor()
        q1 = "select * from cdata"
        cur.execute(q1)

        i = 0
        for row in cur:
            my_tree.insert('', i, text="", values=(row[0], row[1], row[2]))
            i = i + 1

        my_tree.place(x=100, y=200)

    b_placeorder = Button(w1, text="Place Order", width=15, command=place_order)
    b_placeorder.place(x=80, y=50)

    b_additems = Button(w1, text="Add Items", width=15, command=additem)
    b_additems.place(x=80, y=100)

    b_updateitems = Button(w1, text="Update Items", width=15, command=updateitems)
    b_updateitems.place(x=80, y=150)

    b_removeitem = Button(w1, text="Remove Items", width=15, command=removeitem)
    b_removeitem.place(x=80, y=200)

    b2 = Button(w1, text="Logout", width=15)
    b2.place(x=80, y=500)


def geast():
    # frame1
    frame1 = Frame(w, bg="#6f4e37")
    frame1.place(x=0, y=0, height=600, width=800)

    def order():

        category = StringVar()
        ItemName = StringVar()
        ItemPrice = IntVar()
        quntity = IntVar()
        tot = IntVar()

        frame2 = Frame(w, bg="#696969")
        frame2.place(x=200, y=0, height=600, width=600)

        lf = Label(frame2, text="Place Order")
        lf.place(x=20, y=40)

        lf1 = Label(frame2, text="Category")
        lf1.place(x=20, y=80)

        def pick(e):
            if cb1.get() == "Warm Coffee":
                lbox.delete(0, END)
                for item in warm_coffee:
                    lbox.insert(END, item)

            if cb1.get() == "Cold Coffee":
                lbox.delete(0, END)
                for item in cold_coffee:
                    lbox.insert(END, item)

            if cb1.get() == "Tea":
                lbox.delete(0, END)
                for item in tea:
                    lbox.insert(END, item)

            if cb1.get() == "Childed Drinks":
                lbox.delete(0, END)
                for item in child_drinks:
                    lbox.insert(END, item)

            if cb1.get() == "Hot Drinks":
                lbox.delete(0, END)
                for item in hot_drink:
                    lbox.insert(END, item)

            if cb1.get() == "Sandwich":
                lbox.delete(0, END)
                for item in sandwich:
                    lbox.insert(END, item)

            if cb1.get() == "Non-veg Snack":
                lbox.delete(0, END)
                for item in n_snack:
                    lbox.insert(END, item)

            if cb1.get() == "Veg Snack":
                lbox.delete(0, END)
                for item in v_snack:
                    lbox.insert(END, item)

            if cb1.get() == "Mo Mo":
                lbox.delete(0, END)
                for item in momo:
                    lbox.insert(END, item)

            if cb1.get() == "Burgers":
                lbox.delete(0, END)
                for item in burger:
                    lbox.insert(END, item)

            if cb1.get() == "Hot Soup":
                lbox.delete(0, END)
                for item in hot_soup:
                    lbox.insert(END, item)

        list1 = ["Warm Coffee", "Cold Coffee", "Tea", "Childed Drinks", "Hot Drinks",
                 "Sandwich", "Non-veg Snack", "Veg Snack", "Mo Mo", "Burgers", "Hot Soup"]
        warm_coffee = ["Espresso", "Espresso Dopio", "Americano", "Cappuccino", "Honey Latte", "Caramel Latte"]
        cold_coffee = ["Iced Americano", "Iced Cappuccino", "Iced Latte", "Iced Mocha", "Oreo Latte"]
        tea = ["Milk Tea", "Black Tea", "Green Tea", "Masala Tea", "Honey Lemon Tea"]
        child_drinks = ["Lemon Ice Tea", "Peach Ice Tea", "Mint Cooler", "Cold Drink", "Masala Cola",
                        "Fresh Lemone Soda"]
        hot_drink = ["Honet HOt lemon", "Ginger Honey Lemon", "Hot Chocolate"]
        sandwich = ["Veggie Sandwich", "Ham & Cheese Sandwich", "Tuna Mayo Sandwich", "Classic BLT Sandwich"]
        n_snack = ["Fish Finger", "Boneless Chicken Chilly", "Spicy Chicken Wings", "Chicken Nuggets",
                   "Chicken Momo Sadeko", "Pork Chilly", "Pork Tawa"]
        v_snack = ["Heese Balls", "Mushroom Chilly", "Spicy Peanuts", "Aaloo Jeera", "Chips Chilly", "French Fries",
                   "Veg Momo"]
        momo = ["Steam", "Jhol", "Kothey", "Fried", "Chilly"]
        burger = ["Veggie Burger", "Classic Chicken Burger", "Crispy Chicken Burger", "Grilled Chicken Burger",
                  "Hungry Man's Burger"]
        hot_soup = ["Veg & Mushroom Soup", "Hot & Sour Soup", "Chicken Lemon Soup"]

        cb1 = ttk.Combobox(frame2, width=20, textvariable=category)
        cb1['value'] = list1
        cb1.place(x=20, y=110)
        cb1.set("Select Item")
        cb1.bind("<<ComboboxSelected>>", pick)

        search = Entry(frame2, width=20)
        search.place(x=30, y=140)

        lbox = Listbox(frame2, height=25, width=25)
        lbox.place(x=20, y=170)

        frame3 = Frame(frame2, bg="#696969", highlightbackground="black", highlightthickness=3)
        frame3.place(x=200, y=80, height=200, width=350)

        Item_name = Label(frame3, text="Item Name")
        Item_name.place(x=20, y=20)

        Item_entry = Entry(frame3, width=20, textvariable=ItemName)
        Item_entry.place(x=20, y=45)

        price = Label(frame3, text="Price")
        price.place(x=180, y=20)

        price_entry = Entry(frame3, width=20, textvariable=ItemPrice)
        price_entry.place(x=180, y=45)

        quantity = Label(frame3, text="Quantity")
        quantity.place(x=20, y=80)

        e_quntity = Spinbox(frame3, width=15, from_=0, to_=32, textvariable=quntity)
        e_quntity.place(x=20, y=110)

        total = Label(frame3, text="Total")
        total.place(x=180, y=80)

        total_entry = Entry(frame3, width=20, textvariable=tot)
        total_entry.place(x=180, y=110)

        b_cart = Button(frame3, text="Add to Cart")
        b_cart.place(x=210, y=160)

        cols = ["Item Name", "Unit Price", "Qantity", "Price"]
        my_tree = ttk.Treeview(frame2, height=7, show='headings', columns=cols)

        my_tree.column("Item Name", width=100, minwidth=25, anchor=CENTER)
        my_tree.column("Unit Price", width=100, minwidth=25, anchor=CENTER)
        my_tree.column("Qantity", width=100, minwidth=25, anchor=CENTER)
        my_tree.column("Price", width=100, minwidth=25, anchor=CENTER)

        my_tree.heading("Item Name", text="Item Name", anchor=CENTER)
        my_tree.heading("Unit Price", text="Unit Price", anchor=CENTER)
        my_tree.heading("Qantity", text="Qantity", anchor=CENTER)
        my_tree.heading("Price", text="Price", anchor=CENTER)

        my_tree.place(x=190, y=310)

        remove = Button(frame2, text="Remove")
        remove.place(x=230, y=500)

        gt = Label(frame2, text="Grand Total")
        gt.place(x=350, y=500)

        t = Text(frame2, height=1, width=10)
        t.place(x=340, y=525)

        print_ = Button(frame2, text="Print")
        print_.place(x=480, y=500)

    def logout():
        log = messagebox.askyesno("Logout", "Conform You want Logout")
        if log > 0:
            w.destroy()
            return

    b1 = Button(frame1, text="Place Order", command=order)
    b1.place(x=80, y=50)

    b2 = Button(frame1, text="Logout", command=logout)
    b2.place(x=80, y=500)


w = Tk()
w.title("Cafe Management System")
w.geometry("800x600")
# w.resizable(False,False)

cat = StringVar()
IName = StringVar()
IPrice = StringVar()
quntity = IntVar()
tot = IntVar()

# Backgraund Image
bg = ImageTk.PhotoImage(file="Capture.PNG")
bg_image = Label(w, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

# frame1
frame_login = Frame(w, bg="#6f4e37")
frame_login.place(x=450, y=50, height=340, width=300)

l1 = Label(frame_login, text="Username", bg="white")
l1.place(x=50, y=80)
e1 = Entry(frame_login, width=20)
e1.place(x=50, y=110)
l2 = Label(frame_login, text="Password")
l2.place(x=50, y=170)
e2 = Entry(frame_login, width=20)
e2.place(x=50, y=200)
b = Button(frame_login, text="Login", command=login)
b.place(x=120, y=250)
l3 = Button(frame_login, text="Conteneous as Geast", command=geast)
l3.place(x=83, y=280)

w.mainloop()
