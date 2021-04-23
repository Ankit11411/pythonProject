from tkinter import messagebox
import tkinter.ttk
import mysql.connector as my
from datetime import datetime

import time
import datetime
# from menubar import *
import random
import threading
from line import *
import tkinter as tk


# from add_new import *
'''
def clock(counter, l, i):
    global string
    tt = datetime.datetime.fromtimestamp(counter)
    string = tt.strftime("%H:%M:%S")
    l[i].config(text=string)
    p.config(text=i)
    print(l['text'])
    l[i].after(1000, lambda: [clock(counter, l, i)])
    counter += 1


w = Tk()
w.geometry("400x400")
a = 20
b = 20
bt=[]


for i in range(1, 15 + 1):
    if i == 6 or i == 11:
        b = b + 50
        a = 20
    bt.append(Button(w, text=i))
    bt[i-1].place(x=a, y=b)
    a = a + 50
for i in range(0, 15):
    bt[i].config(command=lamda:[question])

w.mainloop()
'''
# bt=[]
# for i in range(2):
#     for j in range(5):
#         gg=str((i*5)+j+1)
#         bt.append(Button(w,text=gg))
#         bt[int(gg)-1].place(x=a,y=b)
#         a=a+50
#     a=20
#     b=b+50
# bt[1].config(bg='yellow')
counter = 66600

def clock():
    global counter
    tt = datetime.datetime.fromtimestamp(counter)
    string = tt.strftime("%H:%M:%S")
    print(string)
    l3.config(text=string)
    l3.after(1000, lambda: [clock()])
    counter += 1
clock()
