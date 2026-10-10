#list is the built in data structure used to store an ordered, mutable(changeable) collection of items
#key characteristics:

#Ordered: Elements maintain the exact order in which they are inserted.

#• Mutable: You can change, add, or remove items after the list is created.

#• Allows Duplicates: The same value can appear multiple times.

#Mixed Data Types: A single list can contain integers, strings, booleans, and even other lists.

marks = [34.2, 65.3, 87.0, 39.2, 78.1]
print(marks)

student = ["Nimra Fatima", 167, "Artificial inteligence"]#can store differnet data types
print(student)

name =["Nimra", "Hamza", "Haider", "Hassan", "umar"]
print(name)

print(type(marks))
print(type(student))

#lists are mutable
marks[0] = 100
student[2] = "AI"

#also i can find the length of string by function len()
print(len(marks))
print(len(student))

#LIST SLICING => list_name[starting index : ending index] => ending index is not included
print(marks[0 : -1])#last element is not print
print(marks[0:])#print full list
print(marks[0:len(marks)])#prints full list

print(student[: -1])#it will automatically starts printing from zero index and the last element will not be printed

#slicing => negative indexing

print(name[-5 : -1])#print full list except last element
print(name[-5: ])#print full list

print(name[-1 : -6 : -1])