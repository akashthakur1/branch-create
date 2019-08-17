a = input("enter the first value")
a = int(a)
#b = input("enter the second value")
#b = int(b)
#print(a, b)
if a % 2 == 0:
    print("this is even number", a)
else:
    print("this is odd number", a)



################################################################################other solutions ######
num = int(input("give me a number to check"))
check = int(input("give me a number to divide by"))

if num%4==0:
    print(num, "is a multiple of 4")
elif num%2==0:
    print(num, "is a even number")
else:
    print(num, "is a odd number")

if num%check==0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divides evenly by", check)


