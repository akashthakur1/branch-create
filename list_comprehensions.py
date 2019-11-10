import random
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [item for item in a if item%2 == 0]


print(b)


c = []

for item in a:
    if item%2 == 0:
        c.append(item)

print(c)


numlist = []
list_length =random.randint(5, 15)
print(numlist)
print(list_length)
while len(numlist)< list_length:

    numlist.append(random.randint(1, 175))

evenlist = [number for number in numlist if number%2 == 0]

print(numlist)
print(evenlist)