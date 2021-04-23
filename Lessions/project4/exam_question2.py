from tkinter import *
from datetime import datetime
from tkinter import messagebox
from PIL import ImageTk, Image


def stop():
    a1 = v1.get()
    a2 = v2.get()
    a3 = v3.get()
    a4 = v4.get()
    a5 = v5.get()
    a6 = v6.get()
    a7 = v7.get()
    a8 = v8.get()
    a9 = v9.get()
    a10 = v10.get()
    a11 = v11.get()
    a12 = v12.get()
    a13 = v13.get()
    a14 = v14.get()
    a15 = v15.get()
    get_answer = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]
    r_answer = [4, 2, 4, 4, 1, 1, 3, 3, 2, 2, 2, 2, 3, 1, 2]
    count = 1
    correct_answer = []
    for i, j in zip(get_answer, r_answer):
        if i == j:
            # print('equal=',i,"===",j,count)
            correct_answer.append(count)
        count = count + 1
    # print(correct_answer)
    # print(len(correct_answer))
    yn = messagebox.askyesno("Be sure!", "Are you sure you want to submit?")
    if yn:
        msg = 'Your Score is ' + str(len(correct_answer)) + '/20'
        messagebox.showinfo('',msg)
        root.destroy()


def last():
    global next_b3
    try:
        next_b2.destroy()
        next_b1.destroy()
    except:
        pass

    frame2 = Frame(root, bg="white")
    frame2.place(x=0, y=0, height=910, width=1000)

    l2 = Label(root, text=q11, bg='white', font='times 15 bold')
    l2.place(x=50, y=50)
    r21 = Radiobutton(root, text='A.  Object', indicator=0, value=1, variable=v11, width=20)
    r21.place(x=50, y=75)
    r22 = Radiobutton(root, text='B.  Function', indicator=0, value=2, variable=v11, width=20)
    r22.place(x=200, y=75)
    r23 = Radiobutton(root, text='C.  Attribute', indicator=0, value=3, variable=v11, width=20)
    r23.place(x=50, y=100)
    r24 = Radiobutton(root, text='D.  Argument', indicator=0, value=4, variable=v11, width=20)
    r24.place(x=200, y=100)

    l11 = Label(root, text=q12, bg='white', font='times 15 bold')
    l11.place(x=50, y=150)
    r31 = Radiobutton(root, text='A.  _x = 2', indicator=0, value=1, variable=v12, width=20)
    r31.place(x=50, y=175)
    r32 = Radiobutton(root, text='B.  __x = 3', indicator=0, value=2, variable=v12, width=20)
    r32.place(x=200, y=175)
    r33 = Radiobutton(root, text='C.  __xyz__ = 5', indicator=0, value=3, variable=v12, width=20)
    r33.place(x=50, y=200)
    r34 = Radiobutton(root, text='D.  None of these', indicator=0, value=4, variable=v12, width=20)
    r34.place(x=200, y=200)

    l11 = Label(root, text=q13, bg='white', font='times 15 bold')
    l11.place(x=50, y=250)
    r31 = Radiobutton(root, text='A.  To identify the variable', indicator=0, value=1, variable=v13, width=60)
    r31.place(x=50, y=275)
    r32 = Radiobutton(root, text='B.  It confuses the interpreter', indicator=0, value=2, variable=v13, width=60)
    r32.place(x=50, y=300)
    r33 = Radiobutton(root, text='C.  It indicates a private variable of a class', indicator=0, value=3, variable=v13,
                      width=60)
    r33.place(x=50, y=325)
    r34 = Radiobutton(root, text='D.  None of these', indicator=0, value=4, variable=v13, width=60)
    r34.place(x=50, y=350)

    l11 = Label(root, text=q14, bg='white', font='times 15 bold')
    l11.place(x=50, y=400)
    r31 = Radiobutton(root, text='A.  val', indicator=0, value=1, variable=v14, width=20)
    r31.place(x=50, y=425)
    r32 = Radiobutton(root, text='B.  raise', indicator=0, value=2, variable=v14, width=20)
    r32.place(x=200, y=425)
    r33 = Radiobutton(root, text='C.  try', indicator=0, value=3, variable=v14, width=20)
    r33.place(x=50, y=450)
    r34 = Radiobutton(root, text='D.  with', indicator=0, value=4, variable=v14, width=20)
    r34.place(x=200, y=450)

    l11 = Label(root, text=q15, bg='white', font='times 15 bold')
    l11.place(x=50, y=500)
    r31 = Radiobutton(root, text='A.  All variable names must begin with an underscore.', indicator=0, value=1,
                      variable=v15, width=60)
    r31.place(x=50, y=525)
    r32 = Radiobutton(root, text='B.  Unlimited length ', indicator=0, value=2, variable=v15, width=60)
    r32.place(x=50, y=550)
    r33 = Radiobutton(root, text='C.  The variable name length is a maximum of 2.', indicator=0, value=3, variable=v15,
                      width=60)
    r33.place(x=50, y=575)
    r34 = Radiobutton(root, text='D.  All of the above', indicator=0, value=4, variable=v15, width=60)
    r34.place(x=50, y=600)

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
    frame.place(x=0, y=0, height=910, width=1000)

    l2 = Label(root, text=q6, bg='white', font='times 15 bold')
    l2.place(x=50, y=50)
    r21 = Radiobutton(root, text='A. 2008', indicator=0, value=1, variable=v6, width=20)
    r21.place(x=50, y=75)
    r22 = Radiobutton(root, text='B. 2000', indicator=0, value=2, variable=v6, width=20)
    r22.place(x=200, y=75)
    r23 = Radiobutton(root, text='C. 2010', indicator=0, value=3, variable=v6, width=20)
    r23.place(x=50, y=100)
    r24 = Radiobutton(root, text='D. 2005', indicator=0, value=4, variable=v6, width=20)
    r24.place(x=200, y=100)

    l2 = Label(root, text=q7, bg='white', font='times 15 bold')
    l2.place(x=50, y=150)
    r21 = Radiobutton(root, text='A.  Key', indicator=0, value=1, variable=v7, width=20)
    r21.place(x=50, y=175)
    r22 = Radiobutton(root, text='B.  Brackets', indicator=0, value=2, variable=v7, width=20)
    r22.place(x=200, y=175)
    r23 = Radiobutton(root, text='C.  Indentation', indicator=0, value=3, variable=v7, width=20)
    r23.place(x=50, y=200)
    r24 = Radiobutton(root, text='D. None of these', indicator=0, value=4, variable=v7, width=20)
    r24.place(x=200, y=200)

    l2 = Label(root, text=q8, bg='white', font='times 15 bold')
    l2.place(x=50, y=250)
    r21 = Radiobutton(root, text='A.    /', indicator=0, value=1, variable=v8, width=20)
    r21.place(x=50, y=275)
    r22 = Radiobutton(root, text='B.    //', indicator=0, value=2, variable=v8, width=20)
    r22.place(x=200, y=275)
    r23 = Radiobutton(root, text='C.    #', indicator=0, value=3, variable=v8, width=20)
    r23.place(x=50, y=300)
    r24 = Radiobutton(root, text='D.    !', indicator=0, value=4, variable=v8, width=20)
    r24.place(x=200, y=300)

    l2 = Label(root, text=q9, bg='white', font='times 15 bold')
    l2.place(x=50, y=350)
    r21 = Radiobutton(root, text='A.  Classes are real-world entities while objects are not real', indicator=0, value=1,
                      variable=v9, width=60)
    r21.place(x=50, y=375)
    r22 = Radiobutton(root, text='B.  Objects are real-world entities while classes are not real', indicator=0, value=2,
                      variable=v9, width=60)
    r22.place(x=50, y=400)
    r23 = Radiobutton(root, text='C.  Both objects and classes are real-world entities', indicator=0, value=3,
                      variable=v9, width=60)
    r23.place(x=50, y=425)
    r24 = Radiobutton(root, text='D.  All of the above', indicator=0, value=4, variable=v9, width=60)
    r24.place(x=50, y=450)

    l2 = Label(root, text=q10, bg='white', font='times 15 bold')
    l2.place(x=50, y=500)
    r21 = Radiobutton(root, text='A.   a ^ b', indicator=0, value=1, variable=v10, width=20)
    r21.place(x=50, y=525)
    r22 = Radiobutton(root, text='B.    a**b', indicator=0, value=2, variable=v10, width=20)
    r22.place(x=200, y=525)
    r23 = Radiobutton(root, text='C.    a ^ ^ b', indicator=0, value=3, variable=v10, width=20)
    r23.place(x=50, y=550)
    r24 = Radiobutton(root, text='D.    a ^ * b', indicator=0, value=4, variable=v10, width=20)
    r24.place(x=200, y=550)

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

    l1 = Label(root, text=q1, bg='white', font='times 15 bold')
    l1.place(x=50, y=50)
    r11 = Radiobutton(root, text='A.         16', indicator=0, value=1, variable=v1, width=20)
    r11.place(x=50, y=75 + 10)
    r12 = Radiobutton(root, text='B.         32', indicator=0, value=2, variable=v1, width=20)
    r12.place(x=200, y=75 + 10)
    r13 = Radiobutton(root, text='C.         64', indicator=0, value=3, variable=v1, width=20)
    r13.place(x=50, y=100 + 10)
    r14 = Radiobutton(root, text='D.     None', indicator=0, value=4, variable=v1, width=20)
    r14.place(x=200, y=100 + 10)

    l1 = Label(root, text=q2, bg='white', font='times 15 bold')
    l1.place(x=50, y=150 + 20)
    r11 = Radiobutton(root, text='A.  Zim Den', indicator=0, value=1, variable=v2, width=20)
    r11.place(x=50, y=175 + 30)
    r12 = Radiobutton(root, text='B.  Guido van Rossum', indicator=0, value=2, variable=v2, width=20)
    r12.place(x=200, y=175 + 30)
    r13 = Radiobutton(root, text='C.  Niene Stom', indicator=0, value=3, variable=v2, width=20)
    r13.place(x=50, y=200 + 30)
    r14 = Radiobutton(root, text='D.  Wick van Rossum', indicator=0, value=4, variable=v2, width=20)
    r14.place(x=200, y=200 + 30)

    l1 = Label(root, text=q3, bg='white', font='times 15 bold')
    l1.place(x=50, y=250 + 40)
    r11 = Radiobutton(root, text='A.    1995', indicator=0, value=1, variable=v3, width=20)
    r11.place(x=50, y=275 + 50)
    r12 = Radiobutton(root, text='B.    1972', indicator=0, value=2, variable=v3, width=20)
    r12.place(x=200, y=275 + 50)
    r13 = Radiobutton(root, text='C.    1981', indicator=0, value=3, variable=v3, width=20)
    r13.place(x=50, y=300 + 50)
    r14 = Radiobutton(root, text='D.    1989', indicator=0, value=4, variable=v3, width=20)
    r14.place(x=200, y=300 + 50)

    l1 = Label(root, text=q4, bg='white', font='times 15 bold')
    l1.place(x=50, y=350 + 60)
    r11 = Radiobutton(root, text='A.    English', indicator=0, value=1, variable=v4, width=20)
    r11.place(x=50, y=375 + 70)
    r12 = Radiobutton(root, text='B.    PHP', indicator=0, value=2, variable=v4, width=20)
    r12.place(x=200, y=375 + 70)
    r13 = Radiobutton(root, text='C.    C', indicator=0, value=3, variable=v4, width=20)
    r13.place(x=50, y=400 + 70)
    r14 = Radiobutton(root, text='D.    All of the above', indicator=0, value=4, variable=v4, width=20)
    r14.place(x=200, y=400 + 70)

    l1 = Label(root, text=q5, bg='white', font='times 15 bold')
    l1.place(x=50, y=450 + 80)
    r11 = Radiobutton(root, text='A.    .py', indicator=0, value=1, variable=v5, width=20)
    r11.place(x=50, y=475 + 90)
    r12 = Radiobutton(root, text='B.    .python', indicator=0, value=2, variable=v5, width=20)
    r12.place(x=200, y=475 + 90)
    r13 = Radiobutton(root, text='C.    .python', indicator=0, value=3, variable=v5, width=20)
    r13.place(x=50, y=500 + 90)
    r14 = Radiobutton(root, text='D.    None of these', indicator=0, value=4, variable=v5, width=20)
    r14.place(x=200, y=500 + 90)

    next_b = Button(root, text='Next Page', font='times 25 bold', bg='grey70', command=next)
    next_b.place(x=1110, y=400)
    submit_b = Button(root, text='Submit', font='times 25 bold', bg='grey70', command=stop)
    submit_b.place(x=1110, y=800)


