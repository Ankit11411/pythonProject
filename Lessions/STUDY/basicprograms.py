'''print("Hello")

a=13# integer
b=5 # float
c=a+b
print("sum=",c)
d = a-b
print("diff =",d)
e = a*b
print("product=",e)
f = a/b # quotient
print("division = ",f)
g = a%b # remainder
print("modulous = ",g)
h = a//b
print("round division =",h)
#Now we are moving towards  special datatypes'''
# python program to find area of circle
'''radius = float(input("Enter a radius "))
diameter = 2 * radius
circumference = 2 *3.14 * radius
area = 3.14*radius*radius
print("radius =",radius)
print("Diameter =",diameter)
print("circumference=",circumference)
print("area  ={",area)
# find the third angle
a = float(input("Enter a side one"))
b = float(input("Enter a side two"))
c = 180-(a+b)
print("Third angle of trianglie is ",c)'''
from employee import *
basic =float(input("Enteryour basic salary"))
gross = basic+hra(basic)+da(basic)
print("your gross salary: {:10.2f}". format(gross))
net = gross-pf(basic)-itax(gross)
print("your net salary: {:10.2f}". format(net))
