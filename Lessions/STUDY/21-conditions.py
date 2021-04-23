'''x = int(input("Enter a number"))
if x % 2 == 0:
    print(x , " is even number")
else:
    print(x , "is odd number")'''





'''angle1 = int(input("Enter a  first number"))
angle2 = int(input("Enter a  second number"))
angle3 = int(input("Enter a  third number"))
if (sum == 180 and angle1>0 and angle2>0 and angle3 >0):
    print("its a valid triangle")
else:
    print("its not a valid triangle")
if (angle1==angle2 and angle2== angle3):
    print("it is an equilateral triangle")
elif(angle1 == angle2  or angle1==angle3):
    print("it is an Isoceles Triangle")
else:
    print(" it is a scalene triangle")

syntax for i in range /for( int i = 0;i<=10;i++)'''





#for i in range(10,0,-1):
    #print(i)

'''start = int(input("Enter a  start number"))
end = int(input("Enter a end number"))
for i in range(start,end+1):
    for j in range(1,11):
        print(i, "*", j, "=", (i*j))

for i in range(start,end+1):
    if i %2!=0:
        print(i)
#7th january 2021: while loops and programming
n=int(input("Enter number:"))
count=0
while(n>0): # 4
    count=count+1 #1+1=2+=3
    n=n//10 #4//10=0
print("The number of digits in the number are:",count)'''





'''n=int(input("Enter number:"))
temp = n
reverse=0
while(n!=0):
    reverse = (reverse*10) + (n % 10)
    n //= 10
print("reverse of a digits is ", reverse)
if(temp==reverse):
    print("its a palindrome")
else:
    print("its not a palindrome")'''





#_____________________________
#13th wednesday Special dataype
'''num =[10.8,"vani",30,40,"raju"]
print(" Total list =", num)
print("first= %f,last =%s" %(num[0],num[4]))
print("using while loop")
i=0
while i<len(num):
    print(num[i])
    i=i+1
print("using for loop")
for i in num:
    print(i)
days=['sunday','monday','tuesday','wed','thurs','fri','sat']
print('\n In reverse order: ')
i = len(days)-1
while i>=0:
    print(days[i])
    i-=1
z=x[:] #clone 
x[1]=99
print(x)
print(z)
j=x#alias
x[2]=23
num = [10,20,30,40,50]
n = len(num)
print("length ",n)
num.append(60)
print("after append ",num)
num.insert(0,5)
print("After inserting value ",num)
num1=num.copy()
print("After copying ", num1)
j = num.count(30)
print("number of times 30 present ",j)
num.remove(50)
print("After removing 50 ",num)
num.reverse()
print("After reversing ",num)
num.sort()
print("After sorting ", num)
num.pop()
print("After pop ", num)
num.clear()
print("After clear ", num)
x =[]
n = int(input("how many  elements? "))
for i in range(n):
    print("enter a elemnt: ",end='')
    x.append(int(input()))
print("the complete list ", x)
y = int(input("Enter a element to get a count: "))
c=0
for i in x:
    if(y==i):
        c+=1
print("{} is found {} times. ".format(y,c))

s1=["vinay","Pravin","Amit","Shravan","govind"]
s2 =["Umeer","vinay","vishal","Amit"]
s3 = set(s1)
s4=set(s2)
intersect=s3.intersection(s4)
common = list(intersect)
print(common)'''




'''Tuples 14-1-2021'''
'''num=eval(input("Enter a elements in ()"))
sum=0
n=len(num)
for i in range(n):
    sum+=num[i]
print(" SUm of number is ",sum)
print("Average of num is ", sum/n)

names = ('vishnu','Anupama','Lakshmi','Beshma')
print(names)
#lst = [input("Enter a new name: ")]
#new = tuple(lst)
pos = int(input('Enter position no'))
names1=names[0:pos-1]
#names1= names1-new
names = names1+names[pos:]
print(names)

emp=[]
n = int(input(" Enter  how many employee ? "))
for i in range(n):
    print("Enter a id ",end='')
    emp.append(int(input()))
    print("Enter a name ", end='')
    emp.append(input())
    print("Enter a salary ", end='')
    emp.append(float(input()))
print('The list is completed with emp details ')
id = int(input(" Enter a id to search"))
for i in range(len(emp)):
    if id ==emp[i]:
        print("id ={:d}, Name ={:s},salary={:.2f}".format(emp[i],emp[i+1],emp[i+2]))
        break'''





