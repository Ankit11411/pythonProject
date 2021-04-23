class extfile:
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def division(x, y):
        return x / y

    def factorial(x):
        ans = 1
        while x != 0:
            ans = ans * x
            x = x - 1
        return ans

    def fibonacci(x):
        a = 1
        b = 0
        ans = [b, a]
        for i in range(x - 2):
            c = a + b
            b = a
            a = c
            ans.append(c)

        return ans

    def reverse(x):
        rev = 0
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10
        return rev

    def triangle(x):
        sp = x * 2 - 2
        for i in range(x):
            for j in range(0, sp):
                print(" ", end="")
            sp = sp - 2
            for k in range(i+1):
                print('*   ', end='')

            print("")
    def star(x):
        sp = 2
        for i in range(1,x, 1):
            for j in range(sp):
                print(" ", end="")
            sp = sp + 2
            for k in range(x - i):
                print('*   ', end="")
            print("")

