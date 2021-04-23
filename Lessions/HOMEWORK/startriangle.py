'''z = int(input("Enter a number"))


for i in range(0, z, 1):
    for j in range(0, i , 1):
        print("  ", end="")
    for k in range(0, z-i, 1):
        print(k+1, end="   ")

    print("")'''

'''z = int(input("Enter a number"))


for i in range(0, z, 1):
    for j in range(0, i , 1):
        print("  ", end="")
    for k in range(0, z-i, 1):
        print(k+1, end="   ")

    print("")'''

'''n=int(input("Enter number"))

sp=n*2-2
for main in range(1,n+1):
    for space in range(sp):
        print(" ",end="")

    sp=sp-2
    for star in range(main):
        print("*   ", end="")
    print()'''

'''n = int(input("Enter number"))

sp = 0
for main in range(n, 0, -1):
    for space in range(sp):
        print(" ", end="")

    sp = sp + 2
    for star in range(main):
        print(main, "   ", end="")
    print()
'''