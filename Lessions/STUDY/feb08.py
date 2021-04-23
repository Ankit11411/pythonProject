class Demo:
    name = "Kiran"  # static varible

    def __init__(self, x, y):  # (p,5,3) #constructor  #x,y  is instance varible / object veriable
        self.a = x  # 5  #a is object variable
        self.b = y  # 3

    def Addition(self):  # Addition(p)
        return (self.a + self.b)  # p.a+p.b

    def Substract(self):  # Substraction(p)
        return (self.a - self.b)  # p.a-p.b


p = Demo(5, 3)
print("Addition", p.Addition())
print("Substraction", p.Substract())
print(p.a)
print(p.b)
p1 = Demo(12, 6)
print("Addition", p1.Addition())
print("Substraction", p1.Substract())
print(p1.a)
print(p1.b)
print(p.name)
print(p1.name)
print(Demo.name)
Demo.name = "Gokul"
print(p.name)
# instance varible ( life inside constructor)
# static varible (varible life throuout the class ,same value for the object of a class)
# local varible (the variable is defind in class as a method)
