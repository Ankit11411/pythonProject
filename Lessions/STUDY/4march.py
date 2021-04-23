import mysql.connector as my

conn = my.connect(username='root', password='root', host='localhost', database='regform2')
cur = conn.cursor()

# q="create database regform2"
# q = "create table detail(FName varchar(20),LName varchar(20),Address varchar(30),contact int,email varchar(20)" \
#     ",gender varchar(20),hobbies varchar(30),qualification varchar(20))"
q=""


cur.execute(q)
# conn.commit()
conn.close()
