#type conversion => 'implicit conversion' it is done by python interpertor directly,
# does not require our manual changes
a = 2
b = 4.25
sum = a + b
print(sum)


#type casting => explicit conversion , u explicitly or manually tell the interpretor to change
#the value from the one type e.g from int to float or to string etc by following the method as 
# first write the type to which u are converting and then the small bracket and put the value
#inside the small brackets which u are type casting



a = "2"
b = 5

#print(sum)it will give error because string can not be added to integer type of value
#int(a)why this gives error because u are not storing it somewhere, rather u should create 
#another variable to store it for u
a = int(a)
sum = a + b 
print(sum)



#second method => easy one/direct method
a = int("2")
print(type(a))
b = 5
sum = a + b
print(sum)



"""Type casting takes place when a value can be meaningfully 
converted from one data type to another.
a = "nimra"
b = 8
a = int(a)
sum = a + b#this will give error"""


#similarly we can convert integer type to string as well
a = 3
b = str(a)
print(type(b))
