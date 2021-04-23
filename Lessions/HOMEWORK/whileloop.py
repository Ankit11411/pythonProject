
''''#FIBONACHII SERIES
def fibo(n):
    a = 0
    b = 1
    l = []
    g = []
    l.append(a)
    l.append(b)
    while n != 0:
        t = a + b
        a = b
        b = t
        l.append(t)
        n = n - 1
    return l


s = int(input("Enetr nmber"))
d = fibo(s)
d.reverse()
print(d)'''


#TRIANGLE
'''n = int(input("Enter number"))
gg = n
m = n
a = n
while m != 0:
    while n != 0:
        print("  ", end="")
        n = n - 1

    while m != a+1:
        print("*   ", end="")
        a = a - 1
    print("")
    m = m - 1
    n = m
    a = gg'''


#STAR TRIANGLE


'''n = int(input("Enter number"))
gg = n
m = n
a = n
while m != 0:
    while n != 0:
        print("  ", end="")
        n = n - 1

    while m != a + 1:
        print("*   ", end="")
        a = a - 1
    print("")
    m = m - 1
    n = m
    a = gg

m = gg
a = gg
n = gg-1
while m != 0:
    while m != a + 2:
        print("  ", end="")
        a = a - 1
    while n != 0:
        print("*   ", end="")
        n = n - 1
    print("")
    m = m - 1
    a = gg
    n = m-1'''

n=int(input("Enter size: "))
sp=n*2-2
main=1
while main <= n:
    space=0
    while space<sp:
        print(" ",end="")
        space=space+1
    sp=sp-2
    star=1
    while star<=main:
        print("*",end="   ")
        star=star+1
    main=main+1
    print()
