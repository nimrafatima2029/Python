a = [input("enter any sequence to check whether it is palindrome or not: ")]
b = a[::-1]
print(b)
if(b == a):
    print(b ,"it is palindrome")
else:
    print(b ,"it is not palindrome")

