'''a = 0
b = 1
c = []
print(a)
print(b)


def fibonachii():
    for i in range(0,10):
        global a
        global b
        ans = a + b
        a = b
        b = ans
        print(ans)
        c[i] = ans


fibonachii()
print(c[i])'''


def fibo(n):
    a = 0
    b = 1
    l = []
    g=[]
    l.append(a)
    l.append(b)
    for i in range(n):
        t = a + b
        a = b
        b = t
        l.append(t)

    return l

print(fibo(6))

# s = int(input("Enetr nmber"))
# d=fibo(s)
# d.reverse()
# print(d)

n = int(input("Enter number"))

sp = n*2-2

for main in range(1, n+1):
    for space in range(sp):
        print(" ", end="")
    sp=sp-2
    for star in range(main):
        print("*   ",end="")
    print()

sp=2
for main in range(1,n,1):
    for space in range(sp):
        print(" ",end="")
    sp=sp+2
    for star in range(n-main):
        print('*   ',end="")
    print("")