def question():
    global q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15
    q1 = '1) What is the maximum possible length of an identifier?'
    q2 = '2) Who developed the Python language?'
    q3 = '3) In which year was the Python language developed?'
    q4 = '4) In which language is Python written?'
    q5 = '5) Which one of the following is the correct extension of the Python file?'
    q6 = '6) In which year was the Python 3.0 version developed?'
    q7 = '7) What do we use to define a block of code in Python language?'
    q8 = '8) Which character is used in Python to make a single line comment?'
    q9 = '9) Which of the following statements is correct regarding the object-oriented programming concept in Python?'
    q10 = '10) Which of the following operators is the correct option for power(ab)?'
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

info = Label(root, text='Test will be of 30minutes\nThere will be 15 Question\n'
                        'Each Question contains 4 Options Out of which you have to select 1 right option\n'
                        'Each Question Contain 1 Marks\n1 page contain 5 question for next 5 question click on next\n\n'
                        'CLICK ON "START TEST" TO START THE TEST\nBest Of Luck',
             font='Times 20 bold', bg='white', fg='grey35')
info.place(x=50, y=300)

logo = ImageTk.PhotoImage(file="Quastech-logo.jpg")
logo_image = Label(root, image=logo).place(x=50, y=10, width=900, height=235)

countup = Label(root, font='times 40 bold', bg="gray33", fg='white')
countup.place(x=1180, y=130)
start_b = Button(root, text='Start  Test', font='times 25 bold', bg='grey70',
                 command=lambda: [question(), submit(), clock()])
start_b.place(x=1200, y=130)

# clock()

root.mainloop()
