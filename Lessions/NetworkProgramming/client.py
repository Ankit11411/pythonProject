import socket

s = socket.socket()
host = "localhost"
port = 12346

s.connect((host, port))

m=input("SELECT OPTION:\n 1=Factorial\n 2=Palindrome\n 3=Prime No.\n>")
n=input("Enter a number\n>")

s.send(m.encode())
s.send(n.encode())
print(s.recv(128).decode())
s.close()