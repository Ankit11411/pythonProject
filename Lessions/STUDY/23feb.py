# list1 = []
# list2 = []
# list3 = []
# n = int(input("Enter size of matrix: "))
#
# for i in range(n):
#     gg = int(input("Enter list1 element"))
#     list1.append(gg)
# for j in range(n):
#     gj = int(input("Enter list2 element"))
#     list2.append(gj)
#
# for k in range(n):
#     list3.append(list1[n - 1] + list2[n - 1])
# print(list3)


'''m1 = [[1, 2], [4, 3]]
m2 = [[6, 2], [9, 7]]
m3 = [[0,0],[0,0]]

for i in range(len(m1)):
    for j in range(len(m2)):
        m3[i][j]=(m1[i][j] + m2[i][j])

print(m3)'''

'''#Ploymorphism:
def add(a,b,c=0):
    print(a+b+c)
add(4,5)
add(4,5,6)'''


# Encapsulation: Data and function hide

'''class bank:
    __bal = 15000

    def __trans(self, amt):
        if bank.__bal > amt > 0:
            print("Transaction amt:")
            bank.__bal = bank.__bal - amt
            print(bank.__bal)
        else:
            print("INVALID REQUEST")

    def __depo(self, amt):
        if 0 < amt < 100000:
            print("Deposit Amount:")
            bank.__bal = bank.__bal + amt
            print(bank.__bal)
        else:
            print("INVALID REQUEST")

    def ts(self, m):
        bank.__trans(self, m)

    def ds(self, m):
        bank.__depo(self, m)


z = bank()
print("Select the Following Option: \n1.WITHDRAW    2.DEPOSIT    3.Exit")
i = int(input(">"))
while i > 0:

    if i == 1:
        a = int(input("enter amount to withdraw: \n>"))
        z.ts(a)
    elif i == 2:
        b = int(input("Enter amount to deposit: \n>"))
        z.ds(b)
    elif i == 3:
        # i=-1
        exit()
    else:
        print("Invalid Request")
        i = -1
    print("**********************************")
    print("Select the Following Option: \n1.WITHDRAW    2.DEPOSIT    3.Exit")
    i = int(input(">"))
'''