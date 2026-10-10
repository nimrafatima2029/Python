#tuple is a built-in collection data type used to store multiple items in a single variable
#💡 Core Characteristics
#Ordered: Elements have a defined order that will not change.
#Immutable: You cannot change, add, or remove elements once the tuple is created.
#Allow Duplicates: Tuples can contain multiple identical values.
#Heterogeneous: A single tuple can hold elements of different data types (e.g., strings, integers, lists).

tup = (1, 2, 3, 4, 5, 6, 7, 8,)
print(type(tup))
print(tup[5]) #it will print element at index 5. thus, we can access elements from the tuple by its index
print(tup)
#you can not change the value at any index using tuples
#tup[0] = 9

#if we print empty tuple it's type will be tuple
tup = ()
print(tup)
print(type(tup))

#if we write a tuple with one element without any comma, python interpreter will consider it's type as int or str
tup = ("abc")
print(tup)
print(type(tup)) #output : string

tup = (1.0) 
print(tup)
print(type(tup)) #output : float

#in order to make it tuple we must have to put comma at the end of the element

tup = ("str",)
print(tup)
print(type(tup))


#tuple slicing

tup2 = ('n', 'i','m', 'r', 'a')
x =tup2[0 : 3]
print(x)
