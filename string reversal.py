word = str(input("enter the string")).upper()
reverse = word[::-1]
print(reverse)

if word == reverse:
    print(" this", word + "is Palindrome")
else:
    print("this", word + "is n't palindrome")