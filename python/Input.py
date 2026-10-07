#input statement is used to accept value from the user 
name = input("enter your name: ")
print("welcome ", name)



#the type of the input result will always be a string
print(type(name))
#also u can type it to other data typyes by using statement like
#print(int(name)) gives error because it is invalid conversion
"""name = int(name)
print(int(name))#but this time i will pass any numeric value and it will run
print(type(name))"""
name = int(input("enter your name,plz pass numerical value: "))#by adding this statement this code will take two inputs
#and now it is also type casted to int so, this is another method of type casting
print(type(name))



#another example => this block of code is okay and execute perfectly, but usually we prefer 
#marks in float data type and age of int type for this we will do type casting as input statement
#gives string
"""name = input("Enter Your Name: ")
age = input("Enter your age: ")
marks  = input("Enter your marks: ")
print(name , age, marks)"""


name = input("Enter Your Name: ")
age = int(input("Enter your age: "))
marks  =float(input("Enter your marks: "))
print(name)
print(age)
print(marks)