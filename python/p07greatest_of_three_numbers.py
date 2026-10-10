a = int(input("Enter your first number: " ))
b = int(input("Enter your second number: " ))
c = int(input("Enter your third number: " ))

if(a > b and a > c):
    print(a , "=> it is greatest of all numbers")
elif(b > c):
    print(b , "=> it is greatest of all numbers")
    
else:
    print(c , "=> it is greatest of all numbers")
    