'''def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)

f=open("fact.txt","")'''

# DAtaBAse CONNECTIVITY

import mysql.connector as my

conn = my.connect(username='root', password='root', host='localhost', database='qwerty')

cur = conn.cursor()

# q="create database qwerty"
# q="create table uiop(roll_no int,name varchar(20),class varchar(20))"
r = int(input("Enter Rollno"))
# n = input("Enter Name")
# c = input("Enter Class")
# v = (r, n, c)
#
# q = "insert into uiop (roll_no,name,class) values(%s,%s,%s)"

q= "delete from uiop where roll_no=%s"%(r)

cur.execute(q)
conn.commit()
conn.close()
print("SUCESS")
