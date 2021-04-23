import socket

s=socket.socket()
host = 'localhost'
port = 12347

s.connect((host,port))

aaa= input("ENETR A NUMBER:\n")

s.send(aaa.encode())
print(s.recv(128).decode())
s.close()