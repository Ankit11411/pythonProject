class bank:
    __bal = 15000

    def __trans(self, amt):
        if bank.__bal > amt > 0:
            print("Successful\nRemaining Balance:",end="")
            bank.__bal = bank.__bal - amt
            print(bank.__bal)
        else:
            print("INVALID REQUEST")

    def __depo(self, amt):
        if 0 < amt < 100000:
            print("Successful\nRemaining Balance: ",end="")
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