'''class A:
    def __init__(self, name):
        print("PARENT CLASS", name)


class B(A):
    def __init__(self, n):
        print("CHILD CLASS")
        super().__init__(n)


b = B("abc")  # B.__init__(b)'''

'''class A:
    def __init__(self):
        pass

    def add(self, a, b):
        print(a + b)


class B(A):
    def __init__(self):
        pass

    def mul(self, n1, n2):
        print(n1 * n2)


b = B()
b.add(4, 5)
b.mul(2, 3)'''

'''class A:
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2

    def add(self):
        print("Addition is ",self.num1+self.num2)

class B(A):
    def __init__(self,a,b):
        super().__init__(a,b)

    def mul(self):
        print("Multiplication is ",self.num1*self.num2)

b=B(5,6)
b.add()
b.mul()
#****************************************************

class A:
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2

    def add(self):
        print("Addition is ",self.num1+self.num2)

class B(A):
    def __init__(self):
        super().__init__(5,6)

    def mul(self):
        print("Multiplication is ",self.num1*self.num2)

b=B()
b.add()
b.mul()'''


'''class A:
    def __init__(self):
        print("PARENTCLASS A")


class B:
    def __init__(self):
        print("PARENT CALSS B")


class C(A, B):
    def __init__(self):
        print("I am Child class c")
        A.__init__(self)
        B.__init__(self)

c = C()'''




class A:
    def __init__(self):
        print("PARENTCLASS A")

    def circle(self,r):
        print ("area of circle is", 3.14*r*r)


class B:
    def __init__(self):
        print("PARENT CALSS B")

    def square(self,s):
        print("Area of square ",s**2)

class C(A, B):
    def __init__(self):
        print("I am Child class c")
        A.__init__(self)
        B.__init__(self)

    def triangle(self,b,h):
        print("area of triange is",0.5*b*h)

c = C()
c.square(4)
c.circle(5)
c.triangle(3,6)
