import socket

s = socket.socket()
port = 12346
host = "localhost"
s.bind((host, port))
s.listen(5)


def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


def Palindrome(n):
    rev = 0
    m = n
    while n > 1:
        gg = n % 10
        rev = rev * 10 + gg
        n = n // 10
    n = m
    if rev == n:
        return 'Palindrome'
    else:
        return 'Not Palindrome'


def Prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return 'Not Prime'
    else:
        return 'Prime'


while True:
    c, addr = s.accept()
    print("Connect from", addr)
    m = c.recv(128)
    n = c.recv(128)
    if int(m) == 1:
        fc = fact(int(n))
    elif int(m) == 2:
        fc = Palindrome(int(n))
    else:
        fc = Prime(int(n))
    ans = "Answer is " + str(fc)
    # ans = "Answer is " +str(m)
    c.send(ans.encode())
    c.close()
