n=int(input("ENTER no of rows: "))
m=int(input("ENTER no of Column: "))
m1=[]
m2=[]
n2=[]

for i in range(n):
    m1=[]
    for j in range(m):
        print("m[",i,"][",j,"]=",end=" ")
        m1.append(int(input()))
    m2.append(m1)
print(m2)

print("enter 2nd matrix data")
for i in range(n):
    n1=[]
    for j in range(m):
        print("m[",i,"][",j,"]=",end="")
        n1.append(int(input()))
    n2.append(n1)
print(n2)


o=[[0,0],[0,0]]

for i in range(len(m2)):
    for j in range(len(n2)):
        o[i][j]=m2[i][j]+n2[i][j]
print(m2,"+",n2)
print("\nsum= ",o)