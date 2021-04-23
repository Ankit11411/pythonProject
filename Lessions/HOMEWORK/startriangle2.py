n = []
for a in range(5):
    n.append(str(input("enter Character")))
    for i in range(a + 1):
        for j in range(5 - i):
            print(" ", end="")
        for j in range(i+ 1):
            print(n[j], end=" ")
        print()
for i in range(1):
    print(i)
# n = ""
# for a in range(5):
#     s=input("enter Character")
#     n=n+s
#     for i in range(a + 1):
#         for j in range(5 - i):
#             print(" ", end="")
#         for j in range(i + 1):
#             print(n[j], end=" ")
#         print()
