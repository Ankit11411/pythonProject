import time
import threading

'''def q1():
    for i in range(10):
        print("q1",i)
        time.sleep(1)

def q2():
    for i in range(10):
        print("q2",i)
        time.sleep(1)
t1=threading.Thread(target=q1)
t2=threading.Thread(target=q2)

# t1.start()
# time.sleep(0.01)
# t2.start()
#
# t1.join()
# t2.join()

t1.start()
t1.join()

t2.start()
t2.join()'''


# Q. Find fact 1 to 10 and fibo series 10 using asyn thread?

def fact():
    for j in range(10):
        f = 1
        for i in range(1, j + 2):
            f = f * i
        print("\nFactorial", i, "=", f)
        time.sleep(1)


def fibo():
    for i in range(10):
        a = 0
        b = 1
        n = i + 1
        ans = 0
        while n != 0:
            ans = a + b
            a = b
            b = ans
            n = n - 1
        print("Fibonachi", i + 1, "=", ans)
        time.sleep(1)


t1 = threading.Thread(target=fact)
t2 = threading.Thread(target=fibo)

t1.start()
time.sleep(0.1)
t2.start()

t1.join()
t2.join()
