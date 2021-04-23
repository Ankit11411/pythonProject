class Animal:
    def __init__(self, e, l):
        self.eyes = e
        self.legs = l

    def eat(self):
        print("eatr")

    def sleep(self):
        print("slpewp")


class Dog(Animal):
    def __init__(self,e,l):
        super().__init__(e,l)

    def bark(self):
        print("BArk")


class Cat(Animal):
    def __init__(self,e,l):
        super().__init__(e,l)

    def run(self):
        print("Run")


d = Dog('Brown',4)
d.bark()
d.eat()
c= Cat('blue',4)
c.eat()
c.run()


