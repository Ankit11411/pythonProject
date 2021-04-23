# OVERRIDE OVERLOADING
# EXCEPTION HANDLING

''''#Q) Enter age from user if you are >18 then you eligible for vote else not
try:
    age=int(input("Enter Age: "))
    if age>=18:
        print("YOU ARE ELIGIBle TO VOTE")
    else:
        # raise TypeError("you areNOT ELIGIBLE")
        raise Exception("you areNOT ELIGIBLE")
except ValueError:
    print("ENTER ONLY NUMBER")'''

# Q) ENTER Student detail from user name class rollno.

'''try:
    name = str(input("ENTER YOUR NAME: "))
    if len(name) > 7:
        raise MemoryError("Max 7 character Allowed!")
    clas = str(input("Enter your Department: "))
    rollno = int(input("ENter your roll no. "))


except ValueError:
    print("Enter only number")'''


try:
    a=int(input("ENTER NO"))
    print(a)
except ValueError:
    print("ENter only number")
finally:
    print("DONE")