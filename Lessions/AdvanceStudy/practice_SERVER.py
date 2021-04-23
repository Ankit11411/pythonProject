import socket

s = socket.socket()
host = 'localhost'
port = 12347

s.bind((host,port))
s.listen(2)

running = True

while running:
    c,addr = s.accept()
    print(c,addr)
    aaa=c.recv(128)
    aaa=int(aaa)
    print(int(aaa))
    if aaa== 1:
        print("!!!!")
        ans=12
    elif aaa == 2:
        print("2222")
        ans=23
    else:
        print("#$#%^56")
        ans=3456789
    c.send(str(ans).encode())


    c.close()
