a = [1, 2, 2, 5, 8, 9, 10, 11, 12, 13, 15]
for item in a:
    if item < 5:
        print(item)

# it is one liner code for print elements by list
print([aa for aa in a if aa < 5])


print([aa for aa in a])

# it be will print line by line
for aa in a:
    print(aa)
