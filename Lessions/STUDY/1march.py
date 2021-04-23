# ENTER no from user and store fibonachi series on files

import mysql.connector as my

'''n = int(input("Enter a numbr: "))
l = []
a = 0
b = 1
l.append(a)
l.append(b)

for i in range(n - 2):
    ans = a + b
    a = b
    b = ans
    l.append(ans)

ww = ""
for i in l:
    gg = str(i)
    ww = ww + gg

f = open("factorial.txt", 'w')
print(ww)
f.write(ww)
f.close()
'''

'''conn = my.connect(username='root', password='root', host='localhost', database='emp')
cur = conn.cursor()

# q='create database emp'
q = 'create table employee(name varchar(20), dept varchar(20),salary'

cur.execute(q)
conn.close()
print("SUCCESS")'''

# REGULAR EXP:RE MODULES
'''
functions:
1. findall()
2. search
3. split()
3. sub()

operation:
\d: string numbers
^: string start
$: string end
*: string avail

(set)
[hfn]: string avail
[a-d]: string avail 
[^hfn]: Not avail
'''

import re

# tx = "Hello how are you"
# x = re.findall("Hell", tx)
# x = re.findall("^Hello", tx)
# x = re.findall("Hellox*", tx)

# print(x)

# USING 2 list convert list into dictionary using update
# dict values store into list

'''l1 = [1, 2, 3, 4, 5, 6]
l2 = ['a', 'b', 'c', 'd', 'e', 'f']
l3 = {}
j = 0
for i in l1:
    l3.update({i: l2[j]})
    j = j + 1
print(l3)'''

d = {1: 'a', 2: 'b', 3: 'c'}
q = []
w = []

x = d.values()
y = d.keys()
for i in x:
    q.append(i)
for j in y:
    w.append(j)
print(q)
print(w)
