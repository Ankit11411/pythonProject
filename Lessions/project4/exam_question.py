from tkinter import *
from datetime import datetime
from PIL import ImageTk,Image
from tkinter import messagebox


def last():
    global next_b3
    try:
        next_b2.destroy()
        next_b1.destroy()
    except:
        pass

    frame2 = Frame(root, bg="white")
    frame2.place(x=0, y=0, height=1000, width=1000)

    l11 = Label(root, text=q11)
    l11.place(x=50, y=50)
    r31 = Radiobutton(root, text='A.', indicator=0, value=1, variable=v11, width=10)
    r31.place(x=50, y=75)
    r32 = Radiobutton(root, text='B.', indicator=0, value=2, variable=v11, width=10)
    r32.place(x=150, y=75)
    r33 = Radiobutton(root, text='C.', indicator=0, value=3, variable=v11, width=10)
    r33.place(x=50, y=100)
    r34 = Radiobutton(root, text='D.', indicator=0, value=4, variable=v11, width=10)
    r34.place(x=150, y=100)

    next_b3 = Button(root, text='Prev Page', font='times 25 bold', bg='grey70', command=next)
    next_b3.place(x=1200, y=400)


def next():
    global next_b1, next_b2
    try:
        next_b.destroy()
        next_b3.destroy()
    except:
        pass

    frame = Frame(root, bg="white")
    frame.place(x=0, y=0, height=1000, width=1000)

    l2 = Label(root, text=q6)
    l2.place(x=50, y=50)
    r21 = Radiobutton(root, text='A.', indicator=0, value=1, variable=v6, width=10)
    r21.place(x=50, y=75)
    r22 = Radiobutton(root, text='B.', indicator=0, value=2, variable=v6, width=10)
    r22.place(x=150, y=75)
    r23 = Radiobutton(root, text='C.', indicator=0, value=3, variable=v6, width=10)
    r23.place(x=50, y=100)
    r24 = Radiobutton(root, text='D.', indicator=0, value=4, variable=v6, width=10)
    r24.place(x=150, y=100)

    next_b1 = Button(root, text='Next Page', font='times 25 bold', bg='grey70', command=last)
    next_b1.place(x=1110, y=400)
    next_b2 = Button(root, text='Prev Page', font='times 25 bold', bg='grey70', command=submit)
    next_b2.place(x=1300, y=400)


def submit():
    global next_b
    # question()
    try:
        next_b2.destroy()
        next_b1.destroy()
    except:
        pass

    frm = Frame(root, bg="white")
    frm.place(x=0, y=0, height=1000, width=1000)

    l1 = Label(root, text=q1)
    l1.place(x=50, y=50)
    r11 = Radiobutton(root, text='A.         16', indicator=0, value=1, variable=v1, width=10)
    r11.place(x=50, y=75)
    r12 = Radiobutton(root, text='B.         32', indicator=0, value=2, variable=v1, width=10)
    r12.place(x=150, y=75)
    r13 = Radiobutton(root, text='C.         64', indicator=0, value=3, variable=v1, width=10)
    r13.place(x=50, y=100)
    r14 = Radiobutton(root, text='D.     None', indicator=0, value=4, variable=v1, width=10)
    r14.place(x=150, y=100)

    next_b = Button(root, text='Next Page', font='times 25 bold', bg='grey70', command=next)
    next_b.place(x=1200, y=400)
    submit_b = Button(root, text='Submit', font='times 25 bold', bg='grey70')
    submit_b.place(x=1200, y=800)


def question():
    global q1, q2, q3, q4, q5, q6, q7, q8,q11, v1, v6,v11
    q1 = '1) What is the maximum possible length of an identifier?'
    q2 = '2) Who developed the Python language?'
    q3 = '3) In which year was the Python language developed?'
    q4 = '4) In which language is Python written?'
    q5 = '5) Which one of the following is the correct extension of the Python file?'
    q6 = '6) In which year was the Python 3.0 version developed?'
    q7 = '7) What do we use to define a block of code in Python language?'
    q8 = '8) Which character is used in Python to make a single line comment?'
    q9 = '9) Which of the following statements is correct regarding the object-oriented programming concept in Python?'
    q10 = '10) Which of the following statements is correct in this python code?'
    q11 = '11) What is the method inside the class in python language?'
    q12 = '12) Which of the following declarations is incorrect?'
    q13 = '13) Why does the name of local variables start with an underscore discouraged?'
    q14 = '14) Which of the following is not a keyword in Python language?'
    q15 = '15) Which of the following statements is correct for variable names in Python language?'
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()
    v5 = IntVar()
    v6 = IntVar()
    v7 = IntVar()
    v8 = IntVar()
    v9 = IntVar()
    v10 = IntVar()
    v11 = IntVar()
    v12 = IntVar()
    v13 = IntVar()
    v14 = IntVar()
    v15 = IntVar()




def clock():
    global string, counter
    start_b.destroy()
    tt = datetime.fromtimestamp(counter)
    string = tt.strftime("%H:%M:%S")
    countup.config(text=string)
    countup.after(1000, lambda: [clock()])
    counter -= 1


root = Tk()
root.geometry('1500x1000+200+1')
root.title('MCQ Test')
counter = 70200
root.config(bg='white')

frame = Frame(root, bg="gray33")
frame.place(x=1060, y=0, height=1000, width=1000)
frame = Frame(root, bg="Dim gray")
frame.place(x=1060, y=350, height=1000, width=1000)

info=Label(root,text='Test will be of 30minutes\nThere will be 15 Question\n'
                     'Each Question contains 4 Options Out of which you have to select 1 right option\n'
                     'Each Question Contain 1 Marks\n1 page contain 5 question for next 5 question click on next\n\n'
                     'CLICK ON "START TEST" TO START THE TEST\nBest Of Luck',
           font='Times 20 bold',bg='white',fg='grey35')
info.place(x=50,y=300)

logo=ImageTk.PhotoImage(file="Quastech-logo.jpg")
logo_image=Label(root,image=logo).place(x=50,y=10,width=900,height=235)

countup = Label(root, font='times 40 bold', bg="gray33", fg='white')
countup.place(x=1180, y=130)
start_b = Button(root, text='Start  Test', font='times 25 bold', bg='grey70', command=lambda: [question(),submit(), clock()])
start_b.place(x=1200, y=130)

clock()

root.mainloop()
