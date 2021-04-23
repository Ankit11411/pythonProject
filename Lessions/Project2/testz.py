from tkinter.filedialog import *
from tkinter import *
from PIL import Image, ImageDraw, ImageTk
import tkinter
import random
import threading
from datetime import datetime


# def img():
#     fil = askopenfile(mode="r+", filetype=[('Image', '.png')])
#     data = fil.read()
#     nt.insert(END, data)
#     fil.close()


def opens():
    filename = filedialog.askopenfilename()
    print(filename)

#
# gg = Tk()
# gg.geometry("400x400")
# # l1=Listbox(gg,text="ASD",width=25)
# # l1.place(x=2,y=150)
# # l2=Listbox(gg,width=25,)
# # l2.place(x=2,y=200)
#
#
#
# # def A():
# #     l1 = Label(gg, text="AAAAAAA", font="Times 20 bold")
# #     l1.place(x=100, y=100)
# #     wp = ['blue', 'green', 'red']
# #     l1.config(fg=wp[random.randrange(0,2)])
# #     threading.Timer(1, A).start()
# # A()
# b = Button(gg, text="select")
# b.place(x=10, y=10)
# gg.mainloop()
'''
import tkinter as Tkinter
from datetime import datetime
counter = 66600

def Stop():
    global a
    a=1


def Start():
    global counter
    tt = datetime.fromtimestamp(counter)
    string = tt.strftime("%H:%M:%S")
    if a==1:
        print(string)
        return string
    # display = string
    label.config(text=string)
    label.after(1000, lambda :[Start()])
    counter += 1

root = Tkinter.Tk()
root.title("Stopwatch")

# Fixing the window size.
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text="Welcome!")
label.pack()
a=0
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', command=lambda: Start())
stop = Tkinter.Button(f, text='Stop', command=lambda: Stop())
f.pack(anchor='center', pady=5)
start.pack(side="left")
stop.pack(side="left")

root.mainloop()'''




from tkinter import *
from datetime import datetime
from tkinter import messagebox


def submit():
    submit_b = Button(root, text='Submit', font='times 25 bold', bg='grey70')
    submit_b.place(x=1200, y=400)

def question():
    # 1) What is the maximum possible length of an identifier?
    # 2) Who developed the Python language?
    # 3) In which year was the Python language developed?
    # 4) In which language is Python written?
    # 5) Which one of the following is the correct extension of the Python file?
    # 6) In which year was the Python 3.0 version developed?
    # 7) What do we use to define a block of code in Python language?
    # 8) Which character is used in Python to make a single line comment?
    # 9) Which of the following statements is correct regarding the object-oriented programming concept in Python?
    # 10) Which of the following statements is correct in this python code?
    # 11) What is the method inside the class in python language?
    # 12) Which of the following declarations is incorrect?
    # 13) Why does the name of local variables start with an underscore discouraged?
    # 14) Which of the following is not a keyword in Python language?
    # 15) Which of the following statements is correct for variable names in Python language?

def clock():
    global string,counter
    start_b.destroy()
    tt = datetime.fromtimestamp(counter)
    string = tt.strftime("%H:%M:%S")
    countup.config(text=string)
    countup.after(1000, lambda: [clock()])
    counter -= 1

root=Tk()
root.geometry('1500x1000+200+1')
counter=70200

frame = Frame(root, bg="gray33")
frame.place(x=1060, y=0, height=1000, width=1000)
frame = Frame(root, bg="Dim gray")
frame.place(x=1060, y=350, height=1000, width=1000)

countup=Label(root,font='times 40 bold', bg="gray33",fg='white')
countup.place(x=1180,y=130)
start_b=Button(root,text='Start  Test',font='times 25 bold',bg='grey70',command=lambda :[submit(),clock()])
start_b.place(x=1200,y=130)



# clock()

root.mainloop()
