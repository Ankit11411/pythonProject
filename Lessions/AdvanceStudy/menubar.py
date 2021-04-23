from tkinter import *
from tkinter.filedialog import *


def des():
    w.destroy()


def non():
    pass


def save():
    try:
        f1 = asksaveasfile(filetype=[('python file', '*.py'), ('text', '*.txt')])
        f1.write(nt.get("0.1", "end"))
        f1.close()
    except AttributeError:
        pass


def new():
    global w, mb, nt
    w = Tk()
    w.title("Notepad")
    w.geometry("300x300")
    mb = Menu(w)

    sb = Scrollbar(w)
    sb.pack(side=RIGHT, fill=Y)
    sb1 = Scrollbar(w, orient='horizontal')
    sb1.pack(side=BOTTOM, fill=X)
    nt = Text(w, height=59, width=237, wrap=NONE, yscrollcommand=sb.set, xscrollcommand=sb1.set)
    nt.pack(side="left")
    f1 = Menu(mb, tearoff=0)
    f1.add_command(label="New", command=lambda: [des(), new()])
    f1.add_command(label="Open", command=openf)
    f1.add_command(label="Save", command=save)
    f1.add_separator()
    f1.add_command(label="Exit", command=des)
    mb.add_cascade(label="File", menu=f1)

    e1 = Menu(mb, tearoff=0)
    e1.add_command(label="Cut", command=non)
    e1.add_command(label="Copy", command=non)
    e1.add_command(label="Paste", command=non)
    mb.add_cascade(label="Edit", menu=e1)

    e2 = Menu(mb, tearoff=0)
    e2.add_command(label="About", command=non)
    mb.add_cascade(label="Help", menu=e2)

    w.config(menu=mb)
    sb1.config(command=nt.xview)
    sb.config(command=nt.yview)

    w.mainloop()


def openf():
    fil = askopenfile(mode="r+", filetype=[('python file', '*.py'), ('text', '.txt')])
    data = fil.read()
    nt.insert(END, data)
    fil.close()


new()
