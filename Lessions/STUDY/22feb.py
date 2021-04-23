# find fibonachi seriese using recursion
# factorial


'''def fibo(a, b):
    ans = a + b
    a = b
    b = ans
    n = 5

    if n==0:
        n=n-1
        break
    print(ans)
    print("")
    fibo(a, b)


fibo(0, 1)'''

'''def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))'''

'''def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


for i in range(10):
    print(fibo(i))'''

'''class A:
    def add(self,a,b):
        print(a+b)
a=A()
A.add(4,5)'''

'''class A:
    def __init__(self):
        self.bal=10000
        
'''

from Lessions.HOMEWORK.modules import extfile


# single inheritence
class A:
    def a(x, y):
        return extfile.add(x, y)


class B(A):
    def b(x, y):
        print("SUM IS", A.a(x, y))


B.b(4, 5)


# MULTIPLE
class A:
    def a(x):
        return extfile.factorial(x)


class B(A):
    def b(x):
        print("Factorial of ",x,"is",A.a(x))

B.b(5)


class C(A):
    def c(x):
        print("Factorial of ",x,"is",A.a(x))
C.c(7)

class D(A):
    def d(x):
        print("Factorial of ",x,"is",A.a(x))
D.d(8)





# multiLevel
class A:
    def a(x):
        return extfile.triangle(x)


class B(A):
    def b(x):
        B.a(x)
        return extfile.star(x)
B.a(5)

class C(B):
    def c(y):
        pass
C.b(5)

# HYBRID
class A:
    def a(x, y):
        print(x, y)


class B(A):
    def b(x, y):
        print(x, y)


class C(A):
    def c(x, y):
        print(x, y)


class D(B, C):
    def d(x, y):
        print(x, y)