'''monday 18-1-2021/dictionary'''
'''dict ={'Name':'chandra','ID':200,'Salary':'9080.50'}
print('Name of the employee = ',dict['Name'])
print('ID of the employee = ',dict['ID'])
print('Salary of the employee = ',dict['Salary'])
print(dict)
print('keys in dict = ',dict.keys())
print('values in dict= ',dict.values())
print("items in dict =",dict.items())
dict=eval(input("enter a elements in { }: " ))
s = sum(dict.values())
print("sum of values: ",s)

x = {}
print("how many payers ? ",end='')
n = int(input())
for i in range(n):
    print("Enter name of player : ", end=' ')
    k = input()
    print("Enter runs: ",end='')
    v = int(input())
    x.update({k:v})
print('\n players in the match: ')
for pname in x.keys():
    print(pname)
print(" enter the name of player to find ", end='')
name=input()
runs=x.get(name,-1)
if(runs==-1):
    print('player not found')
else:
    print("{} made runs {}.".format(name,runs))'''





'''str ="core python"
n = len(str)
i=0
while i<n:
    print(str[i],end=' ')
    i+=1
print()
i=1
while i<=n:
    print(str[-i],end=' ')
    i+=1
print()
str=input('Enter a main string')
sub=input("Enter a substring")
if sub in str:
    print(sub ,'is found in main string')
else:
    print(sub , 'is not found in main string')
n=str.find(sub,0,len(str))
if n ==-1:
    print("sub string not found:")
else:
    print(("sub string found at position : ",n+1))
print(str)
print(str.lstrip())
print(str.rstrip())
print(str.strip())'''





''''Function 20-1-21'''
'''def sum(a,b):
    c=a+b
    return c
x=sum(10,50)
y=sum(1.5,10.75)
print("the sum is ", x)
print('The sum is ',y)'''




'''def even_odd(num):
    if num %2 == 0:
        print(num, " is even")
    else:
        print(num, " is odd")
even_odd(12)
even_odd(13)
def fact(n):
    prod =1
    while n>=1:
        prod*=n
        n-=1
    return prod
for i in range(1,11):
    print("factorial of a {} is {} ".format(i, fact(i)))'''




'''def sum_sub_mul_div(a,b):
    c=a +b
    d= a-b
    e= a *b
    f = a/b
    return c,d,e,f
t=sum_sub_mul_div( 10,5)
for i in t:
    print(i,end=' , ')
def grocery(item,price=40.00):
    print('Item = %s' % item)
    print('price = %.2f ' % price)
grocery(item ='sugar')
grocery(price=90.88,item='oil')
#grocery(99.88,'soap')'''




'''' 25 january -lambda-2021'''

'''f=lambda x,y:x+y
value =f(5,55.5)
print('sum = ',value)

max =lambda x,y: x if x>y else y
a,b =[int(n) for n in input("enter two numbers: ").split(',')]
print('Bigger number = ',max(a,b))'''





'''def iseven(x):
    if x%2==0:
        return True
    else:
        return False
lst =[10,23,45,46,70,99]
lst1=list(filter(iseven,lst))
print(lst1)

lst =[10,23,45,46,70,99]
lst1 =list(filter(lambda x:(x%2==0),lst))
print(lst1)


lst =[1,2,3,4,5]
lst1 =list(map(lambda x:x*x,lst))
print(lst1)

lst1=[1,2,3,4,5]
lst2=[10,20,30,40,50]
lst3=list(map(lambda x,y:x*y,lst1,lst2))
print(lst3)

def decor(fun):
    def inner():
        value = fun()
        return value +2
    return inner
def num():
    return 10
result_fun=decor(num)
print(result_fun())

def da(basic):
    da=basic*80/100
    return da
def hra(basic):
    hra=basic*15/100
    return hra
def pf(basic):
    pf=basic*12/100
    return pf
def itax(gross):
    tax=gross*0.1
    return tax
basic =float(input("Enteryour basic salary"))
gross = basic+hra(basic)+da(basic)
print("your gross salary: {:10.2f}". format(gross))
net = gross-pf(basic)-itax(gross)
rint("your net salary: {:10.2f}". format(net))'''




