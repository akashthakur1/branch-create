num = int(input("enter the number for range of list"))
print(num)

for item in range(1, num+1):
    if num % item == 0:
        print("divisor number is", item)
#    print(item)

