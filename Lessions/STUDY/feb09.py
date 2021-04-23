# class Area:
#     pi = 3.14
#
#     def __init__(self, side, base, height, height1, radius):
#         self.s = side
#         self.b = base
#         self.h = height
#         self.h1 = height1
#         self.r = radius
#
#     def square(self):
#         s = self.s
#         sq = s ** 2
#         print("The araa of square is ", sq)
#
#     def triangle(self):
#         b = self.b
#         h = self.h
#         h1 = self.h1
#         s = (b + h + h1)
#         a = (s * (s - b) * (s - h) * (s - h1)) ** 0.5
#         print("The araa of triangle is ", a)
#
#     def circle(self):
#         ra = Area.pi * self.r ** 2
#         print("the area of circle ", ra)
#
#
# A = Area(4, 2, 3, 6, 3)
# A.square()
# A.triangle()
# A.circle()


# class Area:
#     pi=3.14
#     def __init__(self):
#          pass
#     def square(self,s):
#         sq=s** 2
#         print("The araa of square is ",sq)
#     def triangle(self,b,h,h1):
#         s=(b+h+h1)
#         a=(s*(s-b)*(s-h)*(s-h1)) ** 0.5
#         print("The araa of triangle is ", a)
#
#     def circle(self,r):
#         ra=Area.pi*r**2
#         print("the area of circle ",ra)
# A=Area()
# A.square(4)
# A.triangle(4,2,4)
# A.circle(4)

'''
class Area:
    pi = 3.14

    def __init__(self):
        self.radius = 0
        self.side = 0

    def circle(self):
        re = 3.14 * self.radius ** 2
        print("area of circle ", re)


a = Area()
a.circle()
print(a.radius)
setattr(a, "radius", 5)  # (object,attribute,value) it used for set the value to the attribute
a.circle()
print(a.radius)
getattr(a, "radius")  # (a is object,"radius" is attribute) it used for get the value of the attribute
print(a.radius)

a.circle()
a.radius = 4.23
print(a.radius)

print(hasattr(a, "side"))  # to cheak the "side" attribute have or not.,it give boolean value
print(a.radius)  # it work same as above
print("get", getattr(a, "side"))
print("**************************************************")
delattr(a, "side")  # (a is object ,"side" is attribute name) to delete the attribute
print(hasattr(a, "side"))

inheritance

withoutparameter'''


class Parent:
    def __init__(self):
        print("I am parent class")


class child(Parent):
    def __init__(self):
        print("I am child constructor ")
        super().__init__()  # Parent.__init__(c)


c = child()
p = Parent()


# with parameter
class Parent:
    def __init__(self, name):
        print("I am parent class", name)


class child(Parent):
    def __init__(self):
        print("I am child constructor ")
        super().__init__("Kiran")  # Parent.__init__(c,"kiran"_)


c = child()
p = Parent("Gokul")
