'''b = input("Enter 2nd number")
c = input("Enter 3rd number")

if a > b:
    if a > c:
        print("1st number is greater")
    else:
        print("3rd number is greater")
else:
    if b>c:
        print("2nd is greater")
    else:
        print("3rd number is greater")'''

a = int(input("Enter a number"))
ans = a
n = a - 1
# for i in range(n,0,-1):
while n != 0:
    ans = ans * n
    n = n - 1
print(ans)

for k in range(a,0,-1):
    f=1
    for i in range(k,0,-1):
        f=f*i
    print(f)




