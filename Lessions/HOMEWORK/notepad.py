# Enter number and find factorial
import socket

s = socket.socket()
port = 12345
host = "localhost"

s.connect((host, port))
v = input("\n Factorial=1 \n Fibonacci=2 \n Prime=3 \n Cube=4 \n Select optin:")
n = input("Enter number :")
s.send(v.encode())
s.send(n.encode())
print(s.recv(128).decode())
s.close
